import streamlit as st
from gemini_helper import ask_gemini
from prompts import get_prompt
from gemini_helper import ask_gemini, extract_json

# Page settings (must be the first Streamlit command)
st.set_page_config(page_title="AI Study Assistant", page_icon="📚", layout="centered")
st.title("📚 AI Study Assistant")
st.caption("Explanations • Notes • Quizzes — powered by Gemini")
with st.sidebar:
    st.header("About")
    st.write(
        "An AI-powered study tool that generate concept explanations, "
        "structured notes, and quizzes using the Gemini API."
    )
    st.write("Built with Python, Streamlit, and Google Gemini.")
    st.caption("Made by Sravani Goli — github.com/GoliSravani0306")
st.write("Generate explanations, notes, and quizzes with AI.")

# Three tabs, one per feature
tab_explain, tab_notes, tab_quiz = st.tabs(["💡 Explain", "📝 Notes", "❓ Quiz"])

# ---------- Tab 1: Concept Explanation ----------
with tab_explain:
    st.subheader("Concept Explanation")

    topic = st.text_input("What concept do you want explained?", key="explain_topic")
    level = st.selectbox(
        "Choose your level",
        ["beginner", "intermediate", "advanced"],
        key="explain_level",
    )

    if st.button("Explain", key="explain_button"):
        if topic.strip() == "":
            st.warning("Please enter a concept first.")
        else:
            with st.spinner("Thinking..."):
                try:
                    prompt = get_prompt("explain", topic=topic, level=level)
                    answer = ask_gemini(prompt)
                    st.markdown(answer)
                except Exception as e:
                    st.error(f"Something went wrong: {e}")

# ---------- Tab 2: Notes (coming next) ----------
# ---------- Tab 2: Notes Generation ----------
with tab_notes:
    st.subheader("Notes Generation")

    pasted_text = st.text_area(
        "Paste the text you want notes from",
        height=200,
        key="notes_text",
    )
    uploaded_file = st.file_uploader(
        "...or upload a .txt file", type=["txt"], key="notes_file"
    )

    if st.button("Generate Notes", key="notes_button"):
        # If a file was uploaded, use its content; otherwise use the pasted text
        if uploaded_file is not None:
            source_text = uploaded_file.read().decode("utf-8")
        else:
            source_text = pasted_text

        if source_text.strip() == "":
            st.warning("Please paste some text or upload a file first.")
        else:
            with st.spinner("Writing your notes..."):
                try:
                    prompt = get_prompt("notes", text=source_text)
                    st.session_state["notes_result"] = ask_gemini(prompt)
                except Exception as e:
                    st.error(f"Something went wrong: {e}")

    # Show the saved result (if any) so it survives re-runs
    if "notes_result" in st.session_state:
        st.markdown(st.session_state["notes_result"])
        st.download_button(
            "Download notes",
            data=st.session_state["notes_result"],
            file_name="study_notes.txt",
            key="notes_download",
        )

# ---------- Tab 3: Quiz (coming later) ----------
# ---------- Tab 3: Quiz Generation ----------
with tab_quiz:
    st.subheader("Quiz Generation")

    quiz_topic = st.text_input("What topic should the quiz be about?", key="quiz_topic")
    num_questions = st.slider("Number of questions", 1, 10, 3, key="quiz_num")

    if st.button("Generate Quiz", key="quiz_button"):
        if quiz_topic.strip() == "":
            st.warning("Please enter a topic first.")
        else:
            with st.spinner("Writing your quiz..."):
                try:
                    prompt = get_prompt("quiz", topic=quiz_topic, num_questions=num_questions)
                    raw_response = ask_gemini(prompt)
                    questions = extract_json(raw_response)
                    st.session_state["quiz_questions"] = questions
                    st.session_state["quiz_submitted"] = False
                except Exception as e:
                    st.error(f"Something went wrong: {e}")

    # Show the quiz if one has been generated
    if "quiz_questions" in st.session_state:
        st.divider()
        user_answers = {}

        for i, q in enumerate(st.session_state["quiz_questions"]):
            st.write(f"**Q{i + 1}. {q['question']}**")
            user_answers[i] = st.radio(
                "Choose one:",
                q["options"],
                key=f"quiz_q{i}",
                index=None,
                label_visibility="collapsed",
            )

        if st.button("Submit Quiz", key="quiz_submit"):
            st.session_state["quiz_submitted"] = True

        if st.session_state.get("quiz_submitted"):
            st.divider()
            score = 0
            for i, q in enumerate(st.session_state["quiz_questions"]):
                if user_answers[i] == q["answer"]:
                    st.success(f"Q{i + 1}: Correct! {q['explanation']}")
                    score += 1
                else:
                    st.error(
                        f"Q{i + 1}: Incorrect. Correct answer: {q['answer']}. {q['explanation']}"
                    )
            st.write(f"### Score: {score} / {len(st.session_state['quiz_questions'])}")
            # ---------- Footer ----------
# ---------- Footer ----------
st.divider()
st.markdown(
    """
    <div style="text-align: center; color: gray; font-size: 0.9em;">
        <div>Made by Sravani Goli</div>
        <div style="margin-top: 6px;">
            <a href="https://github.com/YOUR_USERNAME" target="_blank" style="margin: 0 8px; text-decoration: none;">
                🐙 GitHub
            </a>
            <a href="https://linkedin.com/in/YOUR_LINKEDIN" target="_blank" style="margin: 0 8px; text-decoration: none;">
                💼 LinkedIn
            </a>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)