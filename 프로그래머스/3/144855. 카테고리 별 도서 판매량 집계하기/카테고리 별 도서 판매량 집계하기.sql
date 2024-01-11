SELECT A.category, sum(sales) AS total_sales
FROM book A
INNER JOIN BOOK_SALES B ON A.book_id = B.book_id
WHERE B.SALES_DATE LIKE '2022-01%'
GROUP BY A.category
ORDER BY A.category;