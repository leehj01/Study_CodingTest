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

# ## 순차 탐색

# +
# 순차 탐색 소스코드 구현
def sequential_search(n, target, array ):
    # 각 원소를 하나씩 확인
    for i in range(n):
        # 현재의 원소가 찾고자 하는 원소와 동일한 경우
        if array[i] == target:
            return i + 1 # 현재 위치반환 ( 인덱스는  0부터 시작하므로 1 더하기)
        
input_data = input().split()
n = int(input_data[0]) #  생성할 원소의 개수 
target = int(input_data[1]) # 찾고자 하는 숫자

array = list(map(int , input().split()))


# 순차탐색 결과 출력
print(sequential_search(n, target, array))


# -

# ## 이진탐색

# +
# 이진탐색 소스코드 구현 ( 재귀적 구현 )

def binary_search(array, target, start, end) :
    if start > end :  # 원소가 없다는 의미 
        return None 
    mid = (start + end) //2
    
    # 찾는 경우 중간점  인덱스 반환
    if array[mid] == target:
        return mid
    
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target :
        return binary_search(array, target, start, mid -1 )
    
    #중간점의 값보다 찾고자하는 값이 큰 경우 오른쪽확인
    elif array[mid] < target :
        return binary_search(array, target, mid +1 , end)
    
# n(원소의 개수)과 target(찾고자 하는 값)을 입력 받기
n, target = list(map(int, input().split())) # 10 7

#전체 원소 입력 받기
array = list(map(int, input().split())) # 1 3 5 7 9 11 13 15 17 19

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다")
    
else:
    print(result +1 )


# +
# 이진탐색 소스 코드 구현 ( 반복문 구현 )

def binary_search(array, target, start, end) :
    while start <= end:
        mid = (start + end) // 2
        
        # 찾은 경우 중간점 인덱스 반환
        if array[mid]  == target:
            return mid
        
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽확인 
        elif array[mid] > target:
            end = mid -1
        
        # 중간점의 값보다 찾고자하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid +1
    
    return None


n, target = 10 , 7
array = [1, 3 ,5 ,7 ,9 ,11 ,13 ,15 ,17 ,19]

# 이진탐색 수행 결과
result = binary_search(array, target , 0, n-1)
if result == None :
    print("원소가 존재하지 않습니다")
    
else:
    print(result +1 )  
# -

# ### 파이썬 이진탐색 라이브러리

# +
from bisect import bisect_left, bisect_right

a = [1,2, 4,4, 8]
x = 4

print(bisect_left(a,x ))
print(bisect_right( a,x ))
# -

# ### 값이 특정 범위에 속하는 데이터 개수 구하기

# +
from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value] 인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a , right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

# 배열 선언
a = [ 1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# 값이 4인 데이터 개수 출력
print(count_by_range(a ,4, 4))

# 값이 [ -1, 3] 범위에 있는 데이터 개수 출력
print(count_by_range(a , -1 , 3))
# -

# ## 빠르게 입력받기

# +
import sys

# 하나의 문자열 데이터 입력받기
input_data = sys.stdin.readline().rstrip()

# 입력받은 문자열 그래로 출력
print(input_data)
# -
# ## 트리의 순회 (Tree Traversal) 구현


# +
class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node
        
# 전위 순회(Preorder Traversal)
def pre_order(node):
    print(node.data, end= ' ')
    if node.left_node != None:
        pre_order(tree[node.left_node])
    if node.right_node != None:
        pre_order(tree[node.right_node])
        
# 중위 순회(Inorder Traversal)
def in_order(node):
    if node.left_node != None:
        in_order(tree[node.left_node])
    print(node.data, end = ' ')
    if node.right_node != None:
        in_order(tree[node.right_node])
        
# 후휘 순회(Postorder Traversal)
def post_order(node):
    if node.left_node != None:
        post_order(tree[node.left_node])
    if node.right_node != None:
        post_order(tree[node.right_node])
    print(node.data, end = ' ')
    
n = int(input())
tree = {}

for i in range(n):
    data, left_node, right_node = input().split()
    
    if left_node == 'None':
        left_node = None
    if right_node == 'None':
        right_node = None 
    tree[data] = Node(data, left_node, right_node)
    
pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])
# -


