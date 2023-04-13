import pandas as pd
import streamlit as st
from database import update_room_data

def update_room(result):
    room_nums = [i[0] for i in result]
    selected_id = st.selectbox("Choose the room_number :",room_nums)
    st.warning("Do you want to delete ::{}".format(selected_id))
    
    # we want to store the data for each room number : 
    ind = room_nums.index(selected_id)
    attached_bathroom = [i[1] for i in result][ind]
    sharing = [i[2] for i in result][ind]
    laundary_cycle = [i[3] for i in result][ind]
    furniture =[i[4] for i in result][ind]

    # st.write(ind)
    # st.write(attached_bathroom)
    # st.write(sharing)
    # st.write(laundary_cycle)
    # st.write(furniture)

    choice = st.selectbox("Select what you want to update :",["Attached Bathrrom","Sharing","Laundary Cycle","Furniture"])
    
    if choice == "Attached Bathrrom":
        attached_bathroom = st.selectbox("Do you have an attached bathroom :",["Yes","No"])

    if choice == "Sharing":
        sharing = st.slider("No.of students in a room :",1,3)
    
    if choice == "Laundary Cycle":
        laundary_cycle = st.selectbox("Select your laundary days :",["Mon-Thurs","Tues-Fri","Wed-Sat"])
    
    if choice == "Furniture":
        furniture = st.selectbox("Quality of furniture :",["Good","Need maintenance"])

    if st.button("Update room detials"):
        update_room_data(selected_id,attached_bathroom,sharing,laundary_cycle,furniture)
        st.success("Updated details for room number : {}".format(selected_id))