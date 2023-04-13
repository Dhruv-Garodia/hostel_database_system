import pandas as pd
import streamlit as st
from database import view_all_room,delete_room_data
from update_room import update_room
from delete_room import delete_room

def view_room():
    result = view_all_room()
    df = pd.DataFrame(result, columns=['room_no','attached_bathroom','sharing','laundary_cycle','furniture'])
    with st.expander("View all rooms : "):
        st.dataframe(df)

    #getting list of rooms by the room_number 
    room_nums = [i[0] for i in result]
    st.write(room_nums)
    selection = st.selectbox("Do you want to UPDATE or DELETE a record ?",['-','Delete','Update'])
    if selection == "Delete":
        delete_room(room_nums)

    if selection == "Update":
        update_room(result)
        