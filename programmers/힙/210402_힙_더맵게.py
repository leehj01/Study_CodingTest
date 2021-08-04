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

# +
import heapq

def solution(scoville, k):
    heapq.heapify(scoville) # 기존 리스트를 힙으로 만들기 
    i = 0
    while scoville[0] < k:
        if len(scoville) > 1:
            # heappuch(추가할 대상, 추가할 원소 )
            heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville) * 2))
            i += 1
        else:
            return -1
    return i
