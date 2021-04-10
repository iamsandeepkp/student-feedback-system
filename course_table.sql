create table course_table(
roll varchar(8),
course_code varchar(6),
sem int(1),
sem_year int(4),
primary key (course_code)
);

insert into course_table values('CSM17024','CS505',2,2018);

commit;