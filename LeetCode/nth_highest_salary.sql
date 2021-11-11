
-- 문제 풀이1
CREATE FUNCTION getNthHighestSalary(N INT)
RETURNS INT
BEGIN
  RETURN (
            SELECT CASE WHEN COUNT(sub.Salary) < N THEN NULL
                        ELSE MIN(sub.Salary)
                    END
            FROM (
                SELECT DISTINCT Salary
                FROM Employee
                ORDER BY Salary DESC
                LIMIT N
            ) sub
  );
END


-- 문제 풀이2
CREATE FUNCTION getNthHighestSalary(N INT)
RETURNS INT
BEGIN
  RETURN (
          SELECT IF(Count(sub.salary) < N, NULL, MIN(sub.salary))
          FROM(
                 SELECT DISTINCT Salary
                 FROM employee
                 ORDER BY Salary DESC
                 LIMIT N
              ) sub
         );
END

-- 문제 풀이 3
CREATE FUNCTION getNthHighestSalary(N INT)
RETURNS INT
BEGIN
  DECLARE A INT;
  SET A = N - 1;
  RETURN (
          SELECT DISTINCT Salary
          FROM employee
          ORDER BY Salary DESC
          LIMIT A, 1 -- N-1번째까지는 지우고 그 N번째를 가져오라는 의미
         );
END

-- 문제풀이 4
CREATE FUNCTION getNthHighestSalary(N INT)
RETURNS INT
BEGIN
-- DECLARE A INT;
  SET N = N - 1;
  RETURN (
          SELECT DISTINCT Salary
          FROM employee
          ORDER BY Salary DESC
          LIMIT N, 1 -- N-1번째까지는 지우고 그 N번째를 가져오라는 의미
		 );
END

-- 문제풀이 5
CREATE FUNCTION getNthHighestSalary(N INT)
RETURNS INT
BEGIN
-- DECLARE A INT;
  SET N = N - 1;
  RETURN (
          SELECT DISTINCT Salary
          FROM employee
          ORDER BY Salary DESC
          LIMIT 1 OFFSET N -- 중간에 , 안들어감
		 );
END