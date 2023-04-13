import pandas as pd
import streamlit as st
from read_hostel import view_hostel
from read_student import view_student
from read_visitors import view_visitors
from read_emp import view_emp
from read_room import view_room
from read_cloak_room import view_cloak_room

def read_entity(choice):
# def read_entity():
    # menu = ["Student","Employee","Hostel","Visitors","Room","Cloak_Room"]
    # choice = st.selectbox("Choose the entity",menu)

    if choice == "Student":
        st.subheader("View Student details")
        view_student()
    if choice == "Employee":
        st.subheader("View Employee details")
        view_emp()
    if choice == "Hostel":
        st.subheader("View Hostel details")
        view_hostel()
    if choice == "Visitors":
        st.subheader("View Visitors details")
        view_visitors()
    if choice == "Room":
        st.subheader("View Room details")
        view_room()
    if choice == "Cloak_Room":
        st.subheader("View Cloak_Room details")
        view_cloak_room()