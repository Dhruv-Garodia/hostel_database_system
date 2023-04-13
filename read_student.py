import pandas as pd
import streamlit as st
from database import view_all_student,delete_student_data,update_student_data
from delete_student import delete_student
from update_student import update_student

def view_student():
    result = view_all_student()
    # st.write(result)
    df = pd.DataFrame(result, columns=['srn','fname','lname','dept','year','mobile1','mobile2','dob','hostel_id','mess','age','Room_no'])
    with st.expander("View all Students : "):
        st.dataframe(df)

    #getting list of students by their srn 

    # DELETION
    srns = [i[0] for i in result]
    st.write(srns)
    selection = st.selectbox("Do you want to UPDATE or DELETE a record ?",['-','Delete','Update'])
    if selection == "Delete":
        selected_srn = st.selectbox("Choose the SRN :",srns)
        st.warning("Do you want to delete ::{}".format(selected_srn))
        delete_student(selected_srn)

    # UPDATION
    if selection == "Update":
        selected_srn = st.selectbox("Choose the SRN :",srns)
        st.warning("Do you want to update ::{}".format(selected_srn))
        update_student(selected_srn)