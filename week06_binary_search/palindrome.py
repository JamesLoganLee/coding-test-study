# [투 포인터] 회문(팰린드롬) 판별
# 문자열이 앞뒤가 똑같으면(거꾸로 읽어도 같으면) True, 아니면 False
# 예: "level" -> True / "hello" -> False
# (회문 예: 기러기, 토마토, level, racecar)
#
# ─────────────────────────────────────────────────────────
# [투 포인터 활용]
#   양 끝에서 글자를 하나씩 비교하며 안쪽으로 좁혀온다.
#
#   l e v e l
#   ↑       ↑     'l' == 'l' ✅ 같다 → 안쪽으로
#  left   right
#
#   l e v e l
#     ↑   ↑       'e' == 'e' ✅ 같다 → 안쪽으로
#
#   l e v e l
#       ↑         두 손가락이 만남 → 끝! 다 같았으니 True
#
# [핵심 논리]
#   양 끝이 '다르면' 즉시 False (더 볼 필요 없음)
#   같으면 양쪽 손가락을 안쪽으로 → 반복 → 끝까지 같으면 True
#
# [새 문법]
#   word[left] : 문자열도 리스트처럼 위치로 글자를 꺼낼 수 있다
#                "level"[0] = 'l'
#   !=         : "같지 않다"
#
# [들여쓰기 주의 ★]
#   left += 1 과 right -= 1 은 'if 밖, while 안'에 있어야 한다.
#   (조건에 상관없이 매번 좁혀야 하므로)
# ─────────────────────────────────────────────────────────

def solution(word):
    left = 0
    right = len(word) - 1

    while left < right:                  # 두 손가락이 만나기 전까지
        if word[left] != word[right]:    # 양 끝 글자가 다르면
            return False                 # 회문이 아님! 즉시 종료
        left += 1                        # 왼쪽 손가락 오른쪽으로
        right -= 1                       # 오른쪽 손가락 왼쪽으로

    return True                          # 끝까지 다 같으면 회문!

# 테스트
print(solution("level"))   # True
print(solution("hello"))   # False
