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

# ## 처음 했던 방법 : 부분 리스트의 max 값 보다 작으면 없애기

def solution(number, k):
    num = [i for i in number]
    idx = 0
    
    if num[0] == '9':
        return(''.join(num[:len(num) - k]))

    for i in num.copy():
        if i < max(num[idx:idx+k+1]):
            k -= 1 
            num.remove(i)
        else : 
            idx += 1
            
    return ''.join(num)


solution(number, k)

# ## 세번째 방법 : 재귀함수 방법

number = '1924'
k = 2
num = list(number)
length = len(list(number)) - k


# +
def pop_now( num ):  # 뒤에보다 작은애는 없애는 함수 
    now = 0
    for i in range(len(num) -1 ):
        if num[i] < num[i+1]:
            num.pop(now)
            break
        else :
            now += 1 

def solution(number, k):
    num = list(number)
    length = len(list(number)) - k
    while True :

        pop_now( num )
        k -= 1

        if k == 0:
            break

    if len(num) != length  :
        num = num[:length]
             
    return ''.join(num)



# -

solution(number, k)


# ## 마지막 방법 : 스택 방법

def solution(number, k):
    
    stack = []
    length = len(list(number)) - k

    for i in number :
        while stack and stack[-1] < i and k > 0 :
            stack.pop()
            k -= 1
        stack.append(i)

    if k != 0 :
        stack = number[:length]

             
    return ''.join(stack)
