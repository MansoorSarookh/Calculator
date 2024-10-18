import streamlit as st
import pandas as pd

# Initialize session state for storing income, expenses, and transactions
if 'transactions' not in st.session_state:
    st.session_state['transactions'] = []

# Function to add transaction
def add_transaction(type, description, amount):
    st.session_state['transactions'].append({
        'Type': type,
        'Description': description,
        'Amount': amount
    })

# Function to calculate total balance
def calculate_balance():
    total_income = sum(item['Amount'] for item in st.session_state['transactions'] if item['Type'] == 'Income')
    total_expense = sum(item['Amount'] for item in st.session_state['transactions'] if item['Type'] == 'Expense')
    return total_income - total_expense

# Streamlit app layout
st.title("Personal Finance Tracker")
st.write("Track your income, expenses, and view your overall balance.")

# Input form for transactions
st.subheader("Add a New Transaction")
type = st.selectbox("Type", ["Income", "Expense"])
description = st.text_input("Description")
amount = st.number_input("Amount", min_value=0.0, step=0.01)

if st.button("Add Transaction"):
    if description and amount:
        add_transaction(type, description, amount)
        st.success(f"{type} of {amount} added successfully!")
    else:
        st.error("Please enter both a description and amount.")

# Display the balance
st.subheader("Current Balance")
balance = calculate_balance()
st.metric("Balance", f"${balance:.2f}")

# Show transactions history
st.subheader("Transaction History")
if st.session_state['transactions']:
    transactions_df = pd.DataFrame(st.session_state['transactions'])
    st.dataframe(transactions_df)
else:
    st.write("No transactions added yet.")

# Summary of income and expenses
if st.session_state['transactions']:
    st.subheader("Summary")
    total_income = sum(item['Amount'] for item in st.session_state['transactions'] if item['Type'] == 'Income')
    total_expense = sum(item['Amount'] for item in st.session_state['transactions'] if item['Type'] == 'Expense')
    
    col1, col2 = st.columns(2)
    col1.metric("Total Income", f"${total_income:.2f}")
    col2.metric("Total Expenses", f"${total_expense:.2f}")
