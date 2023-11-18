-- 코드를 입력하세요
SELECT CAR_ID,
case when count(case when start_date <= '2022-10-16' and end_date >= '2022-10-16' 
                then 1 else null end) > 0 then '대여중' else '대여 가능' end AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
ORDER BY CAR_ID DESC;


