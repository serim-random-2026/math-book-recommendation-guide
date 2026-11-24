import pandas as pd
import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="성적 분석 및 교재 추천", page_icon="📚")
st.title("📚 맞춤형 교육 자료 추천 프로그램")

# ---------------------------------------------------------
# 1. [입력 화면] input() -> Streamlit 입력 위젯으로 변경
# ---------------------------------------------------------
st.subheader("1. 현재 학년 및 학기 선택")
col1, col2 = st.columns(2)
with col1:
  year = st.selectbox("학년 선택", ["1학년", "2학년", "3학년"])
with col2:
  semester = st.selectbox("학기 선택", ["1학기", "2학기"])

old = f"{year} {semester}"

st.subheader("2. 최근 지필 성적 입력")
grade = st.number_input(
    "점수 입력 (0 ~ 100점)", min_value=0, max_value=100, value=75, step=1
)

# ---------------------------------------------------------
# 2. 난이도별 추천 교육 자료 리스트 & 추천 이유 매칭
# ---------------------------------------------------------
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


# ---------------------------------------------------------
# 3. 성적 분석 및 테이블 출력 함수 정의
# ---------------------------------------------------------
def easy_hard(old, grade):
  st.divider()
  st.subheader(f"📊 분석 결과 ({old} / {grade}점)")

  # 40점 이하 조건 처리
  if grade <= 40:
    st.warning("예전 개념부터 복습하고 나서 풀어보세요.")
    st.info("**총 난이도 => 기초 복습 필요**")
    return

  # 60점, 80점, 100점 이하 조건 분기
  if grade <= 60:
    level = "하"
    target_list = easy_problem
  elif grade <= 80:
    level = "중"
    target_list = middle_problem
  else:
    level = "상"
    target_list = hard_problem

  # 2차원 리스트 생성 후 데이터프레임으로 변환하여 깔끔한 웹 표로 출력
  table_data = [[book, reasons[book]] for book in target_list]
  df = pd.DataFrame(table_data, columns=["교육 자료", "추천 이유"])

  st.write("당신에게 추천하는 교육 자료입니다.")
  st.table(df)
  st.success(f"**총 난이도 => {level}**")


# ---------------------------------------------------------
# 4. [버튼; 분석하기] 클릭 시 함수 실행
# ---------------------------------------------------------
if st.button("분석하기", type="primary", use_container_width=True):
  easy_hard(old, grade)
