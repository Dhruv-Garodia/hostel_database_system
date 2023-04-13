import pandas as pd
import streamlit as st
from database import update_employee_data

def update_emp(ids):
    selected_id = st.selectbox("Choose the employee id :",ids)
    st.warning("Do you want to delete ::{}".format(selected_id))
    col1, col2 = st.columns(2)
    with col1:
        fname = st.text_input("Enter your First Name :")
        lname = st.text_input("Enter your Last Name :")
        salary = st.number_input("Enter you Salary :")

    with col2:
        mobile = st.number_input("Enter your mobile number :")
        address = st.text_input("Your address :")
        super = st.text_input("Enter your supervisors id :")
        hostel_id = st.slider("Block number :",1,6)

    if st.button("Update employee"):
        update_employee_data(selected_id,fname,lname,salary,mobile,address,super,hostel_id)
        st.success("Updated employee record : {}".format(id))