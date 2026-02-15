import streamlit as st
import json 


with open("questions.json", "r") as f:
    all_questions = json.load(f)

st.title("🎯 Quiz Game")
st.write("Test your knowledge across different categories!")

if "category" not in st.session_state:
    st.session_state.category = None

if "score" not in st.session_state:
    st.session_state.score = 0 

if "questions_index" not in st.session_state:
    st.session_state.questions_index = 0

if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False

if "answered" not in st.session_state:
    st.session_state.answered = False

if not st.session_state.quiz_started:
    
    st.subheader("Choose a category:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🌍 Capitals", use_container_width=True):
            st.session_state.category = "capitals"
            st.session_state.quiz_started = True
            st.rerun()
        
        if st.button("💰 Currencies", use_container_width=True):
            st.session_state.category = "currencies"
            st.session_state.quiz_started = True
            st.rerun()
    
    with col2:
        if st.button("👑 Presidents", use_container_width=True):
            st.session_state.category = "presidents"
            st.session_state.quiz_started = True
            st.rerun()
        
        if st.button("📜 History", use_container_width=True):
            st.session_state.category = "history"
            st.session_state.quiz_started = True
            st.rerun()


elif st.session_state.quiz_started:
    questions = all_questions[st.session_state.category]
    
    
    if st.session_state.questions_index < len(questions):
        
        st.progress((st.session_state.questions_index) / len(questions))
        st.write(f"Question {st.session_state.questions_index + 1} of {len(questions)}")
        
        
        q = questions[st.session_state.questions_index]
        
        
        st.subheader(f"❓ {q['question']}")
        
        questions_with_placeholder = ["Select an answer..."] + q["options"]
        selected_option = st.radio(
            "Choose your answer:",
            questions_with_placeholder,
            key=f"q_{st.session_state.questions_index}"
        )
        
        
        if st.button("Submit Answer"):
            if selected_option == "Select an answer...":
                st.warning("⚠️ Please select an answer first!")
            elif not st.session_state.answered:
                if selected_option == q["answer"]:
                    st.success("✅ Correct!")
                    st.session_state.score +=1 
                else:
                    st.error(f"❌ Wrong! The correct answer was: {q['answer']}")
                
                st.session_state.answered = True
        
        
        if st.session_state.answered:
            if st.button("Next Question ➡️"):
                st.session_state.questions_index += 1
                st.session_state.answered = False
                st.rerun()
    
    else:
        
        st.balloons()
        st.success("🎉 Quiz Finished!")
        
        
        percentage = (st.session_state.score / len(questions)) * 100
        
        
        st.subheader(f"Final Score: {st.session_state.score}/{len(questions)}")
        st.write(f"Percentage: {percentage:.1f}%")
        
        
        if percentage >= 80:
            st.success("🏆 Excellent! You're a genius!")
        elif percentage >= 60:
            st.info("👍 Good job! Keep learning!")
        else:
            st.warning("📚 Keep studying! You'll do better next time!")
        
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔄 Restart Same Category"):
                st.session_state.score = 0
                st.session_state.questions_index = 0
                st.session_state.answered = False
                st.rerun()
        
        with col2:
            if st.button("🏠 Back to Categories"):
                st.session_state.category = None
                st.session_state.score = 0
                st.session_state.questions_index = 0
                st.session_state.quiz_started = False
                st.session_state.answered = False
                st.rerun()




