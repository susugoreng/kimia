import streamlit as st

st.title("GAMES KIMIA🧪")
st.write(
    "Selamat datang di games kimia."
)

# Load soal dari file JSON
with open("questions.json", "r") as f:
    questions = json.load(f)

# State
if "score" not in st.session_state:
    st.session_state.score = 0
if "q_index" not in st.session_state:
    st.session_state.q_index = 0
if "answered" not in st.session_state:
    st.session_state.answered = False

st.title("Game Kuis Sederhana")

# Tampilkan pertanyaan
if st.session_state.q_index < len(questions):
    q = questions[st.session_state.q_index]
    st.subheader(f"Pertanyaan {st.session_state.q_index + 1}: {q['question']}")

    for choice in q["choices"]:
        if st.button(choice):
            if not st.session_state.answered:
                st.session_state.answered = True
                if choice == q["answer"]:
                    st.success("Benar!")
                    st.session_state.score += 1
                else:
                    st.error(f"Salah! Jawaban yang benar: {q['answer']}")

    if st.session_state.answered:
        if st.button("Pertanyaan Selanjutnya"):
            st.session_state.q_index += 1
            st.session_state.answered = False
else:
    st.success(f"Kuis selesai! Skor kamu: {st.session_state.score} dari {len(questions)}")
    if st.button("Main Lagi"):
        st.session_state.score = 0
        st.session_state.q_index = 0
        st.session_state.answered = False
