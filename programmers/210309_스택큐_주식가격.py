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

# ###  for 문을 이용한 코드

def solution(prices):
    result =[0] * len(prices)
    for i in range(len(prices)):
        for j in range(i, len(prices)):
            if prices[i] > prices[j] :
                result[i] = j-i 
                break
        if result[i] == 0 :
            result[i] = len(prices) -1  - i
    return result


# ### 스택을 이용한 남의 코드

def solution(p):
    ans = [0] * len(p)
    stack = [0]
    for i in range(1, len(p)):
        if p[i] < p[stack[-1]]:
            for j in stack[::-1]:
                if p[i] < p[j]:
                    ans[j] = i-j
                    stack.remove(j)
                else:
                    break
        stack.append(i)
    for i in range(0, len(stack)-1):
        ans[stack[i]] = len(p) - stack[i] - 1
    return ans
