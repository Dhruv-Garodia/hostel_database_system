-- select h.hostel_id,h.hostel_name,h.no_of_rooms,r.sharing from hostel as h inner join student as s on h.hostel_id=s.hostel_id inner join room as r on s.room_no=r.room_no;

-- -- no.of student in each room
-- select count(srn),room_no from student group by room_no;
-- -- no.of student in each block
-- select count(srn),hostel_id from student group by hostel_id;

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
