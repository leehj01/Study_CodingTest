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

# ## 인접 행렬 방식 예제

# +
INF = 999999999 # 무한의 비용 선언

# 2차원 리스트를 이용해 인접 행렬 표현
graph = [
    [0, 7, 5],
    [9, 0, INF],
    [5, INF, 0]
]

print(graph)
# -

# ## 인접 리스트 방식 예제

# +
# 행(row) 이 3개인 2차원 리스트로 인접 리스트 표현
graph = [[] for _ in range(3)]

# 노드 0에 연결된 노드 정보 저장 (노드, 거리)
graph[0].append((1, 7))
graph[0].append((2, 5))

# 노드 1에 연결된 노드 정보 저장 (노드, 거리)
graph[1].append((0,7))

# 노드 2에 연결된 노드 정보 저장 (노드, 거리)
graph[2].append((0, 5))

print(graph)


# -

# ## DFS 예제

# +
# DFS 메서드 정의

def dfs(graph, v, visited) : # 그래프의 정보, 방문처리 
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end = ' ') # 방문했으면, 해당 노드를 출력 
    
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:  # 인접한 노드가 방문되지 않은 상태라면, 
            dfs(graph, i , visited) # 재귀함수를 이용해 방문을 함.
            

# 각 노드가 연결된 정보를 표현 ( 2차원 리스트 )
graph = [
    [], # 일반적으로 그래프 문제의 노드의 번호가 1번부터 시작하는 경우가 많아, 인덱스 0 은 비워둠
    [2, 3, 8], # 1번 노드와 연결되어있는  2, 3 , 8 로 리스트 초기화
    [1, 7],  # 2 번 노드와 연결됨 
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2,6,8],
    [1,7]
]  # 인접리스트로 표현 

# 각 노드가 방문된 정보를 표현 ( 1 차원 리스트 )
visited = [False] * 9  # 기본적으로 모든값은 false 로 초기화해서, 모든 노드를 하나도 방문하지 않는 것으로 할수 있음
# 1번 노드부터 8 번노드를 가지고 있고, 인덱스 0은 사용하지 않기 위해, 9로 설정 


# 정의된 DFS 함수 호출
dfs(graph, 1, visited )
# -

# ## BFS 예제 

# +
from collections import deque

# BFS 메서드 정의

def bfs(graph, start, visited):
    
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    
    # 현재 노드를 방문 처리
    visited[start] = True
    
    # 큐가 빌때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력하기
        v = queue.popleft()
        print(v, end = ' ')
        
        # 아직 방문하지 안은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                
# 각 노드가 연결된 정보를 표현 ( 2차원 리스트 )
graph = [
    [],
    [ 2, 3, 8],
    [1,7 ],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 표현 ( 1차원 리스트 )
visited = [False] * 9

# 정의된 BFS 함수 호출
bfs ( graph, 1, visited ) # 1 2 3 8 7 4 5 6 
# graph 와  시작노드 1 이라는 뜻. 
# -

# ### 실전문제 : 음료수 얼려먹기
# - N X M 크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다. 구명이 뚫려 있는 부분끼리 상,하, 좌,우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주됨. 
# - 얼음틀의 모양이 주어졌을 때, 생성되는 총 아이스크림 개수를 구하는 프로그램을 작성하세요.
#
#
# - 첫번째 줄에 얼음틀의 세로 길이 N과 가로길이 M 가 주어짐
# - 두번째 부터 N + 1 번째 줄까지 얼음 틀의 형태가 주어짐
# - 구멍이 뚫려있으면 0 , 아니면 1 
#
#
# - 입력 
#    4 5 
#    00110
#    00011
#    11111
#    00000
#    
# - 출력 : 3

# +
# 동빈나샘 코드 

# n, m 을 공백으로 구분하여 입력 받기
n , m = map(int, input().split())

# 2차원 리스트의 맵 정보 받기 
graph = []
for i in range(n):
    graph.append(list(map(int,input())))


# dfs로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문 
def dfs(x, y):
    
    # 주어진 범위를 벗어나는 경우 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    
    # 현재 노드를 아직 방문 안했다먄
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1  # 이렇게 1로 처리함.
            
        # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True 
    
    return False 

# 모든 노드(위치)에 대하여 음료수 채우기 
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i,j) == True : 
            result += 1 
            
print(result)


# -

# ## 미로탈출 문제
# - n x m 크기의 직사각형 형태의 미로에 갇혔따. 미로에는 여러 마리의 괴물이 있어 이를 피해 탈출 해야한다. 
# - 시작 위치는 (1,1)이며 , 미로의 출구는 (N,M)의 위치에 존재하며 한번에 한칸씩 이동할 수있다. 이떄 괴물이 있는 부분은 0, 괴물이 없는 부분은 1로 표시되어있다. 미로는 반드시 탈출할 수 있는 형태로 제시된다.
# - 이때, 탈출하기위해 움직어야하는 최소 칸의개수를 구하시오. 칸을 셀때는 시작칸과 마지막 칸 모두 포함해서 계산한다. 
#
#
# - 입력 : 5 6
#     101010
#     111111
#     000001
#     111111
#     111111
#     
# - 출력 : 10

# +
# 동빈나 샘 코드 ...ㅠㅠ 나는 실패.. 으악

def bfs(x , y):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x,y))
    print(queue)
    
    # 큐가 빌 때까지 반복하기
    while queue :
        x, y  = queue.popleft()
        print( x, y)
        
        # 현재 위치에서 4가지 방향으로의 위치 찾기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 미로찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny< 0 or ny >= m:
                continue 
                
            # 벽인 경우 무시
            if graph[nx][ny] == 0 :
                continue
                
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1 
                queue.append((nx, ny ))
    
    print(graph[n-1][m -1])
    # 가장 오른 쪽까지의 최단 거리 반환 
    return graph[n -1 ][m -1]


from collections import deque

n , m = map(int, input().split())

# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))

graph = [[1, 0, 1, 0, 1, 0], [1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1,1], [1, 1, 1, 1, 1, 1]]
print(graph)
# 이동할 4가지 방향 정의 ( 상, 하, 좌, 우)
dx = [ -1, 1, 0 , 0]
dy = [0, 0, -1, 1]

# bfs를 수행한 결과 출력
print(bfs(0,0))
# -


