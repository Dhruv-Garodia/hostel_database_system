import pandas as pd
import streamlit as st
from database import view_all_cloak,delete_cloak_room
from delete_cloak import delete_cloak
from update_cloak import update_cloak

def view_cloak_room():
    result = view_all_cloak()
    df = pd.DataFrame(result, columns=['duration','srn'])
    with st.expander("View all booked Cloak rooms : "):
        st.dataframe(df)

    #getting list of rooms by the room_number 
    srns = [i[1] for i in result]
    st.write(srns)
    selection = st.selectbox("Do you want to UPDATE or DELETE a record ?",['-','Delete','Update'])
    if selection == "Delete":
        delete_cloak(srns)

    if selection == "Update":
        update_cloak(srns)

