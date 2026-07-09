# [프로그래머스 입문] 길이순 정렬 (짧은 것부터)
# 문자열 리스트를 길이가 짧은 순으로 정렬
# 예: ["banana","kiwi","apple","fig"] -> ['fig','kiwi','apple','banana']
# 핵심: key=len (무엇을 '기준'으로 정렬할지 지정)

def solution(words):
    answer = sorted(words, key=len)
    return answer

# 테스트
print(solution(["banana", "kiwi", "apple", "fig"]))   # ['fig', 'kiwi', 'apple', 'banana']
