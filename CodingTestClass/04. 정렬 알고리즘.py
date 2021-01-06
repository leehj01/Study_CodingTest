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


