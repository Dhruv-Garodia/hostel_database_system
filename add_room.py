import streamlit as st
from database import add_room_data

def create_room():
    col1, col2 = st.columns(2)
    with col1:
        room_no = st.text_input("Enter room no. :")
        attached_bathroom = st.selectbox("Do you have an attached bathroom :",["Yes","No"])
        sharing = st.slider("No.of students in a room :",1,3)

    with col2:
        laundary_cycle = st.selectbox("Select your laundary days :",["Mon-Thurs","Tues-Fri","Wed-Sat"])
        furniture = st.selectbox("Quality of furniture :",["Good","Need maintenance"])
    
    if st.button("Add room"):
        add_room_data(room_no,attached_bathroom,sharing,laundary_cycle,furniture)
        st.success("Added details for room number : {}".format(room_no))