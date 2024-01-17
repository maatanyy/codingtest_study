SELECT
    MCDP_CD as "진료과코드"
    , count(APNT_NO) as "5월예약건수"
from APPOINTMENT
where APNT_YMD like "2022-05-%"
group by MCDP_CD
order by 2 asc, 1 asc