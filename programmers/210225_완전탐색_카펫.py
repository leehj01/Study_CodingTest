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
# Leo는 카펫을 사러 갔다가 아래 그림과 같이 중앙에는 노란색으로 칠해져 있고 테두리 1줄은 갈색으로 칠해져 있는 격자 모양 카펫을 봤습니다.
#
# carpet.png
#
# Leo는 집으로 돌아와서 아까 본 카펫의 노란색과 갈색으로 색칠된 격자의 개수는 기억했지만, 전체 카펫의 크기는 기억하지 못했습니다.
#
# Leo가 본 카펫에서 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로 주어질 때 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# 갈색 격자의 수 brown은 8 이상 5,000 이하인 자연수입니다.
# 노란색 격자의 수 yellow는 1 이상 2,000,000 이하인 자연수입니다.
# 카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 깁니다.

brown = 24
yellow = 24

import math
def solution(brown, yellow):
    y_ver = ([ i for i in range(1, int(math.sqrt(yellow))+1) if yellow % i == 0]) # 세로
    y_ho = [int(yellow/i) for i in y_ver ] # 가로

    for j in zip(y_ho, y_ver):
        if (j[0] + j[1])*2 + 4 == brown:
            return(list(map(lambda x : x+2 , j)))


# +
# 남이 푼 코드

import math
def solution(brown, yellow):
    ans=((brown-4)+math.sqrt((brown-4)**2-16*yellow))//4  # 근의 공식이..? 라고 함... 
    return [ans+2,yellow//ans+2]
