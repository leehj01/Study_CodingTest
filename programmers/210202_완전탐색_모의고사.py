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

# 문제 설명
# 수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.
#
# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...
#
# 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.
#
# 제한 조건

# +
def solution(answers):
    one = [ i for i in range(1,6)] * (10000//5)
    two = [ 2, 1, 2, 3, 2, 4, 2, 5 ] * (10000//8 )
    tree = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (10000//10)
    r_cnt = [0,0,0]

    for i in range(len(answers)):
        if answers[i] == one[i]:
            r_cnt[0] += 1 
        if answers[i] == two[i]:
            r_cnt[1] += 1
        if answers[i] == tree[i]:
            r_cnt[2] += 1

    if len([i for i,j in enumerate(r_cnt) if j == max(r_cnt)]) != 1 :
        return(sorted([i+1 for i,j in enumerate(r_cnt) if j == max(r_cnt)]))
    else:
        return([r_cnt.index(max(r_cnt)) + 1])

answers = [1,3,2,4,2]
# answers = [1,2,3,4,5]
solution(answers)
