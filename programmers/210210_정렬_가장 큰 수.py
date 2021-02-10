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
numbers : [0, 5, 10, 15, 20]
return : 52015100

numbers : [1000, 0, 5, 99, 100]
return : 99510010000

numbers : [0, 0, 0, 0, 0]
return : 0

# -

numbers = [1000, 0, 5, 99, 100]


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
#     answer = ''.join(numbers)
    return numbers

numbers =  [3, 5, 8, 9, 300, 304, 33, 30, 34]
numbers = list(map(str, numbers))
numbers[0].sort()

# +
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start > end : # 원소가 1개인 경우 종료
        return
    
    pivot = start # 피벗은 첫번째 원소
    left = start + 1
    right = end
    while left <= right :
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1 
            
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
            
        if left > right : # 엇갈렸다면 작은 right -=1 데이터와 피벗을 교채
            array[right], array[pivot] = array[pivot], array[right]
            
        else : # 엇갈리지 않았다면 작은 데이터와 큰데이터 교체
            array[left], array[right] = array[right] , array[left]
            
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right -1 )
    quick_sort(array, right +1 , end )
    
            
quick_sort(array, 0, len(array) -1 )
print(array)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -

numbers =  [3, 5, 8, 9, 300, 304, 33, 30, 34,333]
# numbers.sort(reverse = True)

# +
numbers =  [3, 5, 8, 9, 300, 304, 33, 30, 34,333]


quick_sort(numbers, 0, len(numbers) -1 )
print(numbers)

# +
numbers =  [3, 5, 8, 9, 300, 304, 33, 30, 34,333]
numbers = list(map(str, numbers))

for i in range(1, len(numbers)):
    for j in range(i, 0 , -1):
        

# +
numbers =  [3, 5, 8, 9, 300, 304, 33, 30, 34,333]
numbers = list(map(str, numbers))

for i in range(1, len(numbers)):
    for j in range(i, 0 , -1):
        if numbers[j][0] < numbers[j-1][0]:
            numbers[j] , numbers[j-1] = numbers[j-1] , numbers[j]
            
        elif len(numbers[j]) >= 2 :
            if numbers[j][1] < numbers[j-1][1]:
                numbers[j] , numbers[j-1] = numbers[j-1] , numbers[j]
            
            
        else:
            print(numbers)

# +
numbers =  [3, 5, 8, 9, 300, 304, 33, 30, 34,333]
numbers = list(map(str, numbers))

for i in range(1, len(numbers)):
    for j in range(1, i):
        if numbers[j][0] < numbers[j-1][0]:
            numbers[j] , numbers[j-1] = numbers[j-1] , numbers[j]
            
        elif len(numbers[j]) >= 2 :
            if numbers[j][1] < numbers[j-1][1]:
                numbers[j] , numbers[j-1] = numbers[j-1] , numbers[j]
            
            
        else:
            print(numbers)
# -


