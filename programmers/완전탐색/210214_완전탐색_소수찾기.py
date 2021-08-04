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

from itertools import permutations


# +
# 내 풀이 
def search(num):  # 소수를 판별해주는 코드. ( 이코테 마지막 강의에 수록된 것이 나와서 반갑 )
    num = int(num)
    for i in range(2, int(math.sqrt(num)) + 1) :
        if num % i == 0 :
            return '소수아님 '
    return '소수'

def solution(numbers):  
    prime = []
    for i in range( 1, len(numbers) + 1):
        perm = list(permutations( numbers , i )) # 모든 경우의 수를 찾아줌 
        prime.extend([''.join(j) for j in perm if search(''.join(j)) == '소수'])  # 소수인 것만 리스트에 담아줌 
    return len(set(list ( map( int, prime )) ) - {1, 0} )  # int로 한 이유는 011 == 11 은 같게 만들기 위해서 // 소수는 0,1 포함 안함  

# +
# 남의 코드  
# '에라토스테네스 체'를 사용하여 풀었음. 모든 경우의 소수를 구하는 알고리즘?이라 불필요할 것이라 생각했으나, 초 간단 
# 모든 수의 배수를 구해서, 제거함 == 즉, 소수가 됨.
# 비트 연산자를 사용해서 풀어서 애초에 난 불가능한 코드..   


from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))  # 모든 경우의 수를 |= 로 담음...
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):     # a 의 제곱근까지의 값을 확인 ( range니깐 +1 ) 
        a -= set(range(i * 2, max(a) + 1, i))      # i 의 모든 배수를 range와 set을 이용해서 구함 < 천재.. ? >  
    return len(a)
