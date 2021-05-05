with tbl as (select *,
		            round(cast(t.revenue as real)/(select sum(t.revenue) from df_sql as t),3) as percentage
             from df_sql as t
             order by t.revenue desc),
     tbl2 as (select *,
		             sum(tbl.percentage) over (order by tbl.revenue desc rows between unbounded preceding and current row) as percentage_acc
             from tbl)
             select *,
                   case
                       when (percentage_acc>=0) and(percentage_acc<0.8) then "A"
                       when (percentage_acc>=0.8) and(percentage_acc<0.95) then "B"
                        else "C"
                   end as group_client
             from tbl2;