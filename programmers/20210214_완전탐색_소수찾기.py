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

# ### 문제 설명
# 한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.
#
# 각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

# +
from itertools import permutations 

numbers = '0112462'
result = list(permutations( numbers , 7))


# -

def search_prime(num):
    num = int(num)
    for i in range(2, int(math.sqrt(num)) + 1) :
        if num % i == 0 :
            return '소수아님 '
    return '소수'


numbers = '011'
prime = []
for i in range( 1, len(numbers )):
    perm = list(permutations( numbers , i ))
    for j in perm :
        if search_prime(''.join(j)) == '소수':
            prime.append(''.join(j))

len(set(prime) - {'1', '0'})


