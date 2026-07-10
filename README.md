[README.md](https://github.com/user-attachments/files/29876331/README.md)# 🧩 코딩테스트 학습 기록

> 프로그래머스를 중심으로 **매일 1~2문제씩** 푸는 알고리즘 학습 일지입니다.
> 목표: 은행권 디지털 직군 코딩테스트 대비 · Python

---

## 📌 공부 원칙 (나와의 약속)
1. 하루 1~2문제씩 **매일** > 주말 몰아치기
2. 30분 고민 후 막히면 **답 보고 이해** (죄책감 X)
3. 답 본 문제는 **다음날 다시 풀기** (복습이 핵심)
4. 눈으로 X, **직접 타이핑**해서 통과시키기

---

## 📊 진행 현황
| 주차 | 주제 | 푼 문제 수 | 상태 |
|------|------|:------:|:------:|
| 1주 | 기초 문법 (입출력·조건문·반복문) | 4 | ✅ 완료 |
| 2주 | 자료구조 기초 (리스트) | 4 | ✅ 완료 |
| 3주 | 구현·시뮬레이션 | 4 | ✅ 완료 |
| 4주 | 정렬 | 4 | ✅ 완료 |
| 5주 | 그리디 | 4 | ✅ 완료 |
| 6주 | 이분탐색·투포인터 | 0 | ⬜ 예정 |
| 7주 | 스택·큐·해시 | 0 | ⬜ 예정 |
| 8~9주 | DFS/BFS | 0 | ⬜ 예정 |
| 10주 | 동적계획법(DP) | 0 | ⬜ 예정 |
| 11~12주 | 복습·실전 모의고사 | 0 | ⬜ 예정 |

> **Phase 1 완주** ✅ → **Phase 2 진행 중** (정렬·그리디 ✅ / 다음: 이분탐색·DFS/BFS)

---

## ✅ 1주차 — 기초 문법

| 문제 | 배운 개념 | 파일 |
|------|-----------|------|
| 두 수의 합 | 함수·return | [two_sum.py](week01_basic/two_sum.py) |
| 짝수와 홀수 | `if/else`, `%`, `==` | [even_odd.py](week01_basic/even_odd.py) |
| 1부터 n까지 합 | `for`, `range`, 누적(`+=`) | [sum_1_to_n.py](week01_basic/sum_1_to_n.py) |
| n 이하 짝수의 합 | 반복문 안에 조건문 | [even_sum.py](week01_basic/even_sum.py) |

## ✅ 2주차 — 자료구조 기초 (리스트)

| 문제 | 배운 개념 | 파일 |
|------|-----------|------|
| 리스트 원소의 합 | `for x in numbers`로 하나씩 꺼내 누적 | [list_sum.py](week02_list/list_sum.py) |
| 최댓값 찾기 | '기준값 갱신' 패턴 (`if x > biggest`) | [find_max.py](week02_list/find_max.py) |
| 최솟값 찾기 | 부등호 반대(`<`) + 빈 리스트 예외처리 | [find_min.py](week02_list/find_min.py) |
| 평균 구하기 | `sum()` ÷ `len()` | [average.py](week02_list/average.py) |

## ✅ 3주차 — 구현·시뮬레이션

| 문제 | 배운 개념 | 파일 |
|------|-----------|------|
| 짝수만 골라내기 | 빈 리스트 → 조건 → `append`(담기) | [pick_even.py](week03_simulation/pick_even.py) |
| 2배로 만들기 | 값 변형해서 담기 (`x * 2`) | [double.py](week03_simulation/double.py) |
| 홀수 제곱 | 고르기 + 변형 조합 (`x ** 2`) | [odd_square.py](week03_simulation/odd_square.py) |
| 양수 개수 세기 | 담기 대신 세기 (`count += 1`) | [count_positive.py](week03_simulation/count_positive.py) |

## ✅ 4주차 — 정렬

| 문제 | 배운 개념 | 파일 |
|------|-----------|------|
| 오름차순 정렬 | `sorted(리스트)` | [sort_asc.py](week04_sorting/sort_asc.py) |
| 내림차순 정렬 | `reverse=True` | [sort_desc.py](week04_sorting/sort_desc.py) |
| 길이순 정렬 | `key=len` (기준 정하기) | [sort_by_length.py](week04_sorting/sort_by_length.py) |
| 길이 긴 순 정렬 | `key` + `reverse` 조합 | [sort_by_length_desc.py](week04_sorting/sort_by_length_desc.py) |

## ✅ 5주차 — 그리디

| 문제 | 배운 개념 | 파일 |
|------|-----------|------|
| 거스름돈 최소 개수 | 큰 단위부터 · `//`(몫) `%`(나머지) · 값 갱신 | [change_coins.py](week05_greedy/change_coins.py) |
| 가장 큰 수 만들기 | 내림차순 + `str()`로 이어붙이기 | [make_biggest.py](week05_greedy/make_biggest.py) |
| 두 수 곱 최댓값 | 정렬 후 앞 두 개 곱하기 | [max_product.py](week05_greedy/max_product.py) |
| 최대한 많이 사기 | 싼 것부터 + `break`(못 사면 멈춤) | [buy_max_items.py](week05_greedy/buy_max_items.py) |

---

## 📝 배운 것 메모 (헷갈릴 때 여기 보기)

### 1주차 — 기초 문법
- `int(input())`, 짝수 `num % 2 == 0`, 줄 끝 `:` (콜론)
- `==`(판단) / `=`(대입) / `!=`(같지 않다)

### 2주차 — 리스트
- 리스트 `[10,20,30]`, 맨 앞은 **0번**부터
- **기준값 갱신 패턴**(최대·최소), 도구 3형제 `sum` `len` `max/min`
- 빈 리스트 대비 `if not numbers: return None`

### 3주차 — 구현
- 뼈대: 빈 리스트 → 반복 → (조건) → 담기(`append`)/세기(`count += 1`)
- 변형해 담기: `append(x*2)`, `append(x**2)`

### 4주차 — 정렬
- 오름차순 `sorted(x)` / 내림차순 `reverse=True`
- 기준 `key=len` / 조합 `sorted(x, key=len, reverse=True)`

### 5주차 — 그리디 (매 순간 가장 유리한 것부터!)
- **핵심 감각**: "지금 가장 좋아 보이는 것"을 계속 선택 → 전체 최선
- **정렬이 그리디의 무기**: 큰 것부터 / 싼 것부터 정렬해두고 순서대로 처리
- `//` = 몫, `%` = 나머지 (거스름돈에서 개수와 남은 돈 계산)
- `str(x)` = 숫자를 글자로 (이어붙이기용) / `int()` = 앞 0 제거
- `budget -= price` = 값 갱신 / `break` = 반복 즉시 멈추기
- **break 논리**: 싼 것부터 정렬 → 하나 못 사면 뒤도 다 못 삼 → 멈춤

---

*학습 기간: 2026.7 ~ · 참고: 프로그래머스, '이것이 취업을 위한 코딩테스트다 with 파이썬'*
