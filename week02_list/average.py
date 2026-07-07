# [프로그래머스 입문] 평균 구하기
# 리스트의 평균을 return
# 예: [10,20,30,40] -> 25.0
# 핵심: 평균 = 합계(sum) / 개수(len)

def solution(numbers):
    answer = sum(numbers) / len(numbers)   # 합 ÷ 개수
    return answer

# 테스트
print(solution([10, 20, 30, 40]))   # 25.0

# 자주 쓰는 도구 3형제: sum(합) / len(개수) / max·min(최대·최소)
