-- 코드를 입력하세요
SELECT hour(datetime) as HOUR, count(*) as COUNT
FROM ANIMAL_OUTS
GROUP BY hour(datetime)
HAVING HOUR >= 9 AND HOUR < 20
ORDER BY hour(datetime)