# [실전 모의고사 2회 - 3문제 세트, 제한시간 25분]
# 조금 더 응용된 문제. 제가 가르치지 않은 3가지 기법을 스스로 찾아 적용:
#   1) word[::-1] - 문자열 뒤집기 슬라이싱
#   2) 함수 분리(count_divisors) - 재사용 가능하게 구조화
#   3) 중복 카운트 방지(i != num//i)
#
# ─────────────────────────────────────────────────────────
# 문제4: 정렬 후 연속된 두 수의 차이 중 최댓값
#   sort() + 2주차 '기준값 갱신 패턴'(max_diff)의 응용
#
# 문제5: 팰린드롬(회문)인 단어만 골라내기
#   word[::-1] : 문자열을 거꾸로 뒤집는 슬라이싱 문법
#   6주차에서는 left/right 투 포인터로 한 글자씩 비교했지만,
#   이번엔 word == word[::-1] 로 통째로 비교하는 더 짧은 방법을 발견.
#
# 문제6: 1~n 중 약수 개수가 가장 많은 수 찾기
#   count_divisors(num): 약수 개수를 세는 보조함수
#     - int(num**0.5)+1까지만 확인 (문제3의 최적화를 재사용/응용)
#     - i와 num//i가 서로 다를 때만 둘 다 카운트
#       (같으면 제곱수라서 한 번만 세야 함. 예: 36의 약수 6은 6*6=36이라 한 번만)
#   solution(n): 1부터 n까지 돌며 약수 개수가 가장 많은 수를 찾음
#     (동점이면 '>'조건 덕분에 먼저 발견한 더 작은 수가 유지됨)
# ─────────────────────────────────────────────────────────

def solution4(numbers):
    numbers.sort()
    max_diff = 0
    for i in range(1, len(numbers)):
        diff = numbers[i] - numbers[i - 1]
        if diff > max_diff:
            max_diff = diff
    return max_diff

def solution5(words):
    answer = []
    for word in words:
        if word == word[::-1]:      # 뒤집은 단어와 같으면 회문
            answer.append(word)
    return answer

def count_divisors(num):
    count = 0
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            count += 1
            if i != num // i:        # 제곱수가 아니면 반대편 약수도 카운트
                count += 1
    return count

def solution6(n):
    max_count = 0
    answer = 1
    for i in range(1, n + 1):
        div_count = count_divisors(i)
        if div_count > max_count:     # 동점이면 먼저 나온(더 작은) 수 유지
            max_count = div_count
            answer = i
    return answer

# 테스트
print(solution4([1, 5, 3, 19, 8]))                          # 11
print(solution5(["level", "hello", "radar", "world"]))       # ['level', 'radar']
print(solution6(10))                                          # 6
