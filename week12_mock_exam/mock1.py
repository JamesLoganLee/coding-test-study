# [실전 모의고사 1회 - 3문제 세트, 제한시간 20분]
# 힌트 없이 스스로 풀어보는 실전 훈련. 3문제 모두 정답 + 시간 내 완료.
#
# ─────────────────────────────────────────────────────────
# 문제1: 3의 배수만 골라 합 구하기
#   1주차(누적 +=) + 3주차(조건 필터링) 조합
#
# 문제2: 가장 많이 등장한 글자 찾기
#   collections.Counter를 스스로 찾아 활용 (7주차 개수세기의 발전형)
#   Counter(s) : 문자열 각 글자의 개수를 자동으로 세어주는 도구
#   most_common(1) : 가장 많이 나온 것 1개를 [(글자, 개수)] 형태로 반환
#
# 문제3: 소수(prime) 판별
#   - n <= 1 예외처리 (엣지 케이스 감각, 2주차 개념 재사용)
#   - int(n**0.5)+1까지만 확인하는 최적화
#     (제곱근까지만 나눠봐도 충분 - n까지 다 볼 필요 없음)
# ─────────────────────────────────────────────────────────

def solution1(numbers):
    answer = 0
    for num in numbers:
        if num % 3 == 0:
            answer += num
    return answer

from collections import Counter
def solution2(s):
    count = Counter(s)
    return count.most_common(1)[0][0]

def solution3(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 테스트
print(solution1([1, 3, 6, 7, 9, 10]))   # 18
print(solution2("banana"))               # a
print(solution3(7))                      # True
print(solution3(8))                      # False
