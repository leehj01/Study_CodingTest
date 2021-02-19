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

# 조이스틱으로 알파벳 이름을 완성하세요. 맨 처음엔 A로만 이루어져 있습니다.
# ex) 완성해야 하는 이름이 세 글자면 AAA, 네 글자면 AAAA
#
# 조이스틱을 각 방향으로 움직이면 아래와 같습니다.
#
#
# ▲ - 다음 알파벳
# ▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)
# ◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
# ▶ - 커서를 오른쪽으로 이동
#
#
# 예를 들어 아래의 방법으로 JAZ를 만들 수 있습니다.
#
#
# - 첫 번째 위치에서 조이스틱을 위로 9번 조작하여 J를 완성합니다.
# - 조이스틱을 왼쪽으로 1번 조작하여 커서를 마지막 문자 위치로 이동시킵니다.
# - 마지막 위치에서 조이스틱을 아래로 1번 조작하여 Z를 완성합니다.
# 따라서 11번 이동시켜 "JAZ"를 만들 수 있고, 이때가 최소 이동입니다.
#
#

name = 'AXAAAAABAB'

# +
cnt = 0
loca = 0  # location

m = [ min(ord(c) - ord('A'), ord('Z')-ord(c) + 1) for c in name ]
print(m)

while True :
    print(name)
    cnt += m[loca]
    
    
    left , right = 1, 1
    print(m[loca + right])
#     loca += 

    break

# +
name = 'ABABAAAAABA'
m = [ min(ord(c) - 65, 91-ord(c)) for c in name]       

answer = 0
where = 0

while True:    
    answer += m[where]
    m[where] = 0

    if sum(m) == 0:
        break

    left, right = (1,1)

    while m[where - left] <= 0:
        left += 1
    while m[where + right] <= 0:
        right += 1

    answer += left if left < right else right
    where += -left if left < right else right
# -

answer

# +
name = 'ABABAAAAABA'
cnt = 0
loca = 0  # location

len(name)

dx = [-1, 1 ]

for i in range(len(name) ):
    if name[i] < 'N':
        print(name[i])
        cnt += (ord(name[i]) - ord('A'))
        
    elif name[i] >= 'N':
        print(name[i])
        cnt += (ord('Z') - ord(name[i])) + 1 
        
if name[-2] == 'A' and len(name) == 3 and name != 'AAA':
    cnt += 1
elif min(name) == 'A' and max(name) == 'A':
    cnt = 0 
else :
    cnt += len(name) -1 
# -

name = 'ABABAAAAABA'
def max_a(name):
    a = list()
    a_max= 0
    for i in name :
        if i == 'A':
            a.append(i)
            print(a)
        else :
            if a_max > len(a) :
                a = list()
                a_max += len(a)
                return a_max
            else:
                a = list()
                a_max += len(a)
            
            
    print(a)
    print(a_max)
    return a

max_a(name)

from collections import Counter

Counter(name)

m = [ min(ord(c) - 65, 91-ord(c)) for c in name ]
m





cnt += -(ord(max([max(i) for i in name if i > 'N' ])) - ord('Z') ) + 1
cnt

print([max(i) for i in name if i < 'N' ])
ord(min([max(i) for i in name if i < 'N' ]) ) - ord('A')

print([max(i) for i in name if i > 'N' ])
print(max([max(i) for i in name if i > 'N' ]))

- (ord(max([max(i) for i in name if i > 'N' ])) - ord('Z') ) + 1

ord('N' )- ord('A')

'A' > 'B'
'A' < 'B'
'A' < 'Z'

tmp = 'ANMGHB'

max(tmp)


