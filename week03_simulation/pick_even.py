# [프로그래머스 입문] 짝수만 골라내기
# 리스트에서 짝수만 골라 새 리스트로 return
# 예: [1,2,3,4,5,6] -> [2,4,6]
# 핵심: 빈 리스트 만들기 -> 반복 -> 조건 -> append(담기)

def solution(numbers):
    result = []                # 담을 빈 리스트
    for x in numbers:
        if x % 2 == 0:         # 짝수면
            result.append(x)   # result에 담기
    return result

# 테스트
print(solution([1, 2, 3, 4, 5, 6]))   # [2, 4, 6]
