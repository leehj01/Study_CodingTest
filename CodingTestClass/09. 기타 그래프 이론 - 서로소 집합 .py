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

# ## 서로소 집합 : 기본적인 구현 방법 

# +
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        return find_parent(parent , parent[x])
    return x

# 두 원소가 속한 집합을 합치기 
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
# 노드의 개수와 간선 (union 연산)의 개수 입력 받기
v,e = map(int, input().split())
parent = [0] * ( v + 1) # 부모 테이블을 초기화

# 부모 테이블 상에서 부모를 자기 자신으로 초기화
for i in range(1, v + 1 ):
    parent[i] = i
    
# union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력하기
print('각 원소가 속한 집합 : ', end = '')
for i in range(1, v +1):
    print(find_parent(parent, i), end = ' ' )

print()

# 부모 테이블 내용 출력하기, 집합에 대한 정보는 아님 
print('부모 테이블 : ', end = '')
for i in range( 1, v +1):
    print(parent[i], end = ' ')


# -

# ## 서로소 집합 자료구조 : 경로 압축

# 특정 원소가 속한 집합을 찾기
def find_parent(parent , x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# +
## 전체 코드

# 특정 원소가 속한 집합을 찾기
def find_parent(parent , x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기 
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
# 노드의 개수와 간선 (union 연산)의 개수 입력 받기
v,e = map(int, input().split())
parent = [0] * ( v + 1) # 부모 테이블을 초기화

# 부모 테이블 상에서 부모를 자기 자신으로 초기화
for i in range(1, v + 1 ):
    parent[i] = i
    
# union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력하기
print('각 원소가 속한 집합 : ', end = '')
for i in range(1, v +1):
    print(find_parent(parent, i), end = ' ' )

print()

# 부모 테이블 내용 출력하기, 집합에 대한 정보는 아님 
print('부모 테이블 : ', end = '')
for i in range( 1, v +1):
    print(parent[i], end = ' ')


# -

# ## 서로소 집합을 활용한 사이클 판별

# +
## 전체 코드

# 특정 원소가 속한 집합을 찾기 - 경로 압축 기법
def find_parent(parent , x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기 
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
# 노드의 개수와 간선 (union 연산)의 개수 입력 받기
v,e = map(int, input().split())
parent = [0] * ( v + 1) # 부모 테이블을 초기화

# 부모 테이블 상에서 부모를 자기 자신으로 초기화
for i in range(1, v + 1 ):
    parent[i] = i
    
cycle = False # 사이클 발생 여부
    
# union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    # 사이클이 발생한 경우 종료
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    # 사이클이 발생하지 않았다면 합집합 연산 수행
    else:
        union_parent(parent, a, b)

if cycle:
    print('사이클이발생했습니다')
else:
    print('사이클이 발생하지 않았습니다')
        
# 각 원소가 속한 집합 출력하기
print('각 원소가 속한 집합 : ', end = '')
for i in range(1, v +1):
    print(find_parent(parent, i), end = ' ' )

print()

# 부모 테이블 내용 출력하기, 집합에 대한 정보는 아님 
print('부모 테이블 : ', end = '')
for i in range( 1, v +1):
    print(parent[i], end = ' ')
