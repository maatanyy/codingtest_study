-- 코드를 입력하세요
SELECT RI.REST_ID, REST_NAME, FOOD_TYPE, FAVORITES,ADDRESS, 
ROUND(AVG(REVIEW_SCORE),2) as SCORE
FROM REST_INFO as RI, REST_REVIEW as RR
WHERE RI.REST_ID = RR.REST_ID
AND ADDRESS LIKE '서울%' 
GROUP BY RI.REST_ID
ORDER BY SCORE DESC, FAVORITES DESC