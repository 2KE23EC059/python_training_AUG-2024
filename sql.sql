create table IF NOT EXISTS persons (id int primary key auto_increment,name varchar(50) not null, gender varchar(2),location varchar(50),age int check(age > 0));

select * from persons;
insert into persons(name,gender,location,age)
 values('nithin','m','mysuru',10
insert into persons(name,gender,location,age)
 values('mallesh','m','mysuru',19);
insert into persons(name,gender,location,age)
 values('nithin','m','mysuru',25);
insert into persons(name,,location,age)
 values('nithin','mysuru',0);
insert into persons(name,gender,location,age)
 values('harish','m','mysuru',10);
insert into persons(name,gender,location,age)
 values('om','m','mysuru',0);
insert into persons(name,gender,location,age)
 values('jash','m','mysuru',45);
insert into persons(name,age)
 values('nithin',10);
insert into persons(name,gender,location,age)
 values('ahrsish','m','hubli',10);
insert into persons(name,gender,location,age)
 values('nithin','m','mysuru',10);
insert into persons(name,gender,location,age)
 values('hrusikesh','m','hybli',18);
insert into persons(name,gender,location,age)
 values('neha','f','mysuru',88);
insert into persons(name,gender,location,age)
 values('anand','m','hubli',20);
insert into persons(name,gender,location,age)
 values('nootan','m','mysuru',10);
insert into persons(name,gender,location,age)
 values('laxmi','f','hubli',28);
insert into persons(name,location)
 values('neha','mysuru');

select * from persons where age < 18;
select * from persons where location = 'hubli';
select * from persons where name like 'a__a';
select * from persons where name like 'a__s';
select * from persons where name like 'a%a';
select * from persons where name like 'a%';
select * from persons where location in ('hubli','belagavi','dharwad');
