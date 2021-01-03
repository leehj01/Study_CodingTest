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

# # 그래프알고리즘 
# ## 1. 자료구조 
# ### 스택

# +
stack = [] 

# 삽입(5) 삽입 (2) 삽입(3)  삽입 (7) 삭제() 삽입(1) 삽입(4) 삭제()

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1])  # 최상단 원소부터 출력
print(stack)
# -

# ### 큐 

# +
from collections import deque

# 큐 를 구현하기 위해 deque 라이브러리 사용
queue = deque()

# 삽입(5) 삽입 (2) 삽입(3)  삽입 (7) 삭제() 삽입(1) 삽입(4) 삭제()

queue.append(5) # 리스트와 동일하게 동작 
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()  
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse() # 다음 출력을 위해 역순으로 바꾸기
print(queue)  # 나중에 들어온 원소부터 출력

# list(queue) 를 하면, 리스트형으로 바뀜
# -

# ### 재귀함수

# +
def recursive_function():
    print('재귀 함수를 호출합니다.')
    recursive_function()
    
recursive_function()

# maximum recursion depth exceeded while calling a Python object : 재귀의 최대 깊이를 초과했다는 의미 
# -

# ### 재귀함수의 종료 조건 

# +
def recursive_function(i):
    # 100번째 출력했을 때 종료되도록 종료 조건 명시
    if i == 100:
        return 

    print( i , '번째 재귀함수에서', i +1 , '번째 재귀 함수를 호출합니다. ')
    recursive_function(i + 1)
    print(i, '번째 함수를 종료합니다')
    
recursive_function(1)


# -

# ### 재귀함수의 예시
# - 팩토리얼 구현 예제
# - n! = 1 x 2 x ... x ( n -1 ) x n
# - 수학적으로 0! 과 1!의 값은 1 이다.

# +
# 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    # 1부터 n 까지의 수를 차례대로 곱하기
    for i in range(1, n+1):
        result *= i
    return result


# 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n<= 1: # n이 1이하인 경우 1을 반환
        return 1
    # n! = n * (n -1) ! 를 그대로 코드로 작성하기
    return n* factorial_recursive(n-1)


# 각각의 방식으로구현한 n! 출력 
print('반복적으로 구현 : ', factorial_iterative(5))
print('재귀함수로 구현 : ', factorial_recursive(5))

# -

# ### 재귀함수 예시 2 
# - 최대공약수 계산 (유클리스 호제법) 예제
#
#
# - 두개의 자연수에 대한 최대공약수를 구하는 대표적인 알고리즘 
# - 유클리드 호제법
#      - 두자연수 A, B에 대하여 (A >B) A를 B로 나눈 나머지를 R이라고 함
#      - 이때, A와 B의 최대공약수는 B와 R의 최대 공약수와 같음

# +
def gcd(a, b):
    if a% b ==0 :
        return b
    else :
        return gcd (b, a % b)
    
print(gcd (192, 162))
# -








