show tables;
desc student;
alter table student add primary key(rollno);
create table sturesult(sid int,marks int,grade varchar(10));
desc sturesult;
alter table sturesult add foreign key(sid) references student(rollno);

alter table student add check(rollno>=100);
show create table student;
alter table student drop check student_chk_1

