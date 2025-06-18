create database DailyTimeTable;
Drop database DailyTimeTable;
create database Daily_Time_Sheet_2025;
USE Daily_Time_Sheet_2025;
create table DailyTimeTable(
S_NO int not null auto_increment primary key,
START_TIME TIME not null unique,
END_TIME TIME not null unique,
TASK VARCHAR(50) NOT NULL,
HOURS_MINUTES TIME AS (SEC_TO_TIME(MOD(TIME_TO_SEC(END_TIME)+86400-TIME_TO_SEC(START_TIME),86400))) STORED,
LEVEL int default 0
);
describe DailyTimeTable;
drop table DailyTimeTable;
INSERT INTO DailyTimeTable (START_TIME,END_TIME,TASK)VALUES("22:00:00","22:30:00","TO DO LIST & JOURNALING & Motivation Reading");
INSERT INTO DailyTimeTable (START_TIME,END_TIME,TASK)VALUES
("22:30:00","23:00:00","BOOK READING"),("23:00:00","7:00:00","HAPPY SLEEP");
SELECT * FROM DailyTimeTable;
INSERT INTO DailyTimeTable (START_TIME, END_TIME, TASK) VALUES
('07:00:00', '07:30:00', 'MEDITATION'),
('07:30:00', '09:30:00', 'GYM_WORKOUT'),
('09:30:00', '10:00:00', 'BATHING'),
('10:00:00', '10:30:00', 'Tiffen-GetReady'),
('10:30:00', '11:30:00', 'COMMUNICATION'),
('11:30:00', '12:30:00', 'APTITUDE'),
('12:30:00', '14:30:00', 'MYSQL_HTML_CSS'),
('14:30:00', '15:00:00', 'LUNCH'),
('15:00:00', '21:00:00', 'PYTHON_JAVASCRIPT'),
('21:00:00', '22:00:00', 'Cooking-WarmBath-Dinner'),
('22:00:00', '22:30:00', 'TODO_JOURNAL_MOTIREAD'),
('22:30:00', '23:00:00', 'BOOK_READING'),
('23:00:00', '07:00:00', 'HAPPY-SLEEP');
update DailyTimeTable set level=1 where S_NO in(1,2,5,6,7,9,11,12);
update DailyTimeTable set level=1 where S_NO in(11,12);
select * from DailyTimeTable;
select date_format(START_TIME,"%l:%i %p") as Start,date_format(END_TIME,"%l:%i %p") as End,TASK,(
case
when hour(HOURS_MINUTES)=0 then concat(minute(HOURS_MINUTES),"M")
when minute(HOURS_MINUTES)=0 then concat(hour(HOURS_MINUTES)," HOUR",if (hour(HOURS_MINUTES)>1,"S",""))
else concat(hour(HOURS_MINUTES)," HOUR",if (hour(HOURS_MINUTES)>1,"S",""),minute(HOURS_MINUTES),"M")
end) as HOURS_MINUTES from DailyTimeTable;
DROP TABLE DailyTimeSheet;
create table DailyTimeSheet(
DAILY_DATE date PRIMARY KEY default (CURRENT_DATE),
DAILY_DAY varchar(3) generated always as (LEFT(DAYNAME(DAILY_DATE),3)) stored,
MEDITATION INT default 0,
GYM_WORKOUT int default 0,
COMMUNICATION int default 0,
APTITUDE int default 0,
MYSQL_HTML_CSS int default 0,
BLOCK_1 INT default 0,
BLOCK_2 int default 0,
BLOCK_3 int default 0,
PYTHON_JAVASCRIPT int generated always as ((BLOCK_1+BLOCK_2+BLOCK_3)/3) stored,
TODO_JOURNAL_MOTIREAD int default 0,
BOOK_READING INT default 0,
TASK varchar(150) default '----------',
HOURS decimal(3,1) default 0,
OFFICE_OTHER int default 0,
Overall_Percentage DECIMAL(5,2) generated always as (round((0.5*MEDITATION+2*GYM_WORKOUT+1*COMMUNICATION+1*APTITUDE+2*MYSQL_HTML_CSS+6*PYTHON+0.5*TODO_JOURNAL_MOTIREAD+0.5*BOOK_READING+HOURS*OFFICE_OTHER)/(CASE WHEN DAILY_DAY IN ('Sat', 'Sun') THEN 10 ELSE 13 END),2)) stored
);
SHOW COLUMNS FROM DailyTimeSheet;
INSERT INTO DailyTimeSheet (DAILY_DATE,
    MEDITATION,
    GYM_WORKOUT,
    COMMUNICATION,
    APTITUDE,
    MYSQL_HTML_CSS,
    BLOCK_1,
    BLOCK_2,
    BLOCK_3,
    TODO_JOURNAL_MOTIREAD,
    BOOK_READING,
    TASK,
    HOURS,
    OFFICE_OTHER
) VALUES ("2025-06-15",
    100,
    100,
    100,
    100,
    100,
    100,
    100,
    100,
    100,
    100,
    'Dummy task all 100',
    0,
    0
);

drop table DailyTimeSheet;
TRUNCATE DailyTimeSheet;
SELECT * FROM DailyTimeSheet;
/*CREATE TABLE PYTHON(
DAILY_DATE date PRIMARY KEY DEFAULT (CURRENT_DATE),
BLOCK_1 INT,
BLOCK_2 int,
BLOCK_3 int,
BLOCK_AVERAGE FLOAT as ((BLOCK_1+BLOCK_2+BLOCK_3)/3) stored,
CONSTRAINT PYTHON FOREIGN KEY(DAILY_DATE) REFERENCES DailyTimeSheet(DAILY_DATE) ON DELETE CASCADE ON UPDATE CASCADE
);*/
SELECT * FROM dailytimetable;
select * from DailyTimeSheet;
/*
create table OFFICE_OTHER(
DAILY_DATE date PRIMARY KEY DEFAULT (CURRENT_DATE),
TASK varchar(150),
HOURS time,
PERCENTAGE int,
constraint OFFICE_OTHER foreign key (DAILY_DATE) references DailyTimeSheet(DAILY_DATE) on delete cascade on update cascade
);*/
ALTER TABLE DailyTimeSheet
DROP COLUMN DAILY_DAY;

ALTER TABLE DailyTimeSheet
ADD COLUMN DAILY_DAY VARCHAR(3)
    GENERATED ALWAYS AS (LEFT(DAYNAME(DAILY_DATE), 3)) STORED;
INSERT INTO DailyTimeSheet (
   TASK,
    HOURS,
    OFFICE_OTHER
)
VALUES (
    'super',13,76
);
select curdate();
truncate DailyTimeSheet;
describe DailyTimeSheet;
select * from DailyTimeSheet;
drop table oppa;
select CURRENT_TIMESTAMP();
show tables;

