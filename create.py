import streamlit as st
from add_student import create_student
from add_employee import create_employee
from add_hostel import create_hostel
from add_visitors import create_visitors
from add_room import create_room
from add_cloak import create_cloak_room


def create():
    menu = ["Student","Employee","Hostel","Visitors","Room","Cloak_Room"]
    choice = st.selectbox("Choose the entity",menu)

    if choice == "Student":
        st.subheader("Add Student details")
        create_student()
    if choice == "Employee":
        st.subheader("Add Employee details")
        create_employee()
    if choice == "Hostel":
        st.subheader("Add Hostel details")
        create_hostel()
    if choice == "Visitors":
        st.subheader("Add Visitors details")
        create_visitors()
    if choice == "Room":
        st.subheader("Add Room details")
        create_room()
    if choice == "Cloak_Room":
        st.subheader("Add Cloak_Room details")
        create_cloak_room()
    