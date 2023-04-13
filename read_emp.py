import pandas as pd
import streamlit as st
from database import view_all_employee
from update_emp import update_emp
from delete_emp import delete_emp

def view_emp():
    result = view_all_employee()
    df = pd.DataFrame(result, columns=['id','fname','lname','salary','mobile','address','super_id','hostel_id'])
    with st.expander("View all Employees : "):
        st.dataframe(df)

    #getting list of employees by their ids 
    ids = [i[0] for i in result]
    st.write(ids)
    selection = st.selectbox("Do you want to UPDATE or DELETE a record ?",['-','Delete','Update'])
    if selection == "Delete":
            delete_emp(ids)

    if selection == "Update":
        update_emp(ids)
            