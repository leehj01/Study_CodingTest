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

# 문제 설명
# 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.
#
# 제한사항
# prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
# prices의 길이는 2 이상 100,000 이하입니다.

# ### while 문으로 시도 

# +
prices = [1, 2, 3, 2, 3]
result = []
idx = 0

while True :
    i = 1
    cnt = 0
    print(cnt)
    print(prices[0] , prices[i])
        
    while  prices[0] < prices[i] and i < len(prices) :
        
        print(prices[0] , prices[i], i, cnt)
        i += 1 
        cnt += 1
            
        if i == len(prices) :
            prices.pop(0)
            print('prices',prices)

    result.append(cnt)
    print(result,'-------------')
    
    if len(prices) == 0:
        break
        
# -

# ## 두번째 시도

def solution(prices):
    answer =[]

    for i, v in enumerate(prices):
        cnt = -1
        for j, x in enumerate(prices):
            if v <= x and i <= j :
                cnt += 1
            else :
                cnt += 0 

        answer.append(cnt)
    return answer


[1, 2, 3, 4, 3]

prices = [5, 8, 6, 2, 4, 1] 

# +
prices =[1, 2, 3, 2, 3, 3]
result =[0] * len(prices)

for i, v in enumerate(prices):
    for j, x in enumerate(prices[i:]):
        if v <= x :
            print()
            result[i] += 1
            
        else :
            break
            
# answer = list(map(lambda n, m :  n-1  if m < prices[-1] else n , result, prices))
# print(answer)
# answer[-1] = 0
# answer
result

# -


prices[-1]

r = list(map(lambda a,b: a+b, [1,2,3], [10,20,30]))
print(r) # [11, 22, 33]

list(map(lambda n, m :  n-1  if m <= prices[-1] else n , result, prices))

# ## 세번째 시도


