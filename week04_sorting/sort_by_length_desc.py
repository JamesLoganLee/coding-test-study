# [프로그래머스 입문] 길이순 정렬 (긴 것부터)
# 문자열 리스트를 길이가 긴 순으로 정렬
# 예: ["banana","kiwi","apple","fig"] -> ['banana','apple','kiwi','fig']
# 핵심: key(기준) + reverse(방향) 조합

def solution(words):
    answer = sorted(words, key=len, reverse=True)
    return answer

# 테스트
print(solution(["banana", "kiwi", "apple", "fig"]))   # ['banana', 'apple', 'kiwi', 'fig']
