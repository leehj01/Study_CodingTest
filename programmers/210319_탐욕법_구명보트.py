# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.7.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# ## 첫번째 시도 : 정확성은 맞지만 효율성 거지가 됨 

# +
people = [70, 50, 80, 50]
limit = 100
people.sort(reverse = True)
cnt = 0
for i in range(len(people)):
    tmp = 0
    for j in range(i +1 ,len(people)):
        if people[i] + people[j] <= limit :
            print('작아', people[i],people[j])
            people.remove(people[j])
            tmp += 1
            cnt += 1
            print(people ,cnt)
            break
            
    
    if tmp == 0 and i <= len(people)-1:
        cnt += 1
        print(people, cnt)

print(cnt)

# -

# ## 질문목록의 HINT로 직접 풀기
# 우선, 무게 순서대로 사람을 줄 세웁니다.
# 맨 앞에 있는 사람이랑 맨 뒤에 있는 사람이랑 보트에 담을 수 있으면 같이 보냅니다.
# 같이 못 보내면 맨 앞의 사람만 보트에 태워서 보내버립니다.
# 이걸 반복하다가, 맨 앞의 사람이 보트 제한 무게의 절반 이하가 되면,
# 무조건 맨 뒤의 사람과 같이 보낼 수 있으므로 남은 사람은 남은 사람 수의 절반의 보트만 있으면 됩니다.

# +
from collections import deque

def solution(people, limit):
    people.sort(reverse = True)
    people_q = deque(people)
    cnt = 0

    while people_q:
        if people_q[0] + people_q[-1] <= limit  and  people_q[0] > limit//2 and len(people_q) >= 2  :
            people_q.popleft()
            people_q.pop()
            cnt += 1

        elif people_q[0] + people_q[-1] > limit and  people_q[0] > limit//2:
            people_q.popleft()
            cnt += 1

        elif len(people_q) >= 2:
            people_q.popleft()
            people_q.pop()
            cnt += 1

        else :
            people_q.popleft()
            cnt += 1

    return cnt
