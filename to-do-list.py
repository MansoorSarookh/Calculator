import streamlit as st

# Title of the app
st.title("📝 To-Do List App")

# Session state to store the to-do list
if 'tasks' not in st.session_state:
    st.session_state['tasks'] = []

# Add a new task
def add_task():
    new_task = st.session_state['new_task']
    if new_task:
        st.session_state['tasks'].append({'task': new_task, 'completed': False})
        st.session_state['new_task'] = ''  # Clear the input field

# Input for adding new tasks
st.text_input("Enter a new task", key='new_task', on_change=add_task)

# Display tasks with checkboxes
for index, task in enumerate(st.session_state['tasks']):
    col1, col2 = st.columns([0.1, 0.9])  # Columns for checkbox and task text
    completed = col1.checkbox("", value=task['completed'], key=f"task_{index}")
    
    if completed:
        col2.write(f"~~{task['task']}~~")  # Strikethrough for completed tasks
    else:
        col2.write(task['task'])
    
    # Update task completion status
    task['completed'] = completed

# Remove completed tasks
if st.button("Remove Completed Tasks"):
    st.session_state['tasks'] = [task for task in st.session_state['tasks'] if not task['completed']]

# Footer information
st.write("Developed with ❤️ using Streamlit")
