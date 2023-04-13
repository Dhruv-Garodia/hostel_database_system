import streamlit as st
from database import add_hostel_data
import mysql.connector
from mysql.connector import errorcode

def create_hostel():
    col1, col2 = st.columns(2)
    with col1:
        hostel_id = st.slider("Block number :",1,10)
        hostel_name = st.text_input("Enter your Block name :")
        manager_name = st.text_input("Enter the hostel block managers name :")
        
    with col2:
        no_of_rooms = st.number_input("Enter the number of rooms in the block :")
        no_of_students = st.number_input("Enter the students occupancy :")
            
    if st.button("Add Hostel"):
        try:
            add_hostel_data(hostel_id,hostel_name,no_of_rooms,no_of_students,manager_name)
            st.success("Added hostel record : {}".format(hostel_id))
        except mysql.connector.Error as err:
            st.error(err)
        finally:
            print("The hostel number should be between 1 to 6")