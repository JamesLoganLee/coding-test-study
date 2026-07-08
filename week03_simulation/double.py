# [프로그래머스 입문] 2배로 만들기
# 리스트의 각 값을 2배로 만든 새 리스트를 return
# 예: [1,2,3] -> [2,4,6]
# 핵심: 조건 없이 '모든 값을 변형'해서 담기

def solution(numbers):
    result = []
    for x in numbers:
        result.append(x * 2)   # 값을 2배로 변형해 담기
    return result

# 테스트
print(solution([1, 2, 3]))   # [2, 4, 6]
