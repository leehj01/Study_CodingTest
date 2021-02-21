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


