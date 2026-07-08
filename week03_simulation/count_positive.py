# [프로그래머스 입문] 양수 개수 세기
# 리스트에서 양수가 몇 개인지 세어 return
# 예: [-2,5,-1,3,0,7] -> 3  (양수: 5,3,7)
# 핵심: '담기(append)' 대신 '세기(count += 1)'

def solution(numbers):
    count = 0
    for x in numbers:
        if x > 0:          # 양수면 (0은 제외)
            count += 1     # 개수 1 늘리기
    return count

# 테스트
print(solution([-2, 5, -1, 3, 0, 7]))   # 3
