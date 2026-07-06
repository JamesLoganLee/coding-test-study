# [프로그래머스 입문] 1부터 n까지의 합
# 예: n=5 -> 1+2+3+4+5 = 15

def solution(n):
    answer = 0
    for i in range(1, n + 1):
        answer += i
    return answer

# 테스트
print(solution(5))   # 15
print(solution(10))  # 55
