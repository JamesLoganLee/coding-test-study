# [프로그래머스 입문] 내림차순 정렬
# 리스트를 큰 것부터 정렬해서 return
# 예: [5,2,8,1,9] -> [9,8,5,2,1]
# 핵심: reverse=True 옵션

def solution(numbers):
    answer = sorted(numbers, reverse=True)
    return answer

# 테스트
print(solution([5, 2, 8, 1, 9]))   # [9, 8, 5, 2, 1]
