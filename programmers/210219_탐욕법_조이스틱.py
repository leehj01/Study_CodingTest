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

name = 'BBBAAAB'


# +
# 내코드 54.5 정확도 

def solution(name):
    cnt = 0
    
    for i in range(len(name) ):
        if name[i] < 'N':
            cnt += (ord(name[i]) - ord('A'))

        elif name[i] >= 'N':
            cnt += (ord('Z') - ord(name[i])) + 1 

    if name[-2] == 'A' :
        cnt += 1
    else :
        cnt += len(name) -1 
    return cnt

solution(name)


# +
# 남의 코드 1 -  그러나 코드상 문제가 있다.

def solution(name):
    m = [ min(ord(c) - ord('A'), ord('Z')-ord(c) + 1) for c in name ]
    cnt = 0
    loca = 0  # location

    while True :
        cnt += m[loca]
        m[loca] = 0
        if sum(m) == 0 :
            return cnt

        left, right = -1 , 1

        while m[loca + left] == 0:
            left -= 1

        while m[loca + right] == 0:
            right += 1

        # 위치 조정
        cnt += -left if -left  < right else right 
        loca += left if -left < right else right

solution(name)


# +
# 남의 코드 2. - 내가 처음 생각했던 방법이었지만... 끝까지 구현하지 못했다.. 

def solution(st):
    res = 0 
    A_Count =0 
    A_Max = 0 # 가장 긴 A묶음의 A 수 
    A_StartIndex = 0 
    A_EndIndex = 0 
    vertical_count = 0 
    start = True 
    
    for i,v in enumerate(st): # 연속해서 나온 A 횟수 검사 
        if v == 'A' and start == False : 
            A_Count += 1 
            if A_Count > A_Max: 
                A_Max = A_Count 
                A_EndIndex = i        
        else: 
            A_Count = 0 
                
        # 알파벳이 N보다 크면 위로넘기는게 빠르다 
        if ord(v) > ord('N'): 
            count = ord('Z')-ord(v)+1 
        else: 
            count = ord(v) - ord('A')    
        res += count 
        start = False 
        
        
    # 가장 긴 A묶음의 인덱스 
    A_StartIndex = A_EndIndex - A_Max + 1 
    
    # A가 시작이나 끝에있어서 안움직여도 되는경우 
    if A_StartIndex ==0 or A_EndIndex == len(st)-1:
        res = res + len(st)-1 
        res -= A_Max # 이동안해도 되는 A만큼 빼준다. 
         
    # A묶음이 중간에있는경우 예) AZAAAZ 
    else: 
        if A_StartIndex <= (len(st)-A_EndIndex-1): 
            vertical_count = (A_StartIndex-1)*2 + (len(st)-A_EndIndex-1) 
        else: 
            vertical_count = (A_StartIndex-1) + (len(st)-A_EndIndex-1)*2 
            
        res +=min(vertical_count, len(st)-1) 
        
    return res

solution(name)
# -


