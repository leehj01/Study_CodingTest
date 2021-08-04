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

# 수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.
#
# 마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
# completion의 길이는 participant의 길이보다 1 작습니다.
# 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
# 참가자 중에는 동명이인이 있을 수 있습니다.

participant = ['mislav', 'stanko', 'mislav','ana']
completion = ['stanko', 'ana','mislav']

from collections import Counter
def solution(participant, completion):
    return ''.join(list((Counter(participant) - Counter(completion)).keys()))


# +
# 배울만한 코드 : hash 사용  -> hash 값 충돌이 발생할 가능성이 있다. 

def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part  # dic[] 안에 hash를 넣어주면, part에 해당하는 해쉬값이 주어짐. 
        temp += int(hash(part))  # 그 값은 고유한 값이기 때문에, 가감을 해주면서 answer을 찾아줌 
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer
