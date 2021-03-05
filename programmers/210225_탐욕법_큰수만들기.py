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
# 어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.
#
# 예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 이 중 가장 큰 숫자는 94 입니다.
#
# 문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다. number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.
#
# 제한 조건
# number는 1자리 이상, 1,000,000자리 이하인 숫자입니다.
# k는 1 이상 number의 자릿수 미만인 자연수입니다.

# ## 처음 했던 방법

def solution(number, k):
    num = [i for i in number]
    idx = 0
    
    if num[0] == '9':
        return(''.join(num[:len(num) - k]))

    for i in num.copy():
        if i < max(num[idx:idx+k+1]):
            k -= 1 
            num.remove(i)
        else : 
            idx += 1
            
    return ''.join(num)


# ## 다시 시작

def pop_now( num ):
    now = 0
    for i in range(len(num) -1 ):
        if num[i] == '9':
            break
            
        if num[i] < num[i+1]:
            num.pop(now)
            break
        else :
            now += 1 


# +
number = "99991"
num = list(number)
k = 3
length = len(list(number)) - k

while True :
    
    pop_now( num )
    k -= 1
    
    if k == 0:
        break
        
if len(num) != length  :
    num = num[:length]
    
print(''.join(num))
# -

num[:4]


