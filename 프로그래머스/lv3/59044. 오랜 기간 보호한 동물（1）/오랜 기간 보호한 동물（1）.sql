-- 코드를 입력하세요
SELECT ANIMAL_INS.NAME, ANIMAL_INS.DATETIME
FROM ANIMAL_INS
LEFT JOIN ANIMAL_OUTS ON ANIMAL_OUTS.ANIMAL_ID = ANIMAL_INS.ANIMAL_ID
WHERE ANIMAL_OUTS.ANIMAL_ID is NULL
ORDER BY ANIMAL_INS.DATETIME ASC 
LIMIT 3