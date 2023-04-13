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