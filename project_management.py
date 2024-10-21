import streamlit as st
import pandas as pd
from datetime import date

# Developer's signature
st.title("Project Management Tool")
st.subheader("Developed by Mansoor Sarookh, CS Student")

# Initialize project data
if 'projects' not in st.session_state:
    st.session_state['projects'] = []

# Function to add a new project
def add_project():
    with st.form("Add Project"):
        project_name = st.text_input("Project Name")
        project_description = st.text_area("Project Description")
        start_date = st.date_input("Start Date", date.today())
        end_date = st.date_input("End Date", date.today())
        priority = st.selectbox("Priority", ['Low', 'Medium', 'High'])
        submit_button = st.form_submit_button(label="Create Project")

        if submit_button:
            new_project = {
                'name': project_name,
                'description': project_description,
                'start_date': start_date,
                'end_date': end_date,
                'priority': priority,
                'tasks': []
            }
            st.session_state['projects'].append(new_project)
            st.success(f"Project '{project_name}' created!")

# Function to add tasks to a specific project
def add_task(project):
    with st.form(f"Add Task to {project['name']}"):
        task_name = st.text_input("Task Name")
        task_description = st.text_area("Task Description")
        due_date = st.date_input("Due Date", date.today())
        status = st.selectbox("Status", ['To-Do', 'In Progress', 'Completed'])
        submit_button = st.form_submit_button(label="Add Task")

        if submit_button:
            new_task = {
                'task_name': task_name,
                'description': task_description,
                'due_date': due_date,
                'status': status
            }
            project['tasks'].append(new_task)
            st.success(f"Task '{task_name}' added to project '{project['name']}'!")

# Function to display project details and tasks
def display_project(project):
    st.write(f"**Project Name:** {project['name']}")
    st.write(f"**Description:** {project['description']}")
    st.write(f"**Start Date:** {project['start_date']}")
    st.write(f"**End Date:** {project['end_date']}")
    st.write(f"**Priority:** {project['priority']}")
    
    st.subheader("Tasks")
    if project['tasks']:
        for idx, task in enumerate(project['tasks']):
            st.write(f"- **Task {idx+1}:** {task['task_name']}")
            st.write(f"    - Description: {task['description']}")
            st.write(f"    - Due Date: {task['due_date']}")
            st.write(f"    - Status: {task['status']}")
    else:
        st.write("No tasks added yet.")
    
    add_task(project)

# Sidebar for project navigation
st.sidebar.title("Manage Your Projects")

# Add new project button
if st.sidebar.button("Add New Project"):
    add_project()

# List existing projects in the sidebar
if st.session_state['projects']:
    for project in st.session_state['projects']:
        if st.sidebar.button(project['name'], key=project['name']):
            display_project(project)
else:
    st.sidebar.write("No projects available. Add a new project to get started.")
