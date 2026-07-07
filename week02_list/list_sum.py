# [프로그래머스 입문] 리스트 원소의 합
# 정수 리스트 numbers의 모든 원소를 더해 return
# 예: [1,2,3,4,5] -> 15
# 핵심: for로 리스트에서 값을 하나씩 꺼내 누적(+=)

def solution(numbers):
    answer = 0
    for x in numbers:      # 리스트에서 값을 하나씩 x에 꺼냄
        answer += x        # 꺼낸 값을 계속 더해 쌓기
    return answer

# 테스트
print(solution([1, 2, 3, 4, 5]))   # 15
print(solution([10, 20, 30]))      # 60
