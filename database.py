import streamlit as st
import pandas as pd
import mysql.connector

mydb = mysql.connector.connect(
user="root",
password="",
host="localhost",
port=8929,
database="hostel"
)
c = mydb.cursor(buffered=True)

# C - creating tables
def create_tables():
    c.execute('CREATE TABLE IF NOT EXISTS hostel(hostel_id int PRIMARY KEY,hostel_name varchar(30),no_of_rooms int NOT NULL,no_of_students int,manager_name varchar(50))')

    c.execute('CREATE TABLE IF NOT EXISTS employee(id varchar(20) PRIMARY KEY,fname varchar(30),lname varchar(30),salary int,mobile bigint,address varchar(100),super_id varchar(30),hostel_id int,FOREIGN KEY(super_id) REFERENCES employee(id), CONSTRAINT FK_EMP FOREIGN KEY(hostel_id) REFERENCES hostel(hostel_id) ON DELETE CASCADE)')

    c.execute('CREATE TABLE IF NOT EXISTS student(srn varchar(30) PRIMARY KEY,fname varchar(30),lname varchar(30),dept varchar(30),year int,mobile1 bigint NOT NULL,mobile2 bigint NOT NULL,dob date NOT NULL,age int,hostel_id int,mess varchar(20),room_no varchar(30), FOREIGN KEY(hostel_id) REFERENCES hostel(hostel_id), FOREIGN KEY(room_no) REFERENCES room(room_no))')

    c.execute('CREATE TABLE IF NOT EXISTS visitors(visitor_id varchar(30) PRIMARY KEY,fname varchar(30),lname varchar(30),date varchar(30),in_time varchar(20),out_time varchar(20),mobile bigint NOT NULL,srn varchar(30),FOREIGN KEY(srn) REFERENCES student(srn))')

    c.execute('CREATE TABLE IF NOT EXISTS room(room_no varchar(10) PRIMARY KEY, attached_bathroom varchar(5),sharing int,laundary_cycle varchar(20),furniture varchar(20))')

    c.execute('CREATE TABLE IF NOT EXISTS cloak_room(duration int NOT NULL,srn varchar(30),CONSTRAINT FK_CLK FOREIGN KEY(srn) REFERENCES student(srn) ON DELETE CASCADE)')

# execution of custom query
def custom_query(q):
    c.execute(q)
    data = c.fetchall()
    mydb.commit()
    return data

# adding data into tables

def add_student_data(srn,fname,lname,dept,yr,mobile1,mobile2,d,hostel_id,mess,room_no):

    c.execute('INSERT INTO student(srn,fname,lname,dept,year,mobile1,mobile2,dob,hostel_id,mess,room_no) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(srn,fname,lname,dept,yr,mobile1,mobile2,d,hostel_id,mess,room_no))
    mydb.commit()

def add_employee_data(id,fname,lname,salary,mobile,address,super,hostel_id):
    c.execute('INSERT INTO employee(id,fname,lname,salary,mobile,address,super_id,hostel_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)',(id,fname,lname,salary,mobile,address,super,hostel_id))
    mydb.commit()

def add_hostel_data(hostel_id,hostel_name,no_of_rooms,no_of_students,manager_name):
    c.execute('INSERT INTO hostel(hostel_id,hostel_name,no_of_rooms,no_of_students,manager_name) VALUES(%s,%s,%s,%s,%s)',(hostel_id,hostel_name,no_of_rooms,no_of_students,manager_name))
    mydb.commit()

def add_visitor_data(visitor_id,fname,lname,date,in_time,out_time,mobile,srn):
    c.execute('INSERT INTO visitors (visitor_id,fname,lname,date,in_time,out_time,mobile,srn) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',(visitor_id,fname,lname,date,in_time,out_time,mobile,srn) )
    mydb.commit()

def add_room_data(room_no,attached_bathroom,sharing,laundary_cycle,furniture):
    c.execute('INSERT INTO room(room_no,attached_bathroom,sharing,laundary_cycle,furniture) VALUES (%s,%s,%s,%s,%s)',(room_no,attached_bathroom,sharing,laundary_cycle,furniture) )
    mydb.commit()

def add_cloak_room(duration,srn):
    c.execute('INSERT INTO cloak_room(duration,srn) VALUES(%s,%s)',(duration,srn) )
    mydb.commit()

# R - reading data from the tables 
def view_all_hostel():
    c.execute('select * from hostel')
    data = c.fetchall()
    return data

def view_all_student():
    c.execute('select * from student')
    data = c.fetchall()
    return data

def view_all_employee():
    c.execute('select * from employee')
    data = c.fetchall()
    return data

def view_all_visitors():
    c.execute('select * from visitors')
    data = c.fetchall()
    return data

def view_all_room():
    c.execute('select * from room')
    data = c.fetchall()
    return data

def view_all_cloak():
    c.execute('select * from cloak_room')
    data = c.fetchall()
    return data

# U - update data/record entries
def update_student_data(srn,fname,lname,dept,yr,mobile1,mobile2,d,hostel_id,mess,room_no):
    c.execute('UPDATE student set fname=%s,lname=%s,dept=%s,year=%s,mobile1=%s,mobile2=%s,dob=%s,hostel_id=%s,mess=%s,room_no=%s where srn=%s',(fname,lname,dept,yr,mobile1,mobile2,d,hostel_id,mess,srn,room_no) )
    mydb.commit()

def update_hostel_data(hostel_name,manager_name,no_of_rooms,no_of_students,hostel_id):
    c.execute('UPDATE hostel set hostel_name=%s,no_of_rooms=%s,no_of_students=%s,manager_name=%s where hostel_id=%s',(hostel_name,no_of_rooms,no_of_students,manager_name,hostel_id))
    mydb.commit()

def update_employee_data(selected_id,fname,lname,salary,mobile,address,super,hostel_id):
    c.execute('UPDATE employee set fname=%s,lname=%s,salary=%s,mobile=%s,address=%s,super=%s,hostel_id=%s where id=selected_id',(fname,lname,salary,mobile,address,super,hostel_id,selected_id) )
    mydb.commit()

def update_visitor_data(visitor_id,fname,lname,date,in_time,out_time,mobile,srn):
    c.execute('UPDATE visitors set fname=%s,lname=%s,date=%s,in_time=%s,out_time=%s,mobile=%s,srn=%s where visitor_id=%s',(fname,lname,date,in_time,out_time,mobile,srn,visitor_id) )

def update_room_data(room_no,attached_bathroom,sharing,laundary_cycle,furniture):
    c.execute('UPDATE room set attached_bathroom=%s,sharing=%s,laundary_cycle=%s,furniture=%s where room_no=%s',(attached_bathroom,sharing,laundary_cycle,furniture,room_no) )
    mydb.commit()

def update_cloak_data(duration,srn):
    c.execute('UPDATE cloak_room set duration=%s where srn=%s',(duration,srn) )
    mydb.commit()

# D - delete records
def delete_hostel_data(hostel_id):
    c.execute('DELETE FROM hostel where hostel_id="{}"'.format(hostel_id))
    mydb.commit()

def delete_student_data(srn):
    c.execute('DELETE FROM student where srn="{}"'.format(srn))
    st.write("in delete")
    mydb.commit()
    st.write("in delete")

def delete_employee_data(id):
    c.execute('DELETE FROM employee where id="{}"'.format(id))
    mydb.commit()

def delete_visitors_data(id):
    c.execute('DELETE FROM student where visitor_id="{}"'.format(id))
    mydb.commit()

def delete_room_data(room_no):
    c.execute('DELETE FROM room where room_no="{}"'.format(room_no))
    mydb.commit()

def delete_cloak_room(srn):
    c.execute('DELETE FROM cloak_room where srn="{}"'.format(srn))
    mydb.commit()

# calling the procedure to update the age
def proc():
    c.execute('call calc()')
    mydb.commit()

def modify1():
    c.callproc('modify1')
    for result in c.stored_results():
        data = result.fetchall()
    df = pd.DataFrame(data,columns=['hostel_id','hostel_name','no_of_rooms','sharing'])
    st.write('show the no.of rooms in a block wrt block_id')
    st.dataframe(df)

def modify2():
    c.callproc('modify2')
    for result in c.stored_results():
        data = result.fetchall()
    df = pd.DataFrame(data,columns=['count(srn)','room_no'])
    st.write('no.of students in each room')
    st.dataframe(df)

def modify3():
    c.callproc('modify3')
    for result in c.stored_results():
        data = result.fetchall()
    df = pd.DataFrame(data,columns=['count(srn)','hostel_id'])
    st.write('no.of students in each block')
    st.dataframe(df)
    
# calling union function
def read_union():
    c.execute('select srn from student INTERSECT select srn from visitors')
    data = c.fetchall()
    df = pd.DataFrame(data, columns=['srn'])
    with st.expander("SRNS are : "):
        st.dataframe(df)

# calling aggregate and join function
def agg_j():
    c.execute('select count(s.srn),s.hostel_id from hostel as h inner join student as s where h.hostel_id=s.hostel_id group by s.hostel_id')
    data = c.fetchall()
    return data

# calling the function 
def call_func():
    c.execute('select count(srn) from visitors group by srn')
    data = c.fetchall()
    st.write(data[0][0])
    # df = pd.DataFrame(data, columns=['srn'])
    # st.write(df)
    # st.write(df)
    # st.write("op")
    c.execute('select count_visitors({})'.format(data[0][0]) )
    op = c.fetchall()
    # how to 
    st.write(op[0][0])