-- 코드를 입력하세요
SELECT p.PRODUCT_ID, p.PRODUCT_NAME, SUM(p.PRICE*o.AMOUNT) as TOTAL_SALES
FROM FOOD_PRODUCT as p
JOIN FOOD_ORDER as o ON
    p.PRODUCT_ID = o.PRODUCT_ID
WHERE MONTH(o.PRODUCE_DATE) = "5"
GROUP BY p.PRODUCT_ID
ORDER BY TOTAL_SALES DESC, PRODUCT_ID ASC