import pandas as pd
import streamlit as st
from database import view_all_visitors,delete_visitors_data
from delete_visitors import delete_visitors
from update_visitors import update_visitors


def view_visitors():
    result = view_all_visitors()
    # st.write(result)
    df = pd.DataFrame(result, columns=['visitor_id','fname','lname','date','in_time','out_time','mobile','srn'])
    with st.expander("View all Visitors : "):
        st.dataframe(df)

    #getting list of employees by their ids 
    ids = [i[0] for i in result]
    st.write(ids)
    selection = st.selectbox("Do you want to UPDATE or DELETE a record ?",['-','Delete','Update'])
    if selection == "Delete":
        delete_visitors(ids)

    if selection == "Update":
        update_visitors(ids)