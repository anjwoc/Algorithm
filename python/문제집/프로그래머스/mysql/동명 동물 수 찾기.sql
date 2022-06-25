-- 코드를 입력하세요
SELECT NAME, COUNT(NAME) as COUNT
from animal_ins
group by name
having count (name) > 1
order by name