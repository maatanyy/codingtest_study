-- 코드를 입력하세요
SELECT AO.ANIMAL_ID, AO.ANIMAL_TYPE, AO.NAME
FROM ANIMAL_INS as AI
JOIN ANIMAL_OUTS as AO 
on AI.ANIMAL_ID = AO.ANIMAL_ID
where AI.SEX_UPON_INTAKE like 'Intact%' and (AO.SEX_UPON_OUTCOME like 'Spayed%' or 
AO.SEX_UPON_OUTCOME like 'Neutered%')
ORDER BY AO.ANIMAL_ID ASC;
