-- DBMS Semester project

-- PES1UG20CS527

-- creation of table

CREATE TABLE IF NOT EXISTS hostel(hostel_id int PRIMARY KEY,hostel_name varchar(30),no_of_rooms int NOT NULL,no_of_students int,manager_name varchar(50))

CREATE TABLE IF NOT EXISTS student(srn varchar(30) PRIMARY KEY,fname varchar(30),lname varchar(30),dept varchar(30),year int,mobile1 bigint NOT NULL,mobile2 bigint NOT NULL,dob date NOT NULL,age int,hostel_id int,mess varchar(20), FOREIGN KEY(hostel_id) REFERENCES hostel(hostel_id))

CREATE TABLE IF NOT EXISTS student(srn varchar(30) PRIMARY KEY,fname varchar(30),lname varchar(30),dept varchar(30),year int,mobile1 bigint NOT NULL,mobile2 bigint NOT NULL,dob date NOT NULL,age int,hostel_id int,mess varchar(20), FOREIGN KEY(hostel_id) REFERENCES hostel(hostel_id))

CREATE TABLE IF NOT EXISTS student(srn varchar(30) PRIMARY KEY,fname varchar(30),lname varchar(30),dept varchar(30),year int,mobile1 bigint NOT NULL,mobile2 bigint NOT NULL,dob date NOT NULL,age int,hostel_id int,mess varchar(20), FOREIGN KEY(hostel_id) REFERENCES hostel(hostel_id))

CREATE TABLE IF NOT EXISTS student(srn varchar(30) PRIMARY KEY,fname varchar(30),lname varchar(30),dept varchar(30),year int,mobile1 bigint NOT NULL,mobile2 bigint NOT NULL,dob date NOT NULL,age int,hostel_id int,mess varchar(20), FOREIGN KEY(hostel_id) REFERENCES hostel(hostel_id))

CREATE TABLE IF NOT EXISTS student(srn varchar(30) PRIMARY KEY,fname varchar(30),lname varchar(30),dept varchar(30),year int,mobile1 bigint NOT NULL,mobile2 bigint NOT NULL,dob date NOT NULL,age int,hostel_id int,mess varchar(20), FOREIGN KEY(hostel_id) REFERENCES hostel(hostel_id))


-- insertion into table

INSERT INTO student(srn,fname,lname,dept,year,mobile1,mobile2,dob,hostel_id,mess) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(srn,fname,lname,dept,yr,mobile1,mobile2,d,hostel_id,mess);

INSERT INTO employee(id,fname,lname,salary,mobile,address,super_id,hostel_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)',(id,fname,lname,salary,mobile,address,super,hostel_id);

INSERT INTO hostel(hostel_id,hostel_name,no_of_rooms,no_of_students,manager_name) VALUES(%s,%s,%s,%s,%s)',(hostel_id,hostel_name,no_of_rooms,no_of_students,manager_name);

INSERT INTO visitors (visitor_id,fname,lname,date,in_time,out_time,mobile,srn) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',(visitor_id,fname,lname,date,in_time,out_time,mobile,srn);

INSERT INTO room(room_no,attached_bathroom,sharing,laundary_cycle,furniture) VALUES (%s,%s,%s,%s,%s)',(room_no,attached_bathroom,sharing,laundary_cycle,furniture);

INSERT INTO cloak_room(duration,srn) VALUES(%s,%s)',(duration,srn)


-- join and set operations

select count(s.srn),s.hostel_id from hostel as h inner join student as s where h.hostel_id=s.hostel_id group by s.hostel_id

-- set operatoins

select count(s.srn),s.hostel_id from hostel as h inner join student as s where h.hostel_id=s.hostel_id group by s.hostel_id

-- adding procedure

DELIMITER $$
create procedure calc()
begin
declare todaydate DATE;
select current_date() into todaydate;
update student
set age=year(todaydate)-year(dob);
end $$
delimiter ;

-- adding function

DELIMITER $$
CREATE FUNCTION count_visitors(cnt int)
RETURNS varchar(500)
DETERMINISTIC
BEGIN
DECLARE op varchar(500);
set op = "test";
if (cnt>5) then
    SET op = "you had a lot of visitors visiting you.";
elseif (cnt>0) then
    SET op = "you had visitors visiting you.";
else
    SET op = "you had no visitors visiting you.";
end if;
return op;
END; $$ 
DELIMITER ;

-- adding trigger

delimiter $$
create trigger my_trigger
before insert
on hostel for each row 

begin
declare my_msg_error varchar(120); 
declare num int; 
SET my_msg_error = ('The hostel number should be between 1 to 6');

if (new.hostel_id )>6 then
SIGNAL SQLSTATE '45500'
set MESSAGE_TEXT = my_msg_error;
end if; 

end $$
delimiter ;

-- Codes for modifications asked 

DELIMITER $$
CREATE PROCEDURE modify1()
BEGIN
select h.hostel_id,h.hostel_name,h.no_of_rooms,r.sharing from hostel as h inner join student as s on h.hostel_id=s.hostel_id inner join room as r on s.room_no=r.room_no;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE modify2()
BEGIN
select count(srn),room_no from student group by room_no;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE modify3()
BEGIN
select count(srn),hostel_id from student group by hostel_id;
END $$
DELIMITER ;
