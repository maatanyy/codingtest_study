-- 코드를 입력하세요
SELECT FP.PRODUCT_ID, FP.PRODUCT_NAME, SUM(FP.PRICE * FO.AMOUNT) as TOTAL_SALES
FROM FOOD_PRODUCT as FP 
JOIN FOOD_ORDER as FO ON FP.PRODUCT_ID = FO.PRODUCT_ID
WHERE PRODUCE_DATE LIKE '2022-05%'
GROUP BY FP.PRODUCT_ID
ORDER BY TOTAL_SALES DESC, FP.PRODUCT_ID ASC