/* Asia/Yekaterinburg */
/*show timezone;*/

explain analyse
with tbl as (select 
      				to_timestamp(cast(e.timestamp as bigint)/1000)::date as dt,
      				e.user_id,
      				e.url,
      				e.event_action 
			from events as e)


-- Вариант 1. Группировка			
-- Execution Time: 1.170 ms
select count(t.user_id)/2 as count_uniq_users
from (select t.user_id, count(t.event_action)over(partition by t.user_id) as is_bool
      from tbl as t
      where t.dt >= '2022-09-12' 
            and t.dt<='2022-09-22' 
            and t.event_action in ('click_go_to_sberbank','click_link_part')
      group by t.user_id, t.event_action) as t 
where t.is_bool = 2;


-- Вариант 2. Пересечение
-- Execution Time: 8.468 ms	
/*select count(*)as count_uniq_users 		
from	(select distinct t.user_id	
	      from tbl as t
	      where t.dt >= '2022-09-12' 
	            and t.dt<='2022-09-22' 
	            and t.event_action in ('click_go_to_sberbank')
	    intersect 
		select distinct tt.user_id
		      from tbl as tt
		      where tt.dt >= '2022-09-12' 
		            and tt.dt<='2022-09-22' 
		            and tt.event_action in ('click_link_part')) as ttt*/
			
-- Вариант 3. Подзапрос
-- Execution Time: 10.441 ms
/*select count(distinct tt.user_id) as count_uniq_users
from tbl as tt
where tt.dt >= '2022-09-12' 
	  and tt.dt<='2022-09-22' 
	  and tt.event_action = 'click_go_to_sberbank'
	  and exists (select distinct t.user_id
	              from tbl as t
	              where t.dt >= '2022-09-12' 
	                    and t.dt<='2022-09-22' 
	                    and t.event_action = 'click_link_part'
	                    and t.user_id = tt.user_id)*/
			
-- Вариант 4. Джоин
-- Execution Time: 8.252 ms		
/*select count(distinct tt.user_id) as count_uniq_users	
from tbl as tt inner join (select distinct t.user_id
		                    from tbl as t
		                    where t.dt >= '2022-09-12' 
		                          and t.dt<='2022-09-22' 
		                           and t.event_action = 'click_link_part') as ttt 
		       on tt.user_id = ttt.user_id
where tt.dt >= '2022-09-12' 
	 and tt.dt<='2022-09-22' 
     and tt.event_action = 'click_go_to_sberbank'*/

-- Вариант 5. Оконные функции
-- Execution Time: 18.945 ms
/*select count(distinct (ttt.user_id)) as count_uniq_users
from (select tt.*, 
	       sum(tt.is_bool1) over (partition by tt.user_id) as sum_is_bool1,
	       sum(tt.is_bool2) over (partition by tt.user_id) as sum_is_bool2
	  from	(select t.user_id,
		            case when t.event_action = 'click_go_to_sberbank' then 1 else 0 end as is_bool1,
		            case when t.event_action = 'click_link_part' then 1 else 0 end as is_bool2
		    from tbl as t
		    where t.dt >= '2022-09-12' and t.dt<='2022-09-22') as tt) as ttt
where ttt.sum_is_bool1 >=1 and ttt.sum_is_bool2 >=1*/
