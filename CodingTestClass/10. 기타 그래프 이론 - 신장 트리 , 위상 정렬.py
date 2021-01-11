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

# ## 크루스칼 알고리즘

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

# 모든 간선을 담을 리스트와, 최종 비용을 담을 변수
edges = []
result = 0 


# 부모 테이블 상에서 부모를 자기 자신으로 초기화
for i in range(1, v + 1 ):
    parent[i] = i
    
# 모든 간선에 대한 정보를 입력 받기
for _ in range(e) :
    a, b, cost = map(int, input().split())
    # 비용순으로 정렬하기 위해서 튜플의 첫번째 원소를 비용으로 설정
    edges.append((cost, a, b))
    
# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges :
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만, 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        
print(result)
# -

# ## 위상 정렬

# +
from collections import deque

# 노드의 개수와 간선의 개수를 입력받기
v, e = map(int, input().split())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * ( v +1)
# 각 노드에 연결된 간선정보를 담기위한 연결 리스트 초기화
graph = [[] for i in range(v +1)]

#  방향 그래프와 모든 간선 정보를 입력 받기
for _ in range(e) :
    a, b = map(int, input().split())
    graph[a].append(b) # 점점 a 에서 b로 이동가능 
    # 진입차수를 1 증가
    indegree[b] += 1
    
    
# 위상 정렬 함수
def topology_sort():
    result = [] # 알고리즘 수행 결과를 담을 리스트
    q = deque() # 큐 기능을 위한 deque 라이브러리 사용
    # 처음 시작할 떄는 진입차수가  0 인 노드를 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0 :
            q.append(i)
            
    # 큐가 빌때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0 이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
    
    # 위상 정렬을 수행한 결과 출력
    for i in result:
        print(i, end = ' ')

topology_sort()
