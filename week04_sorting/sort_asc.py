# [프로그래머스 입문] 오름차순 정렬
# 리스트를 작은 것부터 정렬해서 return
# 예: [5,2,8,1,9] -> [1,2,5,8,9]
# 핵심: sorted(리스트) 한 줄

def solution(numbers):
    answer = sorted(numbers)
    return answer

# 테스트
print(solution([5, 2, 8, 1, 9]))   # [1, 2, 5, 8, 9]
