begin_list = [i for i in begin]
cnt = 0
for w in word:
    for idx, val in enumerate(w):
        if (val in target) & ( val not in begin_list):
            begin_list[idx] = val
            print(begin_list)
            cnt += 1 
print(cnt)
