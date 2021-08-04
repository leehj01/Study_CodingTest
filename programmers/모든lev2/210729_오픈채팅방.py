
# 첫코드
def solution(record):

    id_list , user_info = [] , []
    record_list = []

    for reco in record:
        chat_alam = [r for r in reco.split()]
        user_id = chat_alam[1].split('d')[1]  

        if chat_alam[0] == 'Enter':
            user_nm = chat_alam[2]

            if user_id in id_list :
                print(user_id)
                num = id_list.index(user_id)
                user_info[num][1] = user_nm
                record_list.append([user_id, '님이 들어왔습니다.'])
            
            else:
                id_list.append(user_id)  
                user_info.append([user_id,user_nm])
                record_list.append([user_id, '님이 들어왔습니다.'])


        elif chat_alam[0] == 'Leave' :
            user_nm = user_info[id_list.index(user_id)][1]
            record_list.append([user_id, '님이 나갔습니다.'])

        elif chat_alam[0] == 'Change' :
            user_nm = chat_alam[2]
            num = id_list.index(user_id)
            user_info[num][1] = user_nm

    answer = []
    for user_re in record_list:
        for user in user_info:
            if user_re[0] == user[0]:
                user_re[0] = user[1]

        user_result = user_re[0]+user_re[1]
        answer.append(user_result)
        
    print(id_list)
    print(user_info)
    print(record_list)
    return answer
  
  
  # 수정 후
  
  def solution(record):
    chat_alam = [r.split(' ') for r in record]
    udb = {log[1]:log[2] for log in chat_alam if len(log)==3}

    answer = []
    for user in chat_alam:
        if user[0] == 'Enter':
            nm = udb[user[1]]
            answer.append('{}님이 들어왔습니다.'.format(nm))
        if user[0] == 'Leave':
            nm = udb[user[1]]
            answer.append('{}님이 나갔습니다.'.format(nm))
    return anser
  
  
  
  # 참고 코드 - 천재인가.. 
  def solution(record):
    logs = [r.split(' ') for r in record]
    udb = {log[1]:log[2] for log in logs if len(log)==3}
    
    return [udb[log[1]]+'님이 들어왔습니다.' if log[0] == 'Enter' else  udb[log[1]]+'님이 나갔습니다.' for log in logs if log[0] !='Change']
