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
start_time = time.time() # 측정시작.

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
# ## 2-3 조건문


score = 95
result = "Success" if score >= 90 else "Fail"
print(result) 

# ## 2-4 반복문

# +
# 1부터 9까지의 홀수의 합을 구할 때 

result = 0

for i in range(1,10):
    if i % 2 == 0: 
        continue  # 짝수이면 건너뛰고 홀수여야 result에 더해짐
    
    result += i

print(result)  # 25

# +
# 합격여부 판단하는데, 특정번호의 학생은 제외하기
score = [90, 85, 77, 65, 97 ]
pass_student = {2,4}

for i in range(5):
	if i + 1 in pass_student:
		continue
	if score[i] >= 80 :
		print(i + 1, "번 학생은 합격입니다" )
# -

for i in range(2,10):
    for j in range(1, 10):
        print(i, "x", j, "=", i*j)
    print()

# ## 함수와 람다표현식

# def 함수명(매개변수):
# 	실행할 소스코드
# 	return 반환 값

# +
a = 0

def func():
	global a
	a += 1 

for i in range(10):
	func()

print(a)

# +
a = 0

def func():
	global a
	a += 1 

for i in range(10):
	func()

print(a)

# +
array  = [ ('홍길동',50), ( '이순신',32), ('아무개', 74) ] 

print(sorted( array, key= lambda x: x[1]  ) )

# +
list1 = [ 1, 2,3,4,5 ]
list2 = [ 6, 7, 8, 9, 10]

result = map(lambda a, b : a+ b , list1, list2 )
print(list (result)) # [ 7, 9 , 11, 13 , 15 ]
# -

# ## 2-6. 실전에서 유용한 표준라이브러리

result = eval("(3+5)*7")
print(result)  # 56

# +
from itertools import permutations

data = ['A' , 'B', 'C' ]
result = list(permutations( data, 3)) # 3개를 골라 모든 순열 구하기
print(result)

# +
from itertools import combinations

data = ['A' , 'B', 'C' ]
result = list(combinations( data, 2 ) )  # 2개를 골라 모든 순열 구하기
print(result)

# +
from itertools import product

data = ['A' , 'B', 'C' ]
result = list(product( data, repeat = 2)) # 2개를 뽑아 모든 순열 구하기 ( 중복 허용 )
print(result)

# +
from itertools import combinations_with_replacement

data = ['A' , 'B', 'C' ]
result = list(combinations_with_replacement( data, 2) )
 # 2개를 뽑아 모든 조합 구하기 ( 중복 허용 )
print(result)

# +
from collections import Counter

counter = Counter(['red','blue','red','green','blue','blue'] )

print(counter['blue']) # blue가 등장한 횟수 출력 # 3
print(dict(counter)) # 사전 자료형으로 반환 # {'red' : 2, 'blue' : 3, 'green' :1 }

# +
# 최대공약수 gcd()
import math

# 최소공배수 (lcm)을 구하는 함수
def lcm(a, b):
    return a*b // math.gcd(a,b)

a= 21
b=14

print(math.gcd(21,14)) # 최대공약수 계산 7
print(lcm (21,14)) # 최소공배수 계산  
