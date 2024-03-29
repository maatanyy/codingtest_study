-- 코드를 입력하세요
SELECT FOOD_PRODUCT.PRODUCT_ID, PRODUCT_NAME, SUM(PRICE * AMOUNT) as TOTAL_SALES
FROM FOOD_PRODUCT, FOOD_ORDER
WHERE FOOD_PRODUCT.PRODUCT_ID = FOOD_ORDER.PRODUCT_ID 
AND PRODUCE_DATE LIKE '2022-05%'
GROUP BY PRODUCT_ID
ORDER BY TOTAL_SALES DESC, FOOD_PRODUCT.PRODUCT_ID 