
def my_solution(N, stages):
    fail_rate_dic = {}
    try_people = len(stages)
        
    for idx in range(1,N+1):
        if idx in list(set(stages)):
            fail_stage = stages.count(idx)
            fail_rate = fail_stage / try_people
            fail_rate_dic[idx] = fail_rate
            try_people -= fail_stage
        else:
            fail_rate_dic[idx] = 0.0
    fail_rate_dic = sorted(fail_rate_dic.items(), key=lambda x:x[1], reverse=True)
    fail_rate_list = list(map(lambda x:x[0], fail_rate_dic))
    return fail_rate_list
  
  
# 

# list.count() 를 해서, 한번에 데이터를 뽑아오는 것이 속도를 줄이는데 도움이 된다. 
# sorted(result, key=lambda x : result[x], reverse=True) 이런식으로 하면, 위의 두줄을 한번에 풀수도 있는 것같다. 
# 좋아요 많이 받은 코드와 내코드가 비슷해서 기분이가 좋담 ><
