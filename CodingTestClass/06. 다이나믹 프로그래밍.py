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

# ## 다이나믹 프로그래밍
# ### 피보나치 수열 : 단순 재귀 소스 코드  

# +
# 피보나치 함수를 재귀함수로 구현
def fibo(x):
    if x == 1 or x ==2 : # 재귀함수이기 때문에, 종료조건을 만듦
        return 1
    return fibo(x - 1) + fibo(x -2)

print(fibo(4))
# -

# ### 피보나치 수열 : 다이나믹 프로그래밍 - 메모이제이션(재귀함수 사용) 소스 코드 

# +
# 한번 계산된 결과를 메모이제이션하기 위한 리스트 초기화
d = [0] * 100 # 100을 한 이유는 아래서 fibo(99) 를 구하고 싶기 때문 

# 피보나치 함수를 재귀함수로 구현 ( 탑다운 다이나믹 프로그래밍 )
def fibo(x):
    # 종료조건 ( 1 혹은 2 일때 1을 반환 )
    if x == 1 or x == 2:
        return 1
    
    #이미 계산한 적 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]
    
    # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    d[x] = fibo(x -1) + fibo(x -2)
    
    return d[x]

print(fibo(99)) # 218922995834555169026
# -

# ### 피보나치 수열 : 보텀업 다이나믹 프로그래밍 소스 코드 

# +
# 앞서 계산된 결과를 저장하기 위한 dp 테이블 초기화
d = [0] * 100

# 첫번째 피보나치 수와 두번째피보나치 수는 1
d[1] = 1
d[2] = 1
n = 99

# 피보나치 함수 반복문으로 구현 ( 보텀업 다이나믹 프로그래밍 )
for i in range(3, n+1 ):
    d[i] = d[i-1] + d[i - 2]
    
print(d[n]) # 218922995834555169026
# -


