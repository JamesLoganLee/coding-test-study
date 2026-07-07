# [프로그래머스 입문] 최댓값 찾기
# 리스트에서 가장 큰 값을 return
# 예: [3,7,2,9,5] -> 9
# 핵심: '기준값 갱신' 패턴 (일단 하나 잡고, 더 크면 바꾼다)

def solution(numbers):
    biggest = numbers[0]       # 첫 값을 '현재 최대'로 시작
    for x in numbers:
        if x > biggest:        # 지금 값이 더 크면
            biggest = x        # 최댓값 갱신
    return biggest

# 테스트
print(solution([3, 7, 2, 9, 5]))   # 9

# 참고: max(numbers) 한 줄로도 가능 (원리를 익힌 뒤엔 편한 도구 사용 OK)
