-- Для решения задания использовалась БД PostgreSQL
-- Вопрос 1. 
WITH tbl as (SELECT sb.client_id,
	sb.start_dt,
	sb.end_dt,
	sb.channel,	
	(CASE
		WHEN (LAG(sb.channel) OVER(PARTITION BY sb.client_id ORDER BY sb.start_dt)) = sb.channel THEN 0 ELSE 1
	END ) as sum	
FROM PUBLIC.SBER AS sb)

SELECT sb1.client_id,
	sb1.start_dt,
	sb1.end_dt,
	sb1.channel,
	SUM(sb2.sum) OVER(PARTITION BY sb1.client_id ORDER BY sb1.start_dt) as key
FROM PUBLIC.SBER as sb1 LEFT JOIN  tbl as sb2 ON (sb1.client_id = sb2.client_id AND sb1.start_dt=sb2.start_dt)


-- Вопрос 2а. 
SELECT *
FROM PUBLIC.SBER as sb
WHERE (sb.start_dt>='01.11.2020' AND '30.11.2020'>=sb.end_dt AND sb.channel='Премьер')

-- Вопрос 2б. 
SELECT *
FROM PUBLIC.SBER as sb
WHERE (sb.start_dt>='01.11.2020' 
	   AND '30.11.2020'>=sb.end_dt 
	   AND sb.channel='Премьер' 
	   AND date_part('day',age(sb.end_dt, sb.start_dt))=10)
