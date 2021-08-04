# 1. 이진 탐색 ( Binary Search )
# 탐색할 자료를 둘로 나누어 해당 데이터가 있을 만한 곳을 탐색하는 방법
# 탐색 알고리즘 중 하나 : 순차 탐색, 해시, 이진탐색

# 2. 분할 정복 알고리즘 과 이진 탐색
# 분할 정복 알고리즘
# - 문제를 하나 또는 둘이상으로 나누고, 해결이 가능하면 해결하고 아니면 다시 나누고
# - 보통 재귀용법을 많이 사용함
# 이진 탐색
# - 리스트를 두개의 서브 리스트로 나누고, 검색할 숫자가 왼쪽/ 오른쪽에 위치하는지 파악해서 찾음

# 3. 어떻게 코드로 만들까?
# 이진 탐색은 데이터가 정렬되어 있는 상태에서 진행
# 데이터가 [2, 3,8, 12, 20 ] 일때, binary_search(data_list, find_data)함수를 만들고,
# data_list의 중간값을 find_data와 비교해서 찾기.

# 4. 알고리즘 구현

def binary_search(data, search):
    print(data) # 확인하기 위한 코드
    # 재귀를 하기 전에!
    # 데이터가 반반씩 줄어들면 1이된 경우가 존재! 여기부터 접근!
    if len(data) == 1 and search == data[0]: # And 마지막에 검색한 숫자가 원하는 데이타!
        return True
    if len(data) == 1 and search != data[0] : # 줄어들어 1이지만, 마지막 검색한 숫자가 내가 원하는 아이가 아니다.
        return False
    if len(data) == 0:
        return False

    # 중간값 정하기
    medium = len(data) //2  # 나눈것의 몫
    if search == data[medium]:
        return True
    else:
        if search > data[medium]: # 만약에 검색이 데이타 뒤에 있다면,
            return binary_search(data[medium:], search) # 뒤에 리스트에 대해서 판단
        else : # 그렇지 않다면 앞부분에 있으니깐,
            return binary_search(data[:medium], search)


import random
data_list = random.sample(range(100), 10)
print(data_list)

# 정렬시키기
data_list.sort() # .sort() 를하면 원본 리스트를 바꾸어줌 따로, 변수에 넣어주지 않아도됨
print(data_list)

bi = binary_search(data_list , data_list[2]) # 원래는 targe 은 숫자
print(bi)

# 알고리즘 분석 - 시간 복잡도 O(log_n)
