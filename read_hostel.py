import pandas as pd
import streamlit as st
from database import view_all_hostel
from update_hostel import update_hostel
from delete_hostel import delete_hostel

def view_hostel():
    result = view_all_hostel()
    df = pd.DataFrame(result, columns=['hostel_id','hostel_name','no_of_rooms','no_of_students','manager_name'])
    with st.expander("View all hostels : "):
        st.dataframe(df)
    
    #getting list of hostel by their ids 

    # DELETION
    ids = [i[0] for i in result]
    st.write(ids)
    selection = st.selectbox("Do you want to UPDATE or DELETE a record ?",['-','Delete','Update'])
    if selection == "Delete":
        selected_id = st.selectbox("Choose the hostel_id :",ids)
        st.warning("Do you want to delete ::{}".format(selected_id))
        delete_hostel(selected_id)
    # UPDATION 
    if selection == "Update":
        selected_id = st.selectbox("Choose the hostel_id :",ids)
        st.warning("Do you want to update ::{}".format(selected_id))
        update_hostel(selected_id)
