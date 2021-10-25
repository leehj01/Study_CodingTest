select city, LENGTH(city)
from station
where id = (select id
    from station
    order by LENGTH(city), city
    limit 1)
or id = (
        select id
        from station
        order by LENGTH(city) desc , city
        limit 1
    )