# 입국 심사를 기다리는 사람 수 n
# 각 심사관이 한명을 심사하는데 걸리는 시간이 담긴 배열 times
# 모든 사람이 심사를 받는데 걸리는 최솟값을 return

n = 6
times = [7,10]

def solution(n ,times):
    answer = 0
    left = 1
    right = max(times) * n

    while left < right :
        mid = (left + right) //2

        work = 0
        for time in times:
            work += mid // time

        if work >= n:
            right = mid
        elif work < n:
            left = mid + 1

    answer = left
    return answer