import pandas as pd
import streamlit as st
from database import delete_cloak_room

def delete_cloak(srns):
    selected_srn = st.selectbox("Choose the room_number :",srns)
    st.warning("Do you want to delete ::{}".format(srns))

    if st.button("Delete room detail"):
        delete_cloak_room(selected_srn)
        st.success("Room has been deleted successfully")