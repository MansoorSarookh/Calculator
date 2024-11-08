import streamlit as st
import pandas as pd
from datetime import datetime

# Initialize session state for storing habits and progress
if 'habits' not in st.session_state:
    st.session_state['habits'] = []
if 'progress' not in st.session_state:
    st.session_state['progress'] = {}

# Function to add a habit
def add_habit(habit_name):
    if habit_name not in st.session_state['habits']:
        st.session_state['habits'].append(habit_name)
        st.session_state['progress'][habit_name] = []
    else:
        st.warning("Habit already exists!", icon="⚠️")

# Function to mark habit as completed for today
def complete_habit(habit_name):
    today = datetime.today().strftime('%Y-%m-%d')
    if today not in st.session_state['progress'][habit_name]:
        st.session_state['progress'][habit_name].append(today)
    else:
        st.warning("You've already completed this habit today!", icon="⚠️")

# Streamlit app layout with custom styling
st.set_page_config(page_title="Habit Tracker", page_icon="📅", layout="wide")

# Custom CSS to improve the UI
st.markdown("""
    <style>
        body {
            background-color: #6a1b9a;  /* Purple background color */
            font-family: 'Arial', sans-serif;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            border-radius: 8px;
            padding: 10px 20px;
            margin: 5px;
            border: none;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .stTextInput>div>input {
            font-size: 16px;
            padding: 10px;
            border-radius: 8px;
            border: 1px solid #ddd;
        }
        .stDataFrame {
            border-radius: 8px;
            background-color: white;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .stSubheader {
            color: #ffffff; /* White color for subheaders to stand out on purple background */
        }
        .stTitle {
            color: #ffffff; /* White color for title */
        }
    </style>
""", unsafe_allow_html=True)

# Streamlit app layout
st.title("Habit Tracker 📅")
st.write("Track your daily habits and monitor your progress. Stay consistent, stay productive!")
st.write("**Created by Mansoor Sarookh**")

# Input form for new habit
st.subheader("Add a New Habit")
habit_name = st.text_input("Habit Name", placeholder="e.g., Drink 8 glasses of water")
if st.button("Add Habit"):
    if habit_name:
        add_habit(habit_name)
        st.success(f"Habit '{habit_name}' added!", icon="✅")
    else:
        st.error("Please enter a habit name.", icon="❌")

# Display current habits
st.subheader("Your Habits")
if st.session_state['habits']:
    for habit in st.session_state['habits']:
        st.write(f"**{habit}**")
        if st.button(f"Mark '{habit}' as Completed Today"):
            complete_habit(habit)

# Show progress for each habit
st.subheader("Progress")
if st.session_state['habits']:
    progress_data = {}
    for habit in st.session_state['habits']:
        progress_data[habit] = len(st.session_state['progress'][habit])

    if progress_data:
        progress_df = pd.DataFrame(list(progress_data.items()), columns=['Habit', 'Days Completed'])
        st.dataframe(progress_df)
    else:
        st.write("No progress made yet.")
else:
    st.write("No habits added yet.")

# Overall Summary
st.subheader("Overall Summary")
if st.session_state['habits']:
    total_habits = len(st.session_state['habits'])
    total_completed = sum(len(st.session_state['progress'][habit]) for habit in st.session_state['habits'])
    st.write(f"Total Habits: **{total_habits}**")
    st.write(f"Total Days Completed Across All Habits: **{total_completed}**")
else:
    st.write("No habits tracked yet.")
