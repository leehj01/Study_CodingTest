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

# 전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
# 전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.
#
# 구조대 : 119
# 박준영 : 97 674 223
# 지영석 : 11 9552 4421
# 전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.
#
# 제한 사항
# phone_book의 길이는 1 이상 1,000,000 이하입니다.
# 각 전화번호의 길이는 1 이상 20 이하입니다.
# 같은 전화번호가 중복해서 들어있지 않습니다.

phone_book.sort()

phone_book

phone_book = ["123","456","789"]

'119' in '976711194223'[:3]

{'97674223'} - {'119'}


# ### 첫번째 시도 : 2중 FOR 문으로 구현한 코드 : 정확성 테스트는 100점이나 효율성에서 0점 맞음...^^

def solution(phone_book):
    for i in phone_book :
        for j in phone_book:
            if i == j[:len(i)] and i != j:
            return False
    return True


# ### 두번째 시도 : combinations으로 구현한 코드 : 정확성 테스트는 100점이나 효율성에서 0점 맞음...^^

from itertools import combinations
def solution(phone_book):
    for i in list(combinations(phone_book, 2)):
        if i[0][:len(min(i))] == i[1][:len(min(i))]:
            return False
    return True


# ### 세번째 시도 : one for문 - 성공

def solution(phone_book):
    phone_book.sort()  # 문자열이라서 순서대로 앞글자 순서대로 비교를 위해 sort 해줌 ( 예전 문자열 정렬에 배운 지식 )
    for i in range(len(phone_book)-1 ):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False
    return True


# ### 다른사람 코드

def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):                   # 괄호 안에 적은 문자열로 시작하는 지 확인하는 메소드  
                                                # p2.startswith(p1 ( 문자열 ) , 시작위치 , 끝나는 위치  )
            return False
    return True
