# 입국 심사를 기다리는 사람 수 n
# 각 심사관이 한명을 심사하는데 걸리는 시간이 담긴 배열 times
# 모든 사람이 심사를 받는데 걸리는 최솟값을 return

n = 6
times = [7,10]

min_time = 1
max_time = max(times) * n

answer =0
while min_time < max_time :
    medium = (min_time + max_time) // 2
    work = 0

    for t in times:
        work += medium // t

        if work >= n:
            max_time = medium
        elif work < n:
            min_time = medium
answer = min_time
print(min_time)