# [실전 모의고사 2회 - 3문제 세트, 제한시간 25분]
# 조금 더 응용된 문제. 제가 가르치지 않은 3가지 기법을 스스로 찾아 적용:
#   1) word[::-1] - 문자열 뒤집기 슬라이싱
#   2) 함수 분리(count_divisors) - 재사용 가능하게 구조화
#   3) 중복 카운트 방지(i != num//i)
#
# ─────────────────────────────────────────────────────────
# 문제4: 정렬 후 연속된 두 수의 차이 중 최댓값
#   sort() + 2주차 '기준값 갱신 패턴'(max_diff)의 응용
# ═══════════════════════════════════════════════════════════════
# [실전 모의고사 2회] 3문제 세트 · 제한시간 25분
# 1회보다 조금 더 응용된 문제. 배운 적 없는 3가지 기법을
# 스스로 찾아 적용함:
#   1) word[::-1]         - 문자열 뒤집기 슬라이싱
#   2) 함수 분리(count_divisors) - 재사용 가능하게 구조화
#   3) i != num//i         - 중복 카운트 방지
# ═══════════════════════════════════════════════════════════════


# ─────────────────────────────────────────────────────────
# 문제4. 정렬 후 연속된 두 수의 차이 중 최댓값 구하기
#   예: [1, 5, 3, 19, 8] -> 정렬하면 [1,3,5,8,19]
#       바로 옆끼리 차이: (3-1)=2, (5-3)=2, (8-5)=3, (19-8)=11
#       -> 이 중 최댓값 11
#
# [사용한 개념]
#   4주차: numbers.sort() - 오름차순 정렬 (sorted()와 달리 원본 리스트 자체를 바꿈)
#   2주차: '기준값 갱신 패턴' - max_diff를 0에서 시작해 더 큰 차이를 만나면 교체
#
# [numbers.sort() vs sorted(numbers) 차이]
#   sorted(numbers) : 정렬된 '새 리스트'를 만들어 돌려줌, 원본은 그대로
#   numbers.sort()  : 원본 리스트 자체를 정렬해서 바꿔버림 (return 값 없음)
#   -> 여기선 원본을 다시 쓸 일이 없으니 sort()로 바로 바꿔도 무방
#
# [한 줄씩 풀이]
#   numbers.sort()              : 리스트를 작은 값부터 순서대로 재배열
#   max_diff = 0                 : 지금까지 찾은 최대 차이값을 0으로 시작
#   for i in range(1, len(numbers)):  : i를 1번 위치부터 마지막까지 (0번은 비교 상대가 없어서 1부터)
#       diff = numbers[i] - numbers[i-1]  : '지금 값'에서 '바로 앞 값'을 뺌 (정렬돼 있으니 항상 0 이상)
#       if diff > max_diff:                : 지금까지 본 것보다 차이가 더 크면
#           max_diff = diff                   : 최댓값 갱신
#   return max_diff              : 반복이 끝난 뒤, 가장 큰 차이를 돌려줌
#
# [숫자로 직접 따라가기] 정렬 후 [1, 3, 5, 8, 19]
#   i=1: numbers[1]-numbers[0] = 3-1 = 2   -> 2>0 이므로 max_diff=2
#   i=2: numbers[2]-numbers[1] = 5-3 = 2   -> 2>2 아님(같음)  max_diff=2 유지
#   i=3: numbers[3]-numbers[2] = 8-5 = 3   -> 3>2 이므로 max_diff=3
#   i=4: numbers[4]-numbers[3] = 19-8 = 11 -> 11>3 이므로 max_diff=11
#   -> 최종 max_diff = 11 (정답)
# ─────────────────────────────────────────────────────────

def solution4(numbers):
    numbers.sort()
    max_diff = 0
    for i in range(1, len(numbers)):
        diff = numbers[i] - numbers[i - 1]
        if diff > max_diff:
            max_diff = diff
    return max_diff


# ─────────────────────────────────────────────────────────
# 문제5. 팰린드롬(회문)인 단어만 골라 리스트로 return
#   회문 = 앞으로 읽으나 뒤로 읽으나 똑같은 단어 (예: level, radar, 기러기)
#   예: ["level","hello","radar","world"] -> ["level","radar"]
#
# [사용한 개념]
#   3주차: 빈 리스트(answer) -> 반복하며 조건에 맞는 것만 append(골라 담기)
#
# [★ 새로 스스로 찾은 문법 - 슬라이싱으로 문자열 뒤집기]
#   word[::-1]
#   -> 파이썬의 '슬라이싱(slicing)' 문법. [시작:끝:간격] 형태인데,
#      셋 다 비우고 간격만 -1을 주면 '처음부터 끝까지 거꾸로'라는 뜻이 됨.
#   예: "level"[::-1] -> "level" (뒤집어도 같음)
#       "hello"[::-1] -> "olleh" (뒤집으면 달라짐)
#
#   6주차에서는 이걸 left/right 투 포인터로 한 글자씩 비교하며 확인했지만
#   (word[left] != word[right] 를 양 끝에서 좁혀가며 비교),
#   이번엔 아예 '통째로 뒤집은 것'과 '원본'을 한 번에 비교하는 훨씬 짧은 방법을 씀.
#
# [한 줄씩 풀이]
#   answer = []                    : 회문인 단어들을 담을 빈 리스트
#   for word in words:              : 단어를 하나씩 꺼내며
#       if word == word[::-1]:        : 원본과 '뒤집은 버전'이 완전히 같으면 = 회문
#           answer.append(word)          : 결과 리스트에 담기
#   return answer                   : 회문들만 모인 리스트 반환
#
# [단어별로 직접 확인해보기]
#   "level" -> 뒤집으면 "level" -> 같음! -> 담김
#   "hello" -> 뒤집으면 "olleh" -> 다름  -> 안 담김
#   "radar" -> 뒤집으면 "radar" -> 같음! -> 담김
#   "world" -> 뒤집으면 "dlrow" -> 다름  -> 안 담김
#   -> 최종 결과 ["level", "radar"] (정답)
# ─────────────────────────────────────────────────────────

def solution5(words):
    answer = []
    for word in words:
        if word == word[::-1]:
            answer.append(word)
    return answer


# ─────────────────────────────────────────────────────────
# 문제6. 1부터 n까지 중, 약수 개수가 가장 많은 수 찾기
#   예: n=10 -> 각 수의 약수 개수를 세어보면
#       1:1개(1)
#       2:2개(1,2)
#       3:2개(1,3)
#       4:3개(1,2,4)
#       5:2개(1,5)
#       6:4개(1,2,3,6)
#       7:2개(1,7)
#       8:4개(1,2,4,8)
#       9:3개(1,3,9)
#       10:4개(1,2,5,10)
#       -> 약수 4개로 최다인 수는 6, 8, 10 세 개 -> 그 중 가장 먼저 나온(작은) 6이 정답
#
# [함수를 두 개로 나눈 이유 - 실전에서 중요한 습관]
#   "약수 개수 세기"라는 작업을 count_divisors라는 '보조 함수'로 따로 뺐다.
#   이렇게 하면:
#     - solution6 안에서 여러 번(1~n까지 매번) 재사용하기 편하다
#     - 코드가 "무엇을 하는지"가 함수 이름만 봐도 바로 읽힌다
#     - 나중에 약수 세는 로직만 따로 테스트하거나 고치기도 쉽다
#
# ── 보조함수: count_divisors(num) - num의 약수 개수를 센다 ──
#
#   [기본 아이디어] 1부터 num까지 다 나눠봐서 나누어떨어지는 개수를 센다
#   [★ 최적화] 문제3에서 썼던 것처럼, num까지 다 볼 필요 없이
#              제곱근(int(num**0.5))까지만 확인해도 충분하다.
#              대신 이번엔 '개수'를 세는 것이라 살짝 다른 트릭이 필요하다.
#
#   약수는 항상 짝을 이룬다. 예를 들어 36의 약수:
#     1 x 36, 2 x 18, 3 x 12, 4 x 9, 6 x 6, ...
#   1부터 6(제곱근)까지만 봐도 -> 36, 18, 12, 9, 6 이라는 반대편 짝을 자동으로 알 수 있다.
#   즉, i를 찾으면 (i, num//i) 두 개가 한 쌍으로 약수라는 뜻!
#
#   count = 0
#   for i in range(1, int(num**0.5) + 1):   : 1부터 제곱근까지 하나씩 확인
#       if num % i == 0:                      : i가 num의 약수이면(나누어떨어지면)
#           count += 1                           : i 자신을 약수로 카운트
#           if i != num // i:                     : i와 그 반대편 짝(num//i)이 서로 다르면
#               count += 1                           : 반대편 짝도 약수이므로 추가 카운트
#                                                    (같으면 = 제곱수, 예: 36의 6x6처럼
#                                                     한 쌍이 사실 같은 수라 한 번만 세야 함)
#   return count
#
#   [숫자로 확인 - num=36]
#     i=1: 36%1=0 -> count=1(자기자신1), 36//1=36, 1!=36 -> count=2(36도 카운트)
#     i=2: 36%2=0 -> count=3(2), 36//2=18, 2!=18 -> count=4(18도)
#     i=3: 36%3=0 -> count=5(3), 36//3=12, 3!=12 -> count=6(12도)
#     i=4: 36%4=0 -> count=7(4), 36//4=9,  4!=9  -> count=8(9도)
#     i=5: 36%5=1(아님) -> 스킵
#     i=6: 36%6=0 -> count=9(6), 36//6=6,  6==6  -> 같으므로 추가 카운트 안 함(중복방지!)
#     -> 총 9개 (실제 36의 약수: 1,2,3,4,6,9,12,18,36 -> 정확히 9개, 맞음)
#
# ── 메인함수: solution6(n) - 1~n 중 약수 개수 최다인 수 찾기 ──
#
#   max_count = 0                        : 지금까지 찾은 '가장 많은 약수 개수'
#   answer = 1                            : 그 개수를 가진 수 (일단 1로 시작)
#   for i in range(1, n + 1):              : 1부터 n까지 하나씩 확인
#       div_count = count_divisors(i)        : i의 약수 개수를 구함 (위 보조함수 사용)
#       if div_count > max_count:              : 지금까지 최다보다 더 많으면
#           max_count = div_count                 : 최다 기록 갱신
#           answer = i                            : 그 수를 답으로 저장
#           (※ '>'를 써서, 동점(같은 개수)일 때는 갱신하지 않음
#              -> 먼저 발견된(더 작은) 수가 그대로 유지됨)
#   return answer
# ─────────────────────────────────────────────────────────

def count_divisors(num):
    count = 0
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            count += 1
            if i != num // i:        # 제곱수가 아닌 경우 반대편 약수도 카운트
                count += 1
    return count

def solution6(n):
    max_count = 0
    answer = 1
    for i in range(1, n + 1):
        div_count = count_divisors(i)
        # '>'를 사용하여 동일한 약수 개수일 경우 더 작은 수(먼저 나온 수)를 유지
        if div_count > max_count:
            max_count = div_count
            answer = i
    return answer


# ═══════════════════════════════════════════════════════════════
# 테스트 실행
# ═══════════════════════════════════════════════════════════════
print(solution4([1, 5, 3, 19, 8]))                          # 11
print(solution5(["level", "hello", "radar", "world"]))       # ['level', 'radar']
print(solution6(10))                                          # 6

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
