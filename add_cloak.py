import streamlit as st
from database import add_cloak_room

def create_cloak_room():
    duration = st.slider("Enter the number of months :",1,6)
    srn = st.text_input("Enter SRN :")
        
    if st.button("Add cloak_room"):
        add_cloak_room(duration,srn)
        st.success("Added cloak_room details for : {}".format(srn))