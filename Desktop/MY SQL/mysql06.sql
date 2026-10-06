use xyz;
show tables;
drop table emp;
create table emp(empno int, name varchar(10), dept varchar(10), doj date, salary int(10));
insert into emp values(101, 'raju', 'admin', '2020-12-23', 24000);
insert into emp values(102, 'sanju', 'hr', '2018-01-24', 30000);
insert into emp values(103, 'manoj', 'account', '2025-08-01', 50000);
insert into emp values(104, 'ritika', 'sales', '2026-07-05', 12000);
insert into emp values(105, 'mohit', 'admin', '2012-05-06', 80000);
insert into emp values(106, 'rohit', 'hr', '2023-09-14', 54000);
insert into emp values(107, 'sakshi', 'sales', '2017-04-03', 23000);
insert into emp values(108, 'ashok', 'account', '2016-01-10', 67000);

select*from emp where doj='2018-01-24';
select*from emp where doj>='2018-01-24';
select*from emp where doj<'2026-07-05';
select year(doj) from emp;
select*from emp where year(doj)='2025';
select*from emp where doj between '2020-01-01' and '2025-12-31';

select adddate(current_date, interval -10 day);
select adddate(current_date, interval 10 day);
select adddate(current_date, interval 3 week);
select adddate(current_date, interval -3 week);
select adddate(current_date, interval 4 month);
select adddate(current_date, interval -4 month);
select adddate(current_date, interval 2 year);
select adddate(current_date, interval -2 year);

select*from emp where doj> adddate(current_date, interval -1 year);