SELECT MIN(CASE WHEN occupation = 'Doctor' THEN Name ELSE NULL END) doctor
     , MIN(CASE WHEN occupation = 'Professor' THEN Name ELSE NULL END) professor
    , MIN(CASE WHEN occupation = 'Singer' THEN Name ELSE NULL END) singer
    , MIN(CASE WHEN occupation = 'Actor' THEN Name ELSE NULL END) actor
FROM (
    SELECT occupation, name
            , ROW_NUMBER() OVER (PARTITION BY occupation ORDER BY name) rn 
    FROM Occupations) t
GROUP BY rn
ORDER BY rn 
