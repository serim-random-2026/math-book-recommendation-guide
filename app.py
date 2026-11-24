# 1. [입력 화면] 제일 먼저 실행
print("=" * 46)
print("\n(1) 현재 학년 학기 선택 => [ 1학년 / 2학년 / 3학년 ], [ 1학기 / 2학기 ]")
year = input("    ▶ 학년 선택 (1학년/2학년/3학년): ")
semester = input("    ▶ 학기 선택 (1학기/2학기): ")
old = f"{year} {semester}"

print("\n(2) 최근 지필 성적 입력 => ( 숫자 ) 점")
grade = int(input("    ▶ 점수 입력: "))

input("\n[버튼; 분석하기] (실행하려면 Enter 키를 누르세요)")


# 2. 난이도별 추천 교육 자료 리스트 & 추천 이유 매칭
easy_problem = ["개념원리", "RPM", "연산"]
middle_problem = ["풍산자", "고쟁이", "쎈"]
hard_problem = ["올림포스", "블랙라벨", "마더텅"]

reasons = {
    "개념원리": "기초 개념과 원리 정리에 최적",
    "RPM": "필수 유형 반복 훈련용",
    "연산": "기초 계산 실수 방지 및 속도 향상",
    "풍산자": "핵심 개념 압축 및 실전 감각 익히기",
    "고쟁이": "중상위권 도약을 위한 유형 심화",
    "쎈": "방대한 문제량으로 빈출 유형 마스터",
    "올림포스": "내신 고난도 및 서술형 대비",
    "블랙라벨": "최상위권 변별력 킬러 문항 정복",
    "마더텅": "실전 기출 분석 및 시간 관리 훈련",
}


# 3. 성적 분석 및 테이블 데이터 변환 함수 정의
def easy_hard(old, grade):
  print("\n" + "=" * 46)
  print("\n[결과 출력 화면]")

  # 40점 이하 조건 처리
  if grade <= 40:
    print("\n예전 개념부터 복습하고 나서 풀어보세요.")
    print("\n총 난이도=> 기초 복습 필요")
    return

  # 60점, 80점, 100점 이하 조건 분기
  if grade <= 60:
    level = "하"
    target_list = easy_problem
  elif grade <= 80:
    level = "중"
    target_list = middle_problem
  elif grade <= 100:
    level = "상"
    target_list = hard_problem
  else:
    print("\n점수는 0~100 사이로 입력해주세요.")
    return

  # [핵심] for 반복문으로 교육 자료 리스트를 순회하며 테이블 생성용 데이터(2차원 리스트)로 변환
  table_data = []
  for book in target_list:
    row = [book, reasons[book]]
    table_data.append(row)

  # 변환된 테이블 데이터를 순회하여 출력
  print("\n당신에게 추천하는 교육 자료입니다.\n")
  print(f"{'추천하는 교육 자료 목록 = ':<24} +------------+----------------------------------+")
  print(f"{'':<24} | {'교육 자료':<8} | {'추천 이유':<30} |")
  print(f"{'':<24} +------------+----------------------------------+")

  for row in table_data:
    book_name = row[0]
    book_reason = row[1]
    print(f"{'':<24} | {book_name:<8} | {book_reason:<30} |")

  print(f"{'':<24} +------------+----------------------------------+")
  print(f"\n총 난이도=> {level}")


# 4. 함수 실행
easy_hard(old, grade)
