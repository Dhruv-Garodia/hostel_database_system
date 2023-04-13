import pandas as pd
import streamlit as st
from database import delete_student_data

def delete_student(selected_srn):
    if st.button("Delete student detail"):
        delete_student_data(selected_srn)
        st.success("Student record has been deleted successfully")