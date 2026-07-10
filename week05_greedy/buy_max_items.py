# [그리디] 예산으로 최대한 많이 사기
# 예산 budget으로 물건(prices)을 가장 많이 사면 몇 개?
# 예: prices=[3,1,2,4,5], budget=7 -> 3개 (싼 것부터 1+2+3=6)
#
# [그리디 포인트] 개수를 최대로 하려면 '싼 것부터' 산다.
#                싼 것부터 정렬했으니, 하나라도 못 사면 뒤는 다 못 삼 -> break로 멈춤
#
# [핵심 문법]
#   sorted(prices)   : 오름차순(싼 것부터)
#   budget -= price  : 예산에서 물건값 빼기(갱신)
#   count += 1       : 살 때마다 개수 1 늘리기(손가락 세듯)
#   break            : 반복 즉시 멈추기

def solution(prices, budget):
    count = 0
    prices = sorted(prices)          # 싼 것부터 정렬
    for price in prices:
        if budget >= price:          # 예산이 이 물건을 살 수 있으면
            budget -= price          # 예산에서 빼고
            count += 1               # 개수 1 늘리기
        else:                        # 예산이 부족하면
            break                    # 더 볼 필요 없이 멈춤
    return count

# 테스트
print(solution([3, 1, 2, 4, 5], 7))   # 3
