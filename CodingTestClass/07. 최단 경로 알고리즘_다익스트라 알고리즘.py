# 다익스트라 알고리즘 : 간단한 구현 방법
import sys
input = sys.stdin.readline
INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정


# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())

# 시작 노드 번호를 입력 받기
start = int(input())

# 각 노드에 연결되어있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n + 1)]

# 방문한 적 있는지 체크하는 목적의 리스트 만들기
visited = [False] * (n + 1)

# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())

    # a 번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))


# 방문하지 않은 노드 중에서 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0  # 가장 최단 거리가 짧은 노드 (인덱스)
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    # 시작노드에서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]

    # 시작 노드를 제외한 전체 n-1 개의 노드에 대해서 반복
    for i in range(n - 1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서 방문처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost


# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달 할 수 없는경우, 무한이라고 출력
    if distance[i] == INF:
        print("무한")

    # 도달 할 수 있는 경우 거리를 출력
    else:
        print(distance[i])

#%%
# 힙 알고리즘
import sys
import heapq
input = sys.stdin.readline

def heapsort(iterable):  # 기본적으로 minheap 형태임
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in interable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

res = heapsort(arr)

for i in range(n):
    print(res[i])

## 최단거리 자료구조 : 힙 라이브러리 - 최소 힙 ( 오른차순 정렬 )

import heapq


# 오름차순 힙 정렬 ( Heap sort)
def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)

    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result


result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# ## 최단거리 자료구조 : 힙 라이브러리 - 최대 힙 ( 내림차순 정렬 )
import heapq


# 내림차순 힙 정렬
def heapsort(iterable):
    h = []
    result = []

    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)

    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result


result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)
#%%

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)  # 무한을 의미하는 갓으로 10억 설정

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())

# 시작 노드 번호를 입력 받기
start = int(input())

# 각 노드에 연결되어있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n + 1)]

# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력 받기
for _ in range(m):
    a, b, c = map(int, input().split())

    # a 번 노드에서 b번 노드로 가는 비용이 c 라는 의미
    graph[a].append((b, c))


def dijkstra(start):
    q = []

    # 시작노드로 가기위한 최단 겨올는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:  # 큐가 비어있지 않다면

        # 가장 최단 거리가 짧은 노드에 대한 정보  꺼내기
        dist, now = heapq.heappop(q)

        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달 할 수 없는 경우, 무한이라고 출력
    if distance[i] == INF:
        print('무한')
    # 도달 할 수있는 경우 거리를 출력
    else:
        print(distance[i])
