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

def solution(new_id):
    answer = ''

    new_id = new_id.lower()

    for c in new_id:
        if c.isalnum() or c in ['-', '_', '.']:
            answer += c

    while '..' in answer:
        answer = answer.replace('..', '.')

    if answer[0] == '.':
        if len(answer) > 1 :
            answer = answer[1:] 
        
    if answer[-1] == '.':
        answer = answer[:-1]

    if answer == '':
        answer = 'a'

    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    if len(answer) <= 2:
        answer = answer + answer[-1] * (3-len(answer))
    return answer


