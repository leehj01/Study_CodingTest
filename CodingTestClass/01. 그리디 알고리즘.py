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

# ## 거스름돈 문제

# +
n = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인
array = [500 ,100 , 50, 10 ]

for coin in array :
    count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin 

print(count)
# -

# ## 1. 1이 될때까지
# - 어떠한 수 n이 1이 될때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 합니다. 단, 두번째 연산은 n 이 k로 나누어 떨어질 때만 선택할 수 있다.
# 1. n에서 1을 뺀다
# 2. n을 k로 나눈다
#
# - n이 1이 될때까지 1, 2 번의 과정을 수행해야하는 횟수의 최솟값을 출력
#
# 입력 : 25 5
# 출력 2

# +
# 내가 짠 코드
n , k = map(int, input().split(" "))

count = 0

while n > 1:
    
    if n % 5 == 0:
        n = int(n // 5)
        count += 1
        
    else :
        n = n - 1
        count += 1
        
print(count)

# +
# 동빈나 샘의 코드 
# 로그 시간복잡도의 코드가 되기때문에, 굉장히 빨라짐 

n, k = map(int, input().split())

result = 0

while True :
    # n이 k로 나누어 떨어지는 수가 될때까지 배기 
    target = (n//k) * k 
    result += (n - target)
    n = target
    
    # n 이 k보다 작을 떄 반복문 탈출
    if n < k :
        break
        
    result += 1
    n //= k
    
# 마지막으로 남은 수에서 1씩 뺴기
result += (n - 1 )
print(result)
# -

# ## 2. 곱하기 혹은 더하기
# - 각 자리가 숫자 (0 부터 9)로만 이루어진 문자열 s가 주어졌을 때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 'x'혹은 '+'연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰수를 구하는 프로그램을 작성하세요. 단 , 모든 연산은 왼쪽에서부터 순서대로 이루어진다고 가정
#
#
# - 첫째 줄에 만들어 질 수 있는 가장 큰 수를 출력합니다
#
# - 입력 1 : 02984  출력 1 : 576
# - 입력 2 : 567    출력 2 : 210
#

# +
# 내가 푼 코드 -> 정답은 맞췄지만,, 틀린 코드였다.. ㅠㅠ 
# 리스트로 만들 필요가 없으며, 1 도 생각해줘야한다.

for i in range(2):
    s = list(map(int, input()))
    result = 1
    
    if {0} in s:
        s.remove(0)
        
    for j in s:
        result *= j 
        
    print(result)

# +
# 다시 풀어보자

for i in range(2) :
    s = list(map(int, input()))
    
    result = s[0]
    
    for j in range(1, len(s)):
        if s[j] < 2 or result < 2 :
            result += s[j]
        else:
            result *= s[j]
            
    print(result)

# +
# 동빈썜 코드

data = input()

# 첫번째 문자를 숫자로 변경하여 대입
result = int(data[0])
print(result)

for i in range(1, len(data)):
    # 두 수중에서 하나라도 0 혹은 1인 경우, 곱하기보다 더하기 수행
    num = int(data[i])
    if num <= 1 or result <=1 :
        result += num
    else:
        result *= num
        
print(result)
# -

# ## 3. 모험가 길드
# - 모험가가 n명 있다. 모험가 길드에서 n명의 모험가를 대상으로 '공포도'를 측정했는데, '공포도'가 높은 모험가는 쉽게 공포를 느껴 위험상황에서의 대처 능력이 떨어진다. 
# - 모험가 그룹을 안전하게 구성하고자 공포도가 x인 모험가는 반드시 x명이상으로 구성한 모험가 그룹에 참여해야 여행을 떠날수 있도록 규정했다
# - 최대 몇개의 모험가 그룹을 만들수 있는가 ? 여행을 떠날 수 있는 **그룹 수의 최댓값**을 구하는 프로그램을 작성해라
#
#
# - 입력 : 5  , 23122
# - 출력 : 2 

# +
# %%time
# 내가 한 코드  - 그룹의 최댓값을 구하라고 했는데.. 난 최솟값을 구함.ㅠㅠ

n = int(input())
g = list(map(int , input()))

g_sorted = sorted(g)
group = 0

for i in g_sorted:
    if i <= n :
        n = n - i
        del g_sorted[0:i]
        group += 1

print(group)


# +
# n = int(input())
# g = list(map(int , input()))

n = 7
g = [4,1,1,1,1,2,2]

g_sorted = sorted(g, reverse=False)
group = 0


for i in g_sorted:
    print(i)
    if n >= i :
        n -= i
        print('n', n)
        del g_sorted[0:i]
        print(g_sorted, '\n')
        group += 1

print(group)

# +
# %%time
## 동빈샘이 한것

n = int(input())
data = list(map(int, input()))
data.sort()

result = 0 # 총그룹수
count = 0  # 현재 그룹에 포함된 모험가의 수

for i in data : # 공포도가 낮은것부터 하나씩 확인
    count += 1  # 현재 그룹에 해당 모험가를 포함시키기
    if count >= i : # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹결성
        result += 1 # 총그룹의 수 증가시키기
        count = 0  # 현재 그룹에 포함된 모험가의 수 초기화
print(result)
# -


