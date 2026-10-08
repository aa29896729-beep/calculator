import random
import streamlit as st

st.title("🎲 로또 번호 생성기")

# 세션 상태 초기화 (최대 5개 세트 저장용)
if "lotto_sets" not in st.session_state:
    st.session_state.lotto_sets = []


# 로또 공 색상 스타일 지정 함수 (1~10: 노랑, 11~20: 파랑, 21~30: 빨강, 31~40: 회색, 41~45: 초록)
def get_ball_color(num):
    if num <= 10:
        return "#fbc02d", "#ffffff"  # 노란색 (배경, 글자)
    elif num <= 20:
        return "#1e88e5", "#ffffff"  # 파란색
    elif num <= 30:
        return "#e53935", "#ffffff"  # 빨간색
    elif num <= 40:
        return "#8e24aa", "#ffffff"  # 보라/회색계열
    else:
        return "#43a047", "#ffffff"  # 초록색


# [로또번호 생성] 버튼
if st.button("로또번호 생성"):
    # 1~45 중 중복 없이 6개 추출 후 정렬
    new_set = sorted(random.sample(range(1, 46), 6))

    # 세션에 저장된 세트가 5개 이상이면 가장 오래된 세트 삭제
    if len(st.session_state.lotto_sets) >= 5:
        st.session_state.lotto_sets.pop(0)

    # 새로운 세트 추가
    st.session_state.lotto_sets.append(new_set)

# 결과 출력 (마지막 줄/하단 영역)
if st.session_state.lotto_sets:
    st.markdown("---")
    st.subheader("추천 로또 번호")

    # 저장된 로또 번호 세트들을 순서대로 출력
    for idx, lotto in enumerate(st.session_state.lotto_sets, 1):
        cols = st.columns([1] + [1] * 6)

        # 세트 번호 표시
        with cols[0]:
            st.markdown(f"**{idx}회차:**")

        # 6개 공을 실제 색상과 형태로 표시
        for i, num in enumerate(lotto):
            bg_color, text_color = get_ball_color(num)
            with cols[i + 1]:
                st.markdown(
                    f"""
                    <div style="
                        background-color: {bg_color};
                        color: {text_color};
                        border-radius: 50%;
                        width: 40px;
                        height: 40px;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        font-weight: bold;
                        font-size: 16px;
                        margin: 0 auto;
                    ">
                        {num}
                    </div>
                    """,
                    unsafe_allow_html=True
                )