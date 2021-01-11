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

# +
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수 및 간선의 개수를 입력 받기
n = int(input())
m = int(input())

# 2 차원 리스트(그래프 표현)을 만들고 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n + 1)]

# 자기자신에서 자기 자신으로 가는 비용을  0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b :
            graph[a][b] = 0
            
# 각 간선에 대한 정보를 입력 받아 , 그 값으로 초기화
for _ in range(m) :
    # a 에서 b로 가는 비용은 c라고 설정
    a, b, c = map(int, input().split())
    graph[a][b] = c
    
# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1 , n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
for a in range(1, n +1):
    for b in range(1 , n +1):
        # 도달할수 없는 경우, 무한으로 출력
        if graph[a][b] == INF:
            print('무한', end = ' ')
        # 도달할 수 있는 경우 거리를 출력
        else:
            print(graph[a][b], end = ' ')
    print()
