import streamlit as st
from database import add_employee_data

def create_employee():
    col1, col2 = st.columns(2)
    with col1:
        id = st.text_input("Enter employee id :")
        fname = st.text_input("Enter your First Name :")
        lname = st.text_input("Enter your Last Name :")
        salary = st.number_input("Enter you Salary :")

    with col2:
        mobile = st.number_input("Enter your mobile number :")
        address = st.text_input("Your address :")
        super = st.text_input("Enter your supervisors id :")
        hostel_id = st.slider("Block number :",1,6)

    if st.button("Add employee"):
        add_employee_data(id,fname,lname,salary,mobile,address,super,hostel_id)
        st.success("Added employee record : {}".format(id))