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

# ## for 문


