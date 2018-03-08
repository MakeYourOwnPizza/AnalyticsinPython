INSERT IGNORE INTO Student VALUES ("111-22-3333","JOHN","CHILDS","6461231212","New York","10025");
INSERT IGNORE INTO Student (SSN,f_name,l_name,city,zip) VALUES (
	"123-12-1234","Mary","Arias","New York","10011");
INSERT IGNORE INTO Student VALUES ("555-11-7777","Roberto","Perez","9173335479","San Francisco","94110");
INSERT IGNORE INTO Student VALUES ("222-33-4455","Lila","Pennington","4251231212","Seattle","98105");

INSERT IGNORE INTO Course VALUES ("c1","Data analytics",1127);
INSERT IGNORE INTO Course VALUES ("c2","Python",303);
INSERT IGNORE INTO Course VALUES ("c3","corp fin",331);
INSERT IGNORE INTO Course VALUES ("c4","prod. mgmt",1127);
INSERT IGNORE INTO Course VALUES ("c5","Ethics",303);
INSERT IGNORE INTO Course VALUES ("c6","leadership",303);
INSERT IGNORE INTO Course VALUES ("c7","bus analytics",1127);

INSERT IGNORE INTO Enrolls_in VALUES ("111-22-3333","c1",93.00);
INSERT IGNORE INTO Enrolls_in VALUES ("123-12-1234","c1",87.00);
INSERT IGNORE INTO Enrolls_in VALUES ("111-22-3333","c2",95.00);
INSERT IGNORE INTO Enrolls_in VALUES ("222-33-4455","c3",44.00);
INSERT IGNORE INTO Enrolls_in VALUES ("555-11-7777","c1",36.00);

SELECT * FROM Enrolls_in;
SELECT * FROM Student WHERE city = "New York";
SELECT DISTINCT city FROM Student ORDER BY city DESC;
CREATE temporary TABLE averages SELECT class, avg(score) AS average from Enrolls_in group by class;
SELECT * from averages;
CREATE TEMPORARY TABLE summary SELECT class, avg(score) AS average, count(score) AS count from Enrolls_in GROUP BY class ORDER BY class asc;
SELECT * FROM summary;

SHOW TABLES
# SELECT f_name, l_name, class FROM student, enrolls_in WHERE Student.ssn = enrolls_in.ssn
# SELECT a.f_name, a.l_name, b.class FROM student a, enrolls_in b WHERE a.ssn = b.ssn AND f_name="John" AND l_name="CHILDS" AND score >= 95;
SELECT c.name FROM student a, enrolls_in b, course c WHERE a.ssn = b.ssn AND b.class = c.number AND a.f_name = "JOHN" AND a.l_name = "CHILDS";
SELECT name, number, room, ssn, score FROM course INNER JOIN Enrolls_in ON course.number = enrolls_in.class
SELECT * FROM Student;