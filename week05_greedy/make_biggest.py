# [그리디] 가장 큰 수 만들기
# 한 자리 숫자들을 이어붙여 만들 수 있는 가장 큰 수(문자열)
# 예: [3,1,4,1,5] -> "54311"
#
# [그리디 포인트] 큰 숫자부터 앞에 놓으면 가장 큰 수가 된다 = 내림차순 정렬
#
# [핵심 문법]
#   sorted(x, reverse=True) : 내림차순 정렬 (4주차)
#   str(x)  : 숫자를 '글자'로 변환 -> 글자끼리 +는 이어붙이기 ("5"+"4"="54")
#   int(str) : 앞자리 불필요한 0 제거용 (예: "00"->0)

def solution(numbers):
    answer = ""
    for x in sorted(numbers, reverse=True):   # 큰 숫자부터
        answer += str(x)                       # 글자로 바꿔 이어붙이기
    return str(int(answer))                     # 맨 앞 0 제거(엣지 케이스 대비)

# 테스트
print(solution([3, 1, 4, 1, 5]))   # "54311"
