import pandas as pd
import streamlit as st
from database import delete_room_data

def delete_room(room_nums):
    selected_id = st.selectbox("Choose the room_number :",room_nums)
    st.warning("Do you want to delete ::{}".format(selected_id))

    if st.button("Delete room detail"):
        delete_room_data(selected_id)
        st.success("Room has been deleted successfully")