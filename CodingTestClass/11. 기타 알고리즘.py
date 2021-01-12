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

# ## 소수의 판별

# +
# 소수 판별 함수
def is_prime_number(x):
    # 2부터 (x - 1)까지의 모든 수를 확인하며
    for i in range(2, x) :
        # x 가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

print(is_prime_number(4))
print(is_prime_number(7))

# +
import math

# 소수 판별 함수
def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어 떨어진다면
        if x % i == 0 : 
            return False # 소수가 아님
    return True # 소수임

print(is_prime_number(4))
print(is_prime_number(7))
# -

# ## 다수의 소수 판별 : 에라토스테네스의 체

# +
import math

n = 1000 # 2부터 1,000까지의 모든 수에 대하여 소수 판별
array = [ True for i in range(n+1)] #처음엔 모든 수가 소수(True)인 것으로 초기화 ( 0과 1은 제외)

# 에라토스테네스의 체 알고리즘
for i in range(2, int(math.sqrt(n)) + 1): #2부터 n의 제곱근까지의 모든 수를 확인하며
    if array[i] == True : # I가 소수인 경우(남은 수인 경우)
        # i 를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

# 모든 소수 출력
for i in range(2, n +1 ):
    if array[i]:
        print(i, end = ' ')
# -
# ## 투포인터 알고리즘

# +
n = 5 # 데이터의 개수 N
m = 5 # 찾고자 하는 부분합 M
data = [ 1, 2, 3, 2, 5] # 전체 수열


count = 0
interval_sum = 0
end = 0

# start 를 차례대로 증가시키며 반복
for start in range(n):
    # end 를 가능한 만큼 이동시키기
    while interval_sum < m and end < n :
        interval_sum += data[end]
        end += 1
        
    # 부분합이 m 일때 카운트 증가
    if interval_sum == m :
        count += 1
    interval_sum -= data[start]
    
print(count) # 3
# -

# ## 정렬되어있는 두 리스트의 합집합

# +
# 사전에 정렬된 리스트 A와 B 선언
n, m = 3 ,4 
a = [1, 3 , 5]
b = [2, 4, 6, 8]

# 리스트 a와 b의 모든 원소를 담을 수 있는 크기의 결과 리스트 초기화

result = [0] * (n + m)
i = 0
j = 0
k = 0

# 모든 원소가 결과 리스트에 담길 때까지 반복
while i < n or j < m :
    # 리스트 b의 모든 원소가 처리되었거나, 리스트 a의 원소가 더 작을 때
    if j >= m or (i < n and a[i] <= b[j]):
        # 리스트 a의 원소를 결과 리스트로 옮기기
        result[k] = a[i]
        i +=1
    # 리스트 a의 모든 원소가 처리되었거나, 리스트 b의 원소가 더 적을 때
    else:
        # 리스트 b의 원소를 결과 리스트에 옮기기
        result[k] = b[j]
        j += 1
    k += 1

# 결과 리스트 출력
for i in result :
    print(i, end = '') # 1234568
# -

# ## 구간합 문제

# +
# 데이터의 개수 n과 데이터 입력 받기
n = 5
data = [10, 20, 30, 40, 50]

# 접두사 합 배열 계산
sum_value = 0
prefix_sum = [0]
for i in data:
    sum_value += i
    prefix_sum.append(sum_value)
    
# 구간합 계산 ( 세번째 수부터 네번째 수까지 )
left = 3
right = 4
print(prefix_sum[right] - prefix_sum[left - 1]) # 70
# -

# ## 순열


# +
import itertools

data = [1,2]

for x in itertools.permutations(data, 2):
    print(list(x))

#
[1, 2]
# [2, 1]
# -

# ## 조합

# +
import itertools

data = [1,2,3]

for x in itertools.combinations(data, 2) :
    print(list(x), end = ' ')

# [1, 2] [1, 3] [2, 3]
# -


