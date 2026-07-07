# [프로그래머스 입문] 최솟값 찾기
# 리스트에서 가장 작은 값을 return
# 예: [3,7,2,9,5] -> 2
# 핵심: 최댓값 코드에서 부등호 방향만 반대로(<)
#       + 빈 리스트 대비(엣지 케이스)

def solution(numbers):
    if not numbers:            # 리스트가 비어 있으면
        return None            # 오류 대신 None 반환 (예외 처리)
    smallest = numbers[0]
    for x in numbers:
        if x < smallest:       # 지금 값이 더 작으면
            smallest = x       # 최솟값 갱신
    return smallest

# 테스트
print(solution([3, 7, 2, 9, 5]))   # 2

# 참고: min(numbers) 한 줄로도 가능
