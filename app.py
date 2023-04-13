import streamlit as st
from home import home
from database import create_tables,proc,read_union,call_func,modify1,modify2,modify3
from r_entity import read_entity
from create import create
from custom import query
from join_agg import read_op


# from create import create
# from delete import delete
# from read_file import read
# from update import update

def main():
    st.title("Hostel Management System 🏡")
    st.subheader("DhruvJyotiGarodia - PES1UG20CS527")
    menu = ["Home","Add data","Student","Employee","Hostel","Visitors","Room","Cloak_Room","Custom Query","Procedure","Join with aggregate","Intersection","Function","Modify"]
    # menu = ["Home","Add data","Read"]
    choice = st.sidebar.selectbox("Menu",menu)
    create_tables()
    
    if choice == "Home":
        st.subheader("PESU Boys Hostel")
        home()
    
    if choice == "Add data":
        create()
    
    if choice == "Student":
        entity = "Student"
        read_entity(entity)

    if choice == "Employee":
        entity = "Employee"
        read_entity(entity)

    if choice == "Hostel":
        entity = "Hostel"
        read_entity(entity)

    if choice == "Visitors":
        entity = "Visitors"
        read_entity(entity)

    if choice == "Room":
        entity = "Room"
        read_entity(entity)

    if choice == "Cloak_Room":
        entity = "Cloak_Room"
        read_entity(entity)
    
    if choice == "Custom Query":
        query()
    
    if choice == "Procedure":
        if st.button("Press to calculate the age"):
            proc()
    
    if choice == "Join with aggregate":
        st.write("Press button to find the number of students in each hostel block :")
        if st.button("Press for output"):
            read_op()

    if choice == "Union":
        st.write("Finding the srns of those students who had visitors visiting them :")
        if(st.button("Find the srns")):
            read_union()
    
    if choice == "Function":
        st.write("Checking if a student had many visitors visiting them :")
        if(st.button("Message")):
            call_func()

    if choice == "Modify":
        st.write("Printing the modification : ")
        if(st.button("Check the modification")):
            modify1()
            modify2()
            modify3()


if __name__ == '__main__':
    main()