# [프로그래머스 입문] 홀수만 골라 제곱하기
# 홀수만 골라 각각 제곱해서 새 리스트로 return
# 예: [1,2,3,4,5] -> [1,9,25]  (1^2, 3^2, 5^2)
# 핵심: '고르기(if) + 변형(제곱)' 조합

def solution(numbers):
    result = []
    for x in numbers:
        if x % 2 == 1:            # 홀수면
            result.append(x ** 2) # 제곱(**)해서 담기
    return result

# 테스트
print(solution([1, 2, 3, 4, 5]))   # [1, 9, 25]
