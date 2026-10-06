use bhopal;
show tables;
drop table stu1;
drop table stu2;
create table stu1(rollno int,name varchar(10),class varchar(10));
create table stu2(sid int,marks int,result varchar(10));

insert into stu1 values(111, 'sakshi', 'btech');
insert into stu1 values(112, 'shrishti', 'mtech');
insert into stu1 values(113, 'ankita', 'mba');
insert into stu1 values(114, 'nida', 'bsc');
select * from stu2;

insert into stu2 values(111, 780, 'pass');
insert into stu2 values(112, 739, 'fail');
insert into stu2 values(115, 970, 'pass');
insert into stu2 values(116, 590, 'fail');
select * from stu2;

select stu1. rollno, stu1. name, stu1. class, stu2. sid, stu2. marks, stu2. result 
from stu1 inner join stu2 on(stu1. rollno=stu2. sid);

select A. rollno, A. name, A. class, B. sid, B. marks, B. result 
from stu1 A inner join stu2 B on(A. rollno= B. sid);

select A.rollno, A.name, A.class, B.sid, B.marks,B.result
from stu1 A inner join stu2 B on(A. rollno< B.sid);

select A.rollno, A.name, A.class, B.sid, B.marks, B.result
from  stu1 A inner join stu2 B on(A. rollno<=B. sid);

select A.rollno, A.name, A.class, B.sid, B.marks, B.result
from stu1 A left outer join stu2 B on(A. rollno= B. sid)
union
select A.rollno, name, A.class, B.sid, B.marks, B.result
from stu1 A right outer join stu2 B on(A. rollno= B.sid);

select A.rollno, A.name, A.class, B.sid, B.marks, B.result
from stu1 A left outer join stu2 B on(A.rollno=b.sid);