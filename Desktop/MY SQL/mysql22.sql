use miracle;
select char(80);

select concat("srishti" , "khaddar");
show tables;
select*from student;
select concat(name,"  ",city)from student;

select*from emp1;
select lower(name)from emp1;
select upper(name)from emp1;
select lcase(name)from emp1;
select ucase(name)from emp1;
select lcase("sHiVam");
select ucase("shivam");

select substring("shrishti khaddar",4,9);
select name,substr(name,3,4)from emp1;

select trim("     shrishti");
select("    shrishti");
insert into emp1 values(114,'  ravi', 'bhopal',54000);
select*from emp1;
select empno, trim(name) from emp1;

select length("shrishti");
select length(name)from emp1;
select name,length(name) from emp1;
