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

# # 2. 구현 : 시뮬레이션과 완전탐색
# - 일반적으로 알고리즘 문제서의 2차원 공간은 행렬(Matrix)의 의미로 사용됨

for i in range(5):
    for j in range(5):
        print('(',1, ',' ,j,')', end = ' ' )
    print()

# - 시뮬레이션 및 완전탐색 문제에서는 2차원 공간에서의 방향 벡터가 자주 활용됨

# +
# 동 북 서 남  x는 행을 의미 , y 는 열을 의미 
dx = [0 , -1, 0 , 1]
dy = [ 1, 0, -1, 0 ]

# 현재 위치 
x, y = 2,2 

for i in range(4):
    # 다음 위치
    nx = x + dx[i]
    ny = y + dy[i]
    print(nx, ny)
# -

# ## 2.0.1 상하좌우 문제
# : A는 N X N 크기의 정사각형 공간 위에 있다. 이 공간은 1X1크기의 정사각형으로 나누어져 있다. 가장 왼쪽 좌표는 ( 1,1 ) 이며, 가장 오른쪽 좌표는 (N ,N )이다. A는 상하좌우 방향으로 이동할 수 있으며, 시작좌표는 항상 (1, 1)이다. 
#
# : A가 이동할 계획서에는 L, R, U , D중 하나의 문자가 반복적으로 적혀 있다. 
#
# L : 왼쪽 한칸,  R : 오른쪽한칸 , U : 위로 한칸, D: 아래로 한칸 
#
# :  N X N 크기의 정사각형 공간을 벗어나는 움직이는 무시됨 
#
# : 공간의 크기 = 5 , 입력 : 5   RRRUDD
#
# 출력 : 3 4 

# +
# 내가 푼 문제 
N = int(input())
move = input()
print(move)
x , y = 1,1 
    
for j in move:
    
    if j == 'R':
        if y < N:
            x += 0
            y += 1  
        
    elif j == 'L':
        if y > 1 :
            x += 0
            y += -1
            
    elif j == 'U':
        if x > 1 :
            x += -1
            y += 0
    elif j == 'D':
        if x < N :
            x += 1
            y += 0
    
print(x, y)
        

# +
# 동빈나샘 구현 코드

# N 입력 받기
n  = int(input())
x, y = 1,1 
plans = input().split()

# L , R, U, D에 따른 이동방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L','R','U','D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            print(nx, ny)
            
        # 공간을 벗어나는 경우 무시
        if nx < 1 or ny < 1 or nx > n or ny  >n :
            continue
            
        x, y = nx, ny
print(x, y)
# -

# ## 2.0.2. 시각 















# +
# H를 입력받기
h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)
# -



# +
  
# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)
# -



# +
# N, M을 공백을 기준으로 구분하여 입력받기
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
# 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

# 정답 출력
print(count)
# -


