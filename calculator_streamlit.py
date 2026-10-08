import streamlit as st

# 앱 제목 설정
st.title("간단한 정수 계산기")

# 정수 및 연산자 입력
num1_str = st.text_input("첫 번째 숫자를 입력하세요")
op = st.text_input("연산자를 입력하세요 (+, -, *, /)")
num2_str = st.text_input("두 번째 숫자를 입력하세요")

# 입력값이 모두 작성되었을 때 계산 진행
if num1_str and op and num2_str:
    # 1. 지원하지 않는 연산자 체크
    if op not in ["+", "-", "*", "/"]:
        st.error("오류: 연산자는 +, -, *, / 만 입력 가능합니다.")
    else:
        try:
            # 2. 정수 변환 시도
            num1 = int(num1_str)
            num2 = int(num2_str)

            # 3. 연산 수행 및 0으로 나누기 예외 처리
            if op == "+":
                result = num1 + num2
            elif op == "-":
                result = num1 - num2
            elif op == "*":
                result = num1 * num2
            elif op == "/":
                if num2 == 0:
                    st.error("오류: 0으로 나눌 수 없습니다.")
                    st.stop()
                result = num1 / num2

            # 4. 결과 출력
            st.success(f"결과: {result}")

        except ValueError:
            # 정수로 변환 불가능한 값 처리
            st.error("오류: 올바른 정수를 입력해 주세요.")