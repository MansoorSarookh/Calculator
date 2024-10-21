import streamlit as st
import pandas as pd
from datetime import date

# File to store project data
PROJECT_DATA_FILE = 'projects.csv'
st.title("Project Management Tool")
# Developer's signature
st.title("Developed By Mansoor Sarookh, CS Student at GPGC Swabi")

# Load project data
def load_projects():
    try:
        return pd.read_csv(PROJECT_DATA_FILE)
    except FileNotFoundError:
        return pd.DataFrame(columns=["Project Name", "Description", "Start Date", "End Date", "Priority", "Status"])

# Save project data
def save_projects(df):
    df.to_csv(PROJECT_DATA_FILE, index=False)

# Add new project function
def add_project():
    st.header("Add New Project")
    name = st.text_input("Project Name")
    description = st.text_area("Project Description")
    start_date = st.date_input("Start Date", date.today())
    end_date = st.date_input("End Date")
    priority = st.selectbox("Priority", ["Low", "Medium", "High"])
    
    if st.button("Create Project"):
        if name and description:
            new_project = pd.DataFrame({
                "Project Name": [name],
                "Description": [description],
                "Start Date": [start_date],
                "End Date": [end_date],
                "Priority": [priority],
                "Status": ["Uncompleted"]
            })
            
            df = load_projects()
            # Update this part to use pd.concat instead of append
            df = pd.concat([df, new_project], ignore_index=True)
            save_projects(df)
            st.success(f"Project '{name}' has been added!")
        else:
            st.error("Please fill in all fields")


# View all projects
def view_projects():
    st.header("Manage Your Projects")
    df = load_projects()

    if df.empty:
        st.info("No projects available. Add a new project to get started.")
    else:
        status_filter = st.selectbox("Filter by status", ["All", "Completed", "Uncompleted"])
        if status_filter != "All":
            df = df[df['Status'] == status_filter]
        
        for i, row in df.iterrows():
            st.subheader(f"{row['Project Name']}")
            st.text(f"Description: {row['Description']}")
            st.text(f"Start Date: {row['Start Date']}")
            st.text(f"End Date: {row['End Date']}")
            st.text(f"Priority: {row['Priority']}")
            st.text(f"Status: {row['Status']}")
            if row['Status'] == "Uncompleted":
                if st.button(f"Mark '{row['Project Name']}' as Completed", key=f"complete_{i}"):
                    df.at[i, 'Status'] = "Completed"
                    save_projects(df)
                    st.success(f"'{row['Project Name']}' marked as Completed")

# View deadlines and high-priority projects
def view_high_priority():
    st.header("Upcoming Deadlines & High Priority Projects")
    df = load_projects()

    if df.empty:
        st.info("No projects available.")
    else:
        today = date.today()
        upcoming_deadlines = df[df['End Date'] >= str(today)].sort_values('End Date')
        high_priority = upcoming_deadlines[upcoming_deadlines['Priority'] == 'High']

        if not high_priority.empty:
            st.subheader("High Priority Projects")
            for i, row in high_priority.iterrows():
                st.text(f"{row['Project Name']} - Deadline: {row['End Date']}")

        st.subheader("Upcoming Deadlines")
        for i, row in upcoming_deadlines.iterrows():
            st.text(f"{row['Project Name']} - Deadline: {row['End Date']}")

# Streamlit sidebar menu
menu = st.sidebar.selectbox("Menu", ["Add Project", "View Projects", "High Priority & Deadlines"])

if menu == "Add Project":
    add_project()
elif menu == "View Projects":
    view_projects()
elif menu == "High Priority & Deadlines":
    view_high_priority()
