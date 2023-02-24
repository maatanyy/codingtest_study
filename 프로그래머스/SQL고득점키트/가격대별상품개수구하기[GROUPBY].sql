--# PRODUCT 테이블에서 만원 단위의 가격대 별로 상품 개수를 출력하는 SQL 문을 작성해주세요.
--# 이때 컬럼명은 각각 컬럼명은 PRICE_GROUP, PRODUCTS로 지정해주시고 가격대 정보는
--# 각 구간의 최소금액(10,000원 이상 ~ 20,000 미만인 구간인 경우 10,000)으로 표시해주세요.
--# 결과는 가격대를 기준으로 오름차순 정렬해주세요.
--
--# 나는 ROUND를 생각했는데 TRUNCATE라는 자르는게 있었다!.
--# 그리고 다른 풀이를 보니 CASE로 나누는 게 있다 , THEN, END 그리고 괄호를 사용한다는 걸 기억하면 좋을듯

SELECT TRUNCATE(PRICE,-4) as PRICE_GROUP, COUNT(*) as PRODUCTS
FROM PRODUCT
GROUP BY PRICE_GROUP
ORDER BY PRICE_GROUP;


# CASE Example
# SELECT (CASE WHEN PRICE BETWEEN 0 AND 9999 THEN '0' .... END)