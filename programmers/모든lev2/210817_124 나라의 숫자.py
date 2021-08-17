# 방법1.  시간초과 코드

from itertools import permutations

def solution(n):
    
    country_all_number = ["1",'2','4']
    repeat = 2 
    num = 10
    country_num = country_all_number * num
    
    while  True:
        if len(country_all_number) > n:
            break
        
        permutation = set(list(permutations(country_num, repeat)))
        per_list = list(map(lambda x : ''.join(list(x)) , list(permutation)))
        per_list.sort()
        
        country_all_number.extend(per_list)
        repeat += 1
    
    answer = country_all_number[n-1]
    return str(answer)
  
  
 
# 2. 통과 코드 - divmod() 이용

def solution(n):
    
    result = []
    
    while n >0:
        
        if n % 3 != 0:
            temp = divmod(n, 3)
            result.append(temp[-1])
            n = temp[0]
            
        elif n % 3 == 0:
            quotient = n // 3 - 1
            temp = 4
            result.append(temp)
            n = quotient

    answer = result[::-1]
    answer = ''.join(list(map(lambda x : str(x), answer)))
    return answer
  
  
 # 대단한 사람 버전 1. 문자열을 그대로 사용함

def solution(n):
    num = ['1','2','4']
    answer = ""

    while n > 0:
        n -= 1
        answer = num[n % 3] + answer # 나머지는 맨 앞으로 가겠금..
        n //= 3    # 몫을 구해서 그것을 새로운 n으로 

    return answer
  
  
# 대단한 사람 버전 2. divmod 와 재귀 함수

def solution(n):
    if n<=3:
        return '124'[n-1]
    else:
        q, r = divmod(n-1, 3) 
        return solution(q) + '124'[r]
