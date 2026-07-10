# [그리디] 두 수의 곱 최댓값
# 리스트에서 두 수를 골라 곱한 값 중 가장 큰 값
# 예: [1,5,3,8,2] -> 40 (가장 큰 두 수 8x5)
#
# [그리디 포인트] 곱을 최대로 하려면 '가장 큰 두 수'를 곱한다.
#
# [핵심 문법]
#   sorted(x, reverse=True) 후 numbers[0], numbers[1] = 1등, 2등
#   *  : 곱하기

def solution(numbers):
    numbers = sorted(numbers, reverse=True)   # 큰 것부터 정렬
    answer = numbers[0] * numbers[1]          # 앞 두 개(가장 큰 두 수) 곱하기
    return answer

# 테스트
print(solution([1, 5, 3, 8, 2]))   # 40
