SELECT hc.hacker_id, hc.name, sum(sub.sc) total_score
FROM (
    SELECT hacker_id, challenge_id, max(score) sc
    FROM Submissions
    GROUP BY hacker_id, challenge_id
    ) sub
    LEFT JOIN Hackers hc ON hc.hacker_id = sub.hacker_id 
GROUP BY sub.hacker_id, hc.name
HAVING total_score != 0
ORDER BY sum(sub.sc) desc, hc.hacker_id
