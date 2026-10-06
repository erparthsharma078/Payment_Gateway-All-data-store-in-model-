use ritika;
select*from employee;

select date_format('2005-10-23', '%d%m%y');
select date_format('2005-10-23', '%d%m%Y');
select date_format('2005-10-23', '%D%m%y');
select date_format('2005-10-23', '%d , %M- %y');
select date_format('2005-10-23', '%a %D - %M - %Y');
select name, dept, date_format(doj, '%d/%m/%Y')from employee;


drop table employee;
create table employee(empno int primary key auto_increment,name varchar(10), city varchar(10));
insert into employee(name,city) values('raju', 'bhopal');
insert into employee(name,city) values('sonu', 'indore');
insert into employee(name,city) values('monu', 'mandideep');
select*from employee;
alter table employee auto_increment=101
insert into employee(name,city) values('seema', 'bhopal');
insert into employee(name,city) values('suresh', 'indore');
insert into employee(name,city) values('sanju', 'bhopal'); 

select*from employees;
select*from employee limit 3;
select*from employee limit 15;
select*from employee limit 4,3;
select*from employee limit 3,2; 
use sk;
show tables;
select*from employees order by salary desc limit 1;
select*from employees order by salary desc limit 0,1;
select*from employees order by salary desc limit 1,1;