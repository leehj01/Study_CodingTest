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

# 0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
#
# 예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.
#
# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.
#
# 제한 사항
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.

# +
def solution(numbers):
    numbers = list(map(str, numbers))

    for i in range(1, len(numbers)):
        for j in range(i, 0 , -1):
            if numbers[j][0] < numbers[j-1][0]:
                numbers[j] , numbers[j-1] = numbers[j-1] , numbers[j]

            elif numbers[j][0] == numbers[j-1][0] and len(numbers[j]) == len(numbers[j-1]):
                if numbers[j][1] < numbers[j-1][1]:
                    numbers[j] , numbers[j-1] = numbers[j-1] , numbers[j]

                elif numbers[j][1] == numbers[j-1][1] and len(numbers[j]) == len(numbers[j-1]):
                    if numbers[j][2] < numbers[j-1][2]:
                        numbers[j] , numbers[j-1] = numbers[j-1] , numbers[j]


            elif numbers[j][0] == numbers[j-1][0] and len(numbers[j]) != len(numbers[j-1]) and int(numbers[j]) % 10 == 0:
                numbers[j] , numbers[j-1] = numbers[j-1] , numbers[j]
                
    numbers = [ i for i in numbers[::-1]]
    answer = ''.join(numbers)
    return answer

numbers =  [3, 30, 34, 5, 9]
solution(numbers)


# +
# 풀었으나 내것이 아닌 코드 .. 
# 1. 아이디어 : 문자형 sort는 int형 sort와 다르게 작동한다.
# 2. 아이디어 :  문자의 길이를 곱한다음 비교하면 더 간단하게 비교할 수 있다. 

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x : (x*4)[:4], reverse = True)
    answer = ''.join(numbers)
    answer = str(int(answer))
    return answer

numbers =  [3, 30, 34, 5, 9]
solution(numbers)

# +
# 공부해볼 코드

import functools  # from functools import cmp_to_key

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator), reverse=True)
    answer = str(int(''.join(n)))
    return answer



# -


numbers =  [3, 30, 34, 5, 9]
solution(numbers)
