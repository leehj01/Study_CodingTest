import re
from itertools import permutations

def solution(expression):

    calculator = re.sub('[0-9]', '', expression)
    calculator = ','.join(calculator).split(',')
    order_cal = list(permutations(set(calculator), len(set(calculator))))

    answer = []
    if len(set(calculator)) > 1 :

        for order in order_cal:
            last = order[-1]
            second = order[-2]
            calculating = expression.split(last)

            result = []
            for cal in calculating:
                if second in cal:
                    temp = cal.split(second) # ['99-133', '221', '334', '555-166-144-551-166']
                    temp = list(map(eval, temp))  # [-34, 221, 334, -472]
                    temp = list(map(str, temp)) # ['-34', '221', '334', '-472']
                    temp = second.join(temp) # -34+221+334+-472
                    result.append(str(eval(temp)))  # 49
                else :
                    result.append(str(eval(cal)))

            result = abs(eval(last.join(result)))
            answer.append(result)
            
    else:
        answer = [abs(eval(expression))]
    return max(answer)
