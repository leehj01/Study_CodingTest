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
plans = input()

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
#             print(nx, ny)
            
            # 공간을 벗어나는 경우 무시
            if nx < 1 or ny < 1 or nx > n or ny  >n :
                continue

            x, y = nx, ny
print(x, y)

# +
n = int(input())
plans = "RRRUDD"

x,y = 1,1
dx = [0,0,-1,1]
dy = [-1,1,0,0]
pointer = ["L","R","U","D"]

for plan in plans:
    for t in range(len(pointer)):
        if plan == pointer[t]:
            nx = x + dx[t]
            ny = y + dy[t]
            print(f"{pointer[t]}\nnewx : {nx}\nnewy : {ny}")
            
            if nx < 1 or ny < 1 or nx > n or ny > n:
                print("pass",end = "—\n")
                continue
            print('move',end = "—\n")
            
            x,y = nx,ny
print(x,y)
# -

# ## 2.0.2. 시각 
# - 완전탐색 문제
# - 정수 N 이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하세요 .
# - 00시 00분 00초 부터 N시 59분 59초까지의 모든 시각중에서 3이 하나라도 포함되는 경우의 수를 출력 
# +
# 내가 푼 코드
N = int(input())

count = 0

m = 45 * 14 + 14*60
print(m)
nm = 0


for i in range(N+1):
    print(i)
    if i != 3 or i != 13 or i != 23 :
        nm += m
        
    else :
        nm = nm*60*60
    
    print(nm)
    
# - > 정말정말 별루인 코드 ㅠㅠㅠ 

# +
# 동빈나 샘 푼것 

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
# ## 2.1. 왕실의 나이트
# - 행복 왕국의 왕실 정원은 체스판과 같은 8 x 8좌표 평면 이다. 
# - 나이트가이동할 때는 L자 형태로만 이동할 수 있으며, 정원을 나갈 수 없다.
# - 이동할 수 있는 경우 : 수평으로 2칸 이동한 후, 수직으로 한칸 이동 / 수직으로 2칸 이동한 뒤 수평으로 한칸 이동 
#
# - 8 X 8 좌표 평면상에서 나이트의 위치가 주어졌을 때, 나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램을 작성하세요. 왕실의 정원에서 행의 위치를 표현할 때는 1부터 8로 표현하며, 열위치를 표현할 때는 a 부터 h 로 표현함 
#
# - 입력 : a1 
# - 출력 : 2

# +
# 내가 푼 코드 

col , row  = input()
row = int(row)
# print(row)
count = 0
movex = [ 1, -1, 1, -1 , 2 , 2 , -2, -2 ]
movey = [ 2, 2,  -2, -2, -1, 1, 1, -1 ]
name_y = { 'a': 1, 'b':2 ,'c':3,'d':4 ,'e':5,'f':6,'g':7,'h':8 }

for i in range(len(movex)):
    nrow = row + movex[i]
    ncol = name_y[col] + movey[i]
    
    if nrow < 1 or nrow > 8 or ncol < 1 or ncol > 8 :
        continue

    count += 1
    
    
print(count)


# +
# 동빈나 샘이 푼 코드

# 현재 나이트 위치 입력 받기
input_data = input()
row = int(input_data[1])
col = int(ord(input_data[0])) - int(ord('a')) +1   # 아스키 코드로 변환

# 나이트가 이동할 수 있는 8가지 방향 정의 - 2 차원 백터로도 사용 가능 
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps :
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_col = col + step[1]
    
    # 해당 위치로 이동이 가능하다면 카운트 증가 
    if next_row >= 1 and next_row <=8 and next_col >= 1 and next_col <= 8:
        result += 1
        
print(result)
# -

# ## 2.2. 문자열 재정렬 문제 
# - 알파벳 대문자와 숫자(0~9) 로만 구성된 문자열이 입력으로 주어집니다. 이때, 모든 알파벳을 오름차순을 정렬하여 이어서 출력한뒤, 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다. 
#
#
#
# - 입력 1 : K1KA5CB7   
# - 출력 1 : ABCKK13
#
#
# - 입력 2 : AJKDLSI412K4JSJ9D
# - 출력 2 : ADDIJJJKKLSS20

# +
# 내가 짠 코드
input_data = list(map ( str, input()) )

input_data.sort()


num = 0 
char_list = []
for i in input_data:
    try :
        num += int(i)
    except:
        char_list.append(i)
        pass
    
# 숫자가 하나더라도 존재하는 경우 가장 뒤에 삽입
if num != 0:
    char_list.append(str(num))
        
# 최종 결과 출력 ( 리스트를 문자열로 변환하여 출력 )
print(''.join(char_list))  


# +
# 동빈썜 코드

data = input()
result = []
value = 0

# 문자를 하나씩 확인하며
for x in data :
    # 알파펫인 경우 결과 리스트에 삽입 
    if x.isalpah():
        result.append()
        
    # 숫자는 따로 더하기
    else :
        value += int(x)
        
# 알파벳을 오름차순으로 정렬
result.sort()

# 숫자가 하나더라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    result.append(str(value))
    
# 최종 결과 출력 ( 리스트를 문자열로 변환하여 출력 )
print(''.join(result))
# -

# ## 2.3. 게임 개발 


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


