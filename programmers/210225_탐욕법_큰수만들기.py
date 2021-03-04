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

def solution(number, k):
    num = [i for i in number]
    idx = 0

    for i in num.copy():
        if i < max(num[idx:idx+k+1]):
            k -= 1 
            num.remove(i)
        else : 
            idx += 1
            
    if len(num) != len(num) - k :
         return(''.join(num[:len(num) - k]))
    else :
         return ''.join(num)


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


# +
number = '99991'
k = 3
num = [i for i in number]
num_copy = num.copy()
idx = 0

if num[0] == '9':
    print(''.join(num[:len(num) - k]))
    

for i in num_copy:
    if i < max(num[idx:idx+k+1]):
        k -= 1 
        num.remove(i)
    else : 
        idx += 1
        
if len(num) != len(num) - k :
    print(num[0])
# -


