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

# ### 문제 설명
# 점심시간에 도둑이 들어, 일부 학생이 체육복을 도난당했습니다. 다행히 여벌 체육복이 있는 학생이 이들에게 체육복을 빌려주려 합니다. 학생들의 번호는 체격 순으로 매겨져 있어, 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다. 예를 들어, 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다. 체육복이 없으면 수업을 들을 수 없기 때문에 체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 들어야 합니다.
#
# 전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때, 체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.
#
# ### 제한사항
# 전체 학생의 수는 2명 이상 30명 이하입니다.
# 체육복을 도난당한 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
# 여벌의 체육복을 가져온 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
# 여벌 체육복이 있는 학생만 다른 학생에게 체육복을 빌려줄 수 있습니다.
# 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.
#
# ### 입출력 예
# n	lost	reserve	return
# 5	[2, 4]	[1, 3, 5]	5
# 5	[2, 4]	[3]	4
# 3	[3]	[1]	2
# 입출력 예 설명
# 예제 #1
# 1번 학생이 2번 학생에게 체육복을 빌려주고, 3번 학생이나 5번 학생이 4번 학생에게 체육복을 빌려주면 학생 5명이 체육수업을 들을 수 있습니다.
#
# 예제 #2
# 3번 학생이 2번 학생이나 4번 학생에게 체육복을 빌려주면 학생 4명이 체육수업을 들을 수 있습니다.
#
# ### 출처
#
# ※ 공지 - 2019년 2월 18일 지문이 리뉴얼되었습니다.
# ※ 공지 - 2019년 2월 27일, 28일 테스트케이스가 추가되었습니다.

def solution(n, lost, reserve):
    student = [i for i in range(1, n+1) ]  # 전체 학생의 리스트 
    use = list(set(student) - set(lost))  # 전체 학생에서 잃어버린 학생 빼기. 
    
    # 여분의 옷을 가져온 애들이 도난 당하면, 자기 자신의 옷을 입기 -> reserve, lost 리셋하기
    result = use + [ i for i in list(set(lost) & set(reserve))]
    reserve_lost = list(set(lost) & set(reserve))
    reserve = [i for i in reserve if i not in set([ i for i in reserve_lost])]
    lost = [j for j in lost if j not in set([ i for i in reserve_lost])]
    
    for i in reserve: # 오른쪽 왼쪽 비교 .
        if  (i - 1 in lost) & ( i > 1) : # 1번 부터 생각해야 오류가 안남
            result.append(i - 1)
            lost.remove(i - 1)

        elif (i + 1 in lost) & ( i < n) :
            result.append(i+1)
            lost.remove(i + 1)
                
    return len(set(result))


# +
n = 8 # 전체 학생 
lost = [1,3,6,8]
reserve = [2,4,7]

solution(n, lost, reserve)


# +
# 같이 보면 좋을 코드

def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)  # 나는 체육복입을 학생의 수를 생각했으나, 여긴그냥 n에서 lost를 뻄
# -


