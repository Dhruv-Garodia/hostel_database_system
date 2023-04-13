import pandas as pd
import streamlit as st
import datetime
from database import update_student_data

def update_student(selected_srn):
    col1, col2 = st.columns(2)
    with col1:
            fname = st.text_input("Enter your First Name :")
            lname = st.text_input("Enter your Last Name :")
            dept = st.selectbox("Department enrolled in :",["CSE","ECE","EEE","MECH","CIVIL","BBA","B.COM"])
            yr = st.slider("year of study :",1,4)
            st.text("selected : {}".format(yr))
            room_no = st.text_input("Enter your room number :")

    with col2:
            mobile1 = st.number_input("Your mobile number :")
            mobile2 = st.number_input("Your parents mobile number : ")
            d = st.date_input("When's your birthday",min_value=datetime.date(1950,1,1),max_value=datetime.date.today())
            st.write('Your birthday is:', d)
            hostel_id = st.slider("Block number :",1,6)
            mess = st.selectbox("Selected mess :",["Food Court","Namdhari","Hostel Mess"])
    if st.button("Update student detail"):
            update_student_data(selected_srn,fname,lname,dept,yr,mobile1,mobile2,d,hostel_id,mess,room_no)
            st.success("Student record has been updated successfully")