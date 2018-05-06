CREATE DATABASE gradesystem;

use gradesystem;

CREATE TABLE student 
(
	sid INT(10) PRIMARY KEY,
	sname CHAR(20),
	gender CHAR(20)
);

CREATE TABLE course
(
	cid INT(10),
	cname CHAR(20),
	CONSTRAINT cou_pk PRIMARY KEY (cid)
);

CREATE TABLE mark
(
	mid INT(10) PRIMARY KEY,
	sid INT(1
	cid INT(10),
	score INT(10),
	CONSTRAINT mar_fk FOREIGN KEY (sid) REFERENCES student (sid),
	CONSTRAINT mark_fk FOREIGN KEY (cid) REFERENCES course (cid)

);