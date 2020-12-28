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

# # 1. 알고리즘 성능평가
# - 수행시간 측정 소스코드 예제

# +
import time
start_time = time.time() # 측정시작

# 프로그램 소스코드
end_time = time.time() # 측정 종료.
print("time : " , end_time - start_time ) # 수행 시간 출력 
# -

# # 2. 파이썬 문법정리
# ## 2-1. 자료형 
# ###  2.1.1. 실수

# +
a = 0.3 + 0.6
print(a)

if  a == 0.9:
    print(True)
else:
    print(False)


# +
a = 0.3 + 0.6
print(round(a,4))

if  round(a,4) == 0.9:
    print(True)
else:
    print(False)

# 실행결과 0.9 True
# -

# ### 2.1.4. 리스트 자료형

# +
# 0부터 9까지의 수를 포함하는 리스트
array = [ i for i in range(10) ]
print(array)

# 0부터 19까지 수 중에서 홀수만 포함하는 리스트
array = [ i for i in range(20) if i % 2 == 1 ]
print(array)

# 1부터 9까지의 수 들의 제곱 값을 포함하는 리스트
array = [ i * i for i in range(1,10) ]
print(array)

# +
# 코드 1 : 리스트 컴프리헨션
array = [ i for i in range(20) if i % 2 == 1 ]
print(array)

# 코드 2 : dlfqkswjrdls zhem
array = []
for i in range(20):
    if i % 2 == 1:
        array.append(i)
print(array)

# +
# N X M 크기의 2차원 리스트 초기화
n = 4
m = 3
array = [[0] * m for _ in range(n)]

array[1][1] = 5
print(array)

# +
# 잘못된 방법
n = 4
m = 3

array = [[0] * m] * n

array[1][1] = 5
print(array)


# - 언더바는 언제 사용하는가?
# : 반복을 수행하되, 반복을 위한 변수의 값을 무시하고자 할때, 언더바(_)를 자주 사용함


# 1부터 9까지 자연수 더하기

summary = 0
for i in range(1, 10):
    summary += i
print(summary)
# -

# hola 반복
for _ in range(5):
    print("hola")

# - 변수명.remove( 특정값 ) : 특정한 값을 가지는 원수를 제거하는데, 값을 가진 원수가 여러개라면 하나만 제거한다. 

# +
a = [ 1,2,3,4,5,5,5]
remove_set = { 3,5 } # 집합 자료형 : 특정한 원소의 존재 유무만을 판단할 때 유용함 

result = [i for i in a if i not in remove_set]
print(result) # [1, 2, 4]
# -

# ### 2.1.5. 문자열 자료형 
# - 백슬래시(\)를 사용하면, 큰따옴표나 작은 따옴표를 원하는 만큼 포함시킬 수 있음

data = "DO YOU LIKE \"PYTHONE\"?"
print(data)


# +
a = "hello"
b = "world"

print(a + " " + b)
# -

# ### 2.1.8. 집합 자료형
# - 집합 연산에서 합집합 / 교집합 / 차집합 연산 이 존재함

# +
a = set([ 1,2,3,4,5 ])
b = set([ 3,4,5,6,7 ])

# 합집합 
print( a | b )  # {1, 2, 3, 4, 5, 6, 7}
print( a & b )  # {3, 4, 5}
print( a - b )  #  {1, 2}
# -

# # 2. 파이썬 문법정리
# ## 2-2 .기본 입출력
# - 자주 사용되는 표준 입력 방법

a,b,c = map(int , input( ).split( ) )
print(a, b, c)

# - 입력을 최대한 빠르게 받아야하는 경우
#     - sys.stdin.readline( ) 메서드를 사용함
#     - 단, 입력후 엔터가 줄바꿈기호로 입력되므로 rstrip( ) 메서드를 함께 사용함

# +
import sys

# 문자열 입력 받기
data = sys.stdin.readline().rstrip()
print(data)
# -


