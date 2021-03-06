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

# H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다. 어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다. 위키백과1에 따르면, H-Index는 다음과 같이 구합니다.
#
# 어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.
#
# 어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# 과학자가 발표한 논문의 수는 1편 이상 1,000편 이하입니다.
# 논문별 인용 횟수는 0회 이상 10,000회 이하입니다.

citations = [3, 0, 6 , 1, 5]


def solution(citations):
    for h in range(len(citations), 0,-1) :
        if len([i for i in citations if i >= h ] ) >= h:
            return h
    return 0


# +
# 배우면 좋을 남코드  - map 을 이용 

def solution(citations):
    citations.sort(reverse=True)    # 큰수부터 
    answer = max(map(min, enumerate(citations, start=1))) 
    return answer


# +
# 위의 코드 설명 
citations = [12,11,10,9,8,1]
citations.sort(reverse=True)  
for i , v in enumerate(citations, start=1):
    print(i, v)
    
list(map(min, enumerate(citations, start=1)))
