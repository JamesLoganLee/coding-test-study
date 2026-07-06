# [프로그래머스 입문] n 이하 짝수의 합
# 1부터 n까지 중 짝수만 더하기. 예: n=10 -> 2+4+6+8+10 = 30
# 핵심: 반복문(for) 안에 조건문(if)

def solution(n):
    answer = 0
    for i in range(1, n + 1):
        if i % 2 == 0:      # 짝수일 때만
            answer += i
    return answer

# 테스트
print(solution(10))  # 30
