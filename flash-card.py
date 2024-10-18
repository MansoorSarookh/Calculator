import streamlit as st
import random

# Display creator's name at the top
st.title("Flashcard Study App")
st.write("**Created by Mansoor Sarookh**")

# Initialize session state for storing flashcards and progress tracking
if 'flashcards' not in st.session_state:
    st.session_state['flashcards'] = []
if 'current_question' not in st.session_state:
    st.session_state['current_question'] = None
if 'score' not in st.session_state:
    st.session_state['score'] = {'correct': 0, 'incorrect': 0}
if 'attempted' not in st.session_state:
    st.session_state['attempted'] = 0

# Function to add a flashcard
def add_flashcard(question, answer):
    st.session_state['flashcards'].append({'question': question, 'answer': answer})

# Function to pick a random question
def pick_random_question():
    if st.session_state['flashcards']:
        return random.choice(st.session_state['flashcards'])
    return None

# Function to reset the score
def reset_score():
    st.session_state['score'] = {'correct': 0, 'incorrect': 0}
    st.session_state['attempted'] = 0

# Adding a new flashcard
st.subheader("Add a New Flashcard")
question = st.text_input("Question")
answer = st.text_input("Answer")
if st.button("Add Flashcard"):
    if question and answer:
        add_flashcard(question, answer)
        st.success(f"Flashcard added: {question} - {answer}")
    else:
        st.error("Please enter both question and answer.")

# Display available flashcards
if st.session_state['flashcards']:
    st.subheader("Available Flashcards")
    for index, flashcard in enumerate(st.session_state['flashcards'], start=1):
        st.write(f"{index}. **Q:** {flashcard['question']} **A:** {flashcard['answer']}")
else:
    st.write("No flashcards available yet. Add some to start!")

# Quiz section
st.subheader("Flashcard Quiz")
if st.button("Start Quiz"):
    st.session_state['current_question'] = pick_random_question()

if st.session_state['current_question']:
    st.write(f"**Question:** {st.session_state['current_question']['question']}")
    if st.button("Show Answer"):
        st.write(f"**Answer:** {st.session_state['current_question']['answer']}")

    # Buttons to mark correct or incorrect
    if st.button("I Got it Right!"):
        st.session_state['score']['correct'] += 1
        st.session_state['attempted'] += 1
        st.session_state['current_question'] = pick_random_question()  # Load next question
    if st.button("I Got it Wrong!"):
        st.session_state['score']['incorrect'] += 1
        st.session_state['attempted'] += 1
        st.session_state['current_question'] = pick_random_question()  # Load next question

# Display quiz score
st.subheader("Quiz Score")
st.write(f"Correct Answers: {st.session_state['score']['correct']}")
st.write(f"Incorrect Answers: {st.session_state['score']['incorrect']}")
st.write(f"Total Attempts: {st.session_state['attempted']}")

# Reset quiz and score
if st.button("Reset Quiz"):
    reset_score()
    st.success("Quiz has been reset!")

# Display creator's name at the bottom
st.write("**Created by Mansoor Sarookh**")
