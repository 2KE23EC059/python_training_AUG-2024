use mallesh_db;
select * from employees;

create table employees(id int primary key auto_increment, name varchar(50) not null, designation varchar(40) not null, technology varchar(30) not null, phone_num bigint unique, commission int, salary float default 0, years_of_exp int);
insert into employees(name,designation,technology,phone_num,commission,salary,years_of_exp)
values('mallesh','manager','python','9585366536',10000, '1025205',2);
insert into employees(name,designation,technology,phone_num,commission,salary,years_of_exp)
values('harish','manager','python','9585366585',100, '10256205',5);
insert into employees(name,designation,technology,phone_num,commission,salary,years_of_exp)
values('harish','teamleader','c','9585366585',100250, '1525221',3);
insert into employees(name,designation,technology,phone_num,commission,salary,years_of_exp)
values('aditya','manager','python','7959856412',100258, '10255910',25);
insert into employees(name,designation,technology,phone_num,commission,salary,years_of_exp)
values('mukund','teamleader','python','947895134',105165, '102562048',10);
insert into employees(name,designation,technology,phone_num,commission,salary,years_of_exp)
values('manoj','teamleader','java','7359715678',1055, '205845',3);
insert into employees(name,designation,technology,phone_num,commission,salary,years_of_exp)
values('anand','manager','python','2584661266',25, '10584445',5);
insert into employees(name,designation,technology,phone_num,commission,salary,years_of_exp)
values('harish','python','9585366585',100, '10256205');
insert into employees(name,designation,technology,phone_num,commission,salary,years_of_exp)
values('harish','manager',100, '10256205',5);
insert into employees(name,designation,technology,phone_num,commission,salary,years_of_exp)
values('manager','python','9585366585','10256205',5);
insert into employees(name,designation,technology,phone_num,commission,salary,years_of_exp)
values('mukund','teamleader','c++','9585358462',100512, '102055812',8);
insert into employees(name,designation,technology,phone_num,commission,salary,years_of_exp)
values('manager','python');
insert into employees(name,designation,technology,phone_num,commission,salary,years_of_exp)
values('manager','9585366585', '10256205',5)

