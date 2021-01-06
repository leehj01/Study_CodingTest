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

# ## 선택 정렬 알고리즘

# +
array = [7 , 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)) :
    min_index  = i # 가장 작은 원소의 인덱스
    for j in range(i + 1 , len(array)) :
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # 스와프
    
print(array)   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -

# ### 스와프 소스코드 

# +
# 파이썬 스와프 소스코드 
# 0 인덱스와 1 인덱스의 원소 교체하기

array= [3,5 ]

array[0] , array[1] = array[1], array[0]

print(array)
# -

# ## 삽입 정렬 알고리즘 

# +
array = [7,5 ,9,0,3,1,6,2,4,8]

for i in range(1, len(array)) :
    for j in range(i, 0, -1): # 인덱스 i 부터 1까지 1씩 감소하면서 반복하는 문법
        if array[j] < array[j - 1 ] : # 한카니씩 왼쪽으로 이동 
            array[j] , array[j-1] = array[j-1], array[j]
        else: # 자기보다 작은 데이터를 만다면 그 위치에서 멈춤
            break

print(array)  
# -

# ## 퀵 정렬 알고리즘

# +
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start > end : # 원소가 1개인 경우 종료
        return
    
    pivot = start # 피벗은 첫번째 원소
    left = start + 1
    right = end
    while left <= right :
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1 
            
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
            
        if left > right : # 엇갈렸다면 작은 right -=1 데이터와 피벗을 교채
            array[right], array[pivot] = array[pivot], array[right]
            
        else : # 엇갈리지 않았다면 작은 데이터와 큰데이터 교체
            array[left], array[right] = array[right] , array[left]
            
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right -1 )
    quick_sort(array, right +1 , end )
    
            
quick_sort(array, 0, len(array) -1 )
print(array)
# -

# ### 퀵 정렬 다른 코드 

# +
array = [5, 7, 9 , 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array) :
    # 리스트가 하나 이하의 원소만을 담고있다면 종료
    if len(array) <= 1 :
        return array
    
    pivot = array[0]
    tail = array[1:] # 피벗을 제외한 리스트
    
    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [ x for x in tail if x > pivot] # 분활된 오른쪽 부분 
    
    # 분할 이후 왼쪽 부분과 오른쪽부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


print(quick_sort(array))
# -

# ## 계수 정렬 알고리즘 

# +
# 모든 원소의 값이  0보다 크거나 같다고 가정 
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

# 모든 범위를 포함하는 리스트선언(모든 값을 0으로 초기화)
count = [0] * (max(array) + 1)
print(count)

for i in range(len(array)) :
    count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가

print(count)
    
for i in range(len(count)) : # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]) : 
        print(i, end = ' ') # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력 
# -

# ## 정렬 문제 : 두 배열의 원소 교체
# - 두개의 배열 A 와 B를 가지고 있다. 두 배열은 N 개의 원소로 구성되어있으며, 배열의 원소는 모두 자연수이다.
# - 최대 K 번 바꿔치기 연산을 수행할 수 있는데, 바꿔치기 연산이란 배열  A 에 있는 원소 하나와 배열 B에 있는 원소하나를 골라서 두 원소를 서로 바꾸는 것을 말함
# - 최종목표는 배열 A의 모든 원소의 합이 최대가 되도록 하는 것이다.
#
#
# - N과 K , 그리고 배열 A와 B의 정보가 주어졌을 때, 최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최댓값을 출력 하시오
# - 입력 5 3 
#         12543
#         55665
# - 출력 26

# +
# %%time
# 내가 푼 것
n, k =  map(int, input().split())
a = list(map( int, input()))
b = list(map( int, input()))

while k > 0 :
    for i in range(n) :
        if a[i] == min(a) :
            min_idx = i

        if b[i] == max(b):
            max_idx = i

    a[min_idx] , b[max_idx] = b[max_idx] , a[min_idx] 
    k -= 1 
    
print(sum(a))

# 내코드랑 아래 코드랑 비교하면, 만약 b가 a 보다 다 작을 경우에 대해서는 허점이 생김
# -

# ### 동빈샘의 아이디어 : 먼저 정렬을 한 후에 , 비교하기

# +
# %%time
# 동빈샘이 푼것 
n, k = map(int, input().split())
a = list(map( int, input()))
b = list(map( int, input()))

a.sort() # 배열 a는 오름차순 정렬 수행
b.sort(reverse = True ) # 배열 b는 내림차순 정렬 수행

# 첫번째 인덱스부터 확인하며, 두 배열의 원소를 최대 k번 비교
for i in range(k):
    # a의 원소가 b의 원소보다 작은 경우
    if a[i] < b[i] :
        # 두 원소를 교체
        a[i], b[i] = b[i], a[i]
    else : # a의 원소가 b의 원소보다 크거나 같을때, 반복문 탈출
        break

print(sum(a))
# -


