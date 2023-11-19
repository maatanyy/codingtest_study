-- 코드를 입력하세요
SELECT USER_ID, NICKNAME, 
CONCAT(CITY,' ',STREET_ADDRESS1,' ',STREET_ADDRESS2) as 전체주소,
    CONCAT(LEFT(TLNO,3),'-',MID(TLNO,4,4),'-',RIGHT(TLNO,4)) as 전화번호
FROM USED_GOODS_BOARD
JOIN USED_GOODS_USER ON USED_GOODS_BOARD.WRITER_ID = USED_GOODS_USER.USER_ID
GROUP BY USER_ID
HAVING COUNT(*)>=3
ORDER BY USER_ID DESC