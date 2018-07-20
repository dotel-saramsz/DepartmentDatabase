CREATE DATABASE departmentDatabase;

USE departmentDatabase;


#Schemas here!
CREATE TABLE department(
	dept_id INT NOT NULL PRIMARY KEY auto_increment,
    dept_name VARCHAR(50) NOT NULL,
    photo_url VARCHAR(255),
    dept_block CHAR(1) NOT NULL UNIQUE,
    CHECK(dept_block IN ('A','B','C','D','E','F','G','H'))
    );

CREATE TABLE employee(
	staff_id INT NOT NULL PRIMARY KEY,
    staff_fname VARCHAR(20) NOT NULL,
    staff_mname VARCHAR(15) NOT NULL,
    staff_lname VARCHAR(20) NOT NULL,
    photo_url VARCHAR(255),
    email varchar(100) UNIQUE,
    home_contact VARCHAR(10) UNIQUE,
    mobile_contact VARCHAR(15) UNIQUE,
    address VARCHAR(30),
    department_id INT,
    date_joined TIMESTAMP DEFAULT NOW(),
    FOREIGN KEY(department_id) REFERENCES department(dept_id) ON DELETE CASCADE ON UPDATE CASCADE
    );  
    
    
CREATE TABLE academic_post(
	post_id INT PRIMARY KEY AUTO_INCREMENT,
    post_name VARCHAR(30)
);
CREATE TABLE nonacademic_post(
	post_id INT PRIMARY KEY AUTO_INCREMENT,
    post_name VARCHAR(30)
);
    
CREATE TABLE academic(
# add Post HOD, DHOD
	staff_id INT NOT NULL PRIMARY KEY,
    salutation VARCHAR(10),
	designation VARCHAR(20) NOT NULL,
    service_type VARCHAR(15),
    contract_type VARCHAR(15),
    qualification VARCHAR(10),
    post_id INT,
    FOREIGN KEY(post_id) REFERENCES academic_post(post_id) ON DELETE CASCADE ON UPDATE CASCADE,
    CHECK(contract_type IN ('IOE Contract','TU Contract','Course Contract')),
    FOREIGN KEY(staff_id) REFERENCES employee(staff_id) ON DELETE CASCADE ON UPDATE CASCADE
    );
    
CREATE TABLE nonacademic(
	staff_id INT NOT NULL PRIMARY KEY,
	post_id INT,
    FOREIGN KEY(post_id) REFERENCES nonacademic_post(post_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(staff_id) REFERENCES employee(staff_id) ON DELETE CASCADE ON UPDATE CASCADE
    );
    
CREATE TABLE course(
	course_code VARCHAR(10) NOT NULL PRIMARY KEY UNIQUE,
	course_name VARCHAR(60) NOT NULL,
    department_id INT,
    FOREIGN KEY(department_id) REFERENCES department(dept_id) ON DELETE CASCADE ON UPDATE CASCADE
    );
    
CREATE TABLE instructs(
	staff_id INT not null,
    course_code VARCHAR(10) not null,
    semester CHAR(1) not null,
	FOREIGN KEY(staff_id) REFERENCES academic(staff_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(course_code) REFERENCES course(course_code) ON DELETE CASCADE ON UPDATE CASCADE
     );
     
CREATE TABLE canteach(
	staff_id INT not null,
    course_code VARCHAR(10) not null,
	FOREIGN KEY(staff_id) REFERENCES academic(staff_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(course_code) REFERENCES course(course_code) ON DELETE CASCADE ON UPDATE CASCADE
     );


#Triggers here!
SET DELIMITER |

CREATE TRIGGER set_null BEFORE INSERT ON academic
FOR EACH ROW
BEGIN
IF NEW.contract_type = ' ' OR NEW.contract_type = '' THEN
	SET NEW.contract_type = NULL;
END IF;
END; |

CREATE TRIGGER set_unknown BEFORE INSERT ON employee
FOR EACH ROW 
BEGIN
IF NEW.address = ' ' OR NEW.address = '' THEN
	SET NEW.address = 'UNKNOWN';
END IF;
END; |


#CREATE TRIGGER instructor_canteach BEFORE INSERT ON instructs
#FOR EACH ROW 
#BEGIN
#	IF (NEW.staff_id,NEW.course_code) NOT IN (SELECT staff_id,course_code from can_teach)  then
#		rollback;
#	END IF;		
#END; |

SET DELIMITER ;


#Views Here!
CREATE VIEW instructor AS 
SELECT E.staff_id,A.salutation,CONCAT(E.staff_fname,' ',E.staff_lname) AS name,
E.email,E.mobile_contact,A.designation FROM employee E
NATURAL JOIN academic A
ORDER BY E.staff_fname;


#Data Here ! 
INSERT INTO department (dept_name,dept_block)
VALUES ('Department of Electronics and Computer Engineering','B'),
('Department of Mechanical Engineering','D'),
('Department of Civil Engineering' ,'F'),
 ('Department of Electrical Engineering','C'),
('Department of Science and Humanitites','G'),
('Department of Architecture','E');

INSERT INTO employee(staff_id,staff_fname,staff_mname,staff_lname,email,mobile_contact,address,department_id)
VALUES
(1662,'Aman','','Shakya','aman.shakya@ioe.edu.np','9841218877','',1),
(1843,'Amar','Bahadur', 'Gurung','gurung21amar@gmail.com','9851082279','',1),
(7000,'Amrit','Lal', 'Ranjitkar','','9841213242','',1),
(1814,'Anand','Kumar','Sah','er_anandkumar@hotmail.com','9849664988','',1),
(1648,'Anil','','Verma','anil@ioe.edu.np','9851027501','',1),
(1837,'Anila','','Kansakar','anilakansakar@gmail.com','9843760911','',1),
(7001,'Arjun','','Upadhyaya','arjunupadhyay552@gmail.com','9849765284','',1),
(1659,'Arun','Kumar','Timilsina','t.arun@ioe.edu.np','9851148555','',1),
(7002,'Babita','','Pradhan','pradhanbabita457@gmail.com','9841686457','',1),
(1660,'Babu','Ram' ,'Dawadi','baburd@ioe.edu.np','9841340354','',1),
(1836,'Bal','Krishna','Nyaupane','balkrishnanyaupane@gmail.com','9851132890','',1),
(1216,'Banshee','Ram','Pradhan','bnsheeramprdhan123@gmail.com','9841317451','',1),
(1222,'Basanta','','Joshi','basanta@ioe.edu.np','9851190040','',1),
(1663,'Bibha','','Sthapit','bibha@ioe.edu.np','9841340250','',1),
(7003,'Chaitya','', 'Shakya','chaitya.shakya@ioe.edu.np','9849451159','',1),
(1741,'Daya','Sagar','Baral','dsbaral@ioe.edu.np','9851049546','',1),
(1738,'Deepak','Lal','Shrestha','deepak2002@hotmail.com','9851084380','',1),
(1653,'Dibakar','Raj','Pant','pdibakar@gmail.com','9841500525','',1),
(1527,'Dinesh','Kumar','Sharma','dksharma@ioe.edu.np','9851040503','',1),
(7004,'Dinesh','Man','Amatya','','9851184277','',1),
(7005,'Abhijit','', 'Gupta','','9851151706','',1),
(1704,'Durga', 'Prasad', 'Khatiwada','','9841468672','',1),
(7006,'Jitendra', 'Kumar', 'Manandhar','mejiten@ioe.edu.np','9841291845','',1),
(1584,'Jyoti','','Tandukar','jyoti.tandukar@gmail.com','9851026199','',1),
(1716,'Kamal', 'Prasad', 'Nepal','knepal@ioe.edu.np','9851026608','',1),
(7007,'Khagendra' ,'B.' ,'Shrestha','','9851073373','',1),
(1245,'Nand', 'Bikram', 'Adhikari','adhikari@ioe.edu.np','9841741053','',1),
(1695,'Nirpa', 'Dhoj', 'Khadka','ndkhadka@ioe.edu.np','9841413838','',1),
(1587,'Ram', 'Krishna', 'Maharjan','rkmaharjn@gmail.com','9851232355','',1),
(1831,'Ranju', 'Kumari', 'Shiwakoti','rshiwakoti613@gmail.com','9851233734','',1),
(1756,'Rupesh', 'Kumar' ,'Sah','rupeshsah@ioe.edu.np','9851074254','',1),
(1655,'Sanjib', 'Prasad', 'Pandey','sanjeeb@ioe.edu.np','9840052621','',1),
(7008,'Sharad', 'Kumar', 'Ghimire','skghimire@ioe.edu.np','9841284474','',1),
(1529,'Shashidhar', 'Ram' ,'Joshi','srjoshi@ioe.edu.np','9849202577','',1),
(1530,'Subarna','','Shakya','drss@ioe.edu.np','9851032303','',1),
(1841,'Suman','', 'Sharma','seeiumaan@gmail.com','9851081030','',1),
(7009,'Suramya', 'Sharma' ,'Dahal','','9849849873','',1),
(1842,'Surendra','','Khadka','khadkabrand9@gmail.com','9849270472','',1),
(1585,'Surendra','', 'Shrestha','surendra@ioe.edu.np','9851198713','',1),
(1218,'Suresh','','Jha','sjha@ioe.edu.np','9851189597','',1),
(1840,'Suresh','','Pokharel','suresh.wrc@gmail.com','9846333110','',1),
(1162,'Prahlad','','Bista','','9841255247','Gokarna',1),
(1209,'Manish','-','Shrestha','smanish@gmail.com','9841513726','Bramhatole',1),
(1190,'Chhatra','Bahadur','Shrestha','-','9841672445','Pulchowk',1),
(1067,'Jira','Maya','Thapa','-','9849505776','Sanothimi',1),
(1193,'Sangeeta','-','Magar','-','9841573770','Pulchowk',1);

INSERT INTO academic_post(post_name)
VALUES
('HOD'),('DHOD'),('MSc. Coordinator');

INSERT INTO nonacademic_post(post_name)
VALUES
('Admin'),('Office Helper');

INSERT INTO academic(staff_id,salutation,designation,service_type,contract_type,qualification,post_id)
VALUES
(1662,'Dr. Prof.','Lecturer','Full-time','','Doctorate',3),
(1843,'','Lecturer','Part-time','IOE Contract','',null),
(7000,'','Part Time','Part-time','','',null),
(1814,'','Lecturer','Full-time','','',null),
(1648,'','Lecturer','Full-time','IOE Contract','',null),
(1837,'','Instructor','','IOE Contract','',null),
(7001,'','Teaching Assistant','Part-time','','',null),
(1659,'Dr.','Lecturer','Full-time','','Doctorate',null),
(7002,'','Part Time','Part-time','','',null),
(1660,'','Lecturer','Full-time','','',null),
(1836,'','Lecturer','','IOE Contract','',null),
(1216,'','Lecturer','','TU Contract','',null),
(1222,'Dr.','Lecturer','Full-time','IOE Contract','Doctorate',null),
(1663,'','Lecturer','Full-time','','',2),
(7003,'','Part Time','Part-time','','',null),
(1741,'','Lecturer','Full-time','TU Contract','',null),
(1738,'','Instructor','Full-time','','',null),
(1653,'','Reader','Full-time','','',1),
(1527,'Dr.','Professor','Full-time','','Doctorate',null),
(7004,'','Part Time','Part-time','Course Contract','',null),
(7005,'','Part Time','Part-time','Course Contract','',null),
(1704,'','Senior Instructor','Full-time','','',null),
(7006,'','Lecturer','Full-time','','',null),
(1584,'Dr.','Reader','Full-time','','Doctorate',null),
(1716,'','Instructor','Full-time','','',null),
(7007,'','Part Time','Part-time','Course Contract','',null),
(1245,'Dr. Prof.','Lecturer','Full-time','TU Contract','Doctorate',null),
(1695,'','Chief Instructor','Full-time','','',null),
(1587,'Dr.','Professor','Full-time','','Doctorate',null),
(1831,'','Lecturer','','IOE Contract','',null),
(1756,'','Asst. Technician','','TU Contract','',null),
(1655,'Dr.','Reader','Full-time','','Doctorate',null),
(7008,'','Lecturer','Full-time','','',null),
(1529,'Dr. Prof.','Professor','Full-time','','Doctorate',null),
(1530,'Dr. Prof.','Professor','Full-time','','Doctorate',null),
(1841,'','Lecturer','','IOE Contract','',null),
(7009,'','Part Time','Part-time','','',null),
(1842,'','Lecturer','','IOE Contract','',null),
(1585,'Dr.','Reader','Full-time','','Doctorate',null),
(1218,'','Deputy Instructor','Full-time','','',null),
(1840,'','Instructor','','IOE Contract','',null);

INSERT INTO nonacademic(staff_id,post_id)
VALUES
(1162,1),
(1209,1),
(1190,2),
(1067,2),
(1193,2);

INSERT INTO course(course_code,course_name,department_id)
VALUES('CT401','Computer Programming',1),
('CT501','Object Oriented Programming',1),
('CT502','Theory of Computation',1),
('CT552','Data Structure & Algorithm',1),
('CT551','Discrete Structure',1),
('CT601','Software Engineering',1),
('CT602','Data Communication',1),
('CT603','Computer Orginization & Architecture',1),
('CT655','Embedded System',1),
('CT653','Artificial Intelligence',1),
('CT652','Database Management System',1),
('CT651','Object Oriented Analysis & Design',1),
('CT656','Operating System',1),
('CT657','Computer Network',1),
('CT654','Minor Project',1),
('CT701','Project Management',1),
('CT702','Computer Network',1),
('CT703','Distributed System',1),
('CT704','Digital Signal Analysis & Processing',1),
('CT707','Project I',1),
('CT751','Information Systems',1),
('CT753','Simulation & Modeling',1),
('CT754','Internet & Intranet',1),
('CT755','Project II',1),
('CT72501','Advanced Java Programming (Elective I)',1),
('CT72502','Data Mining (Elective I)',1),
('CT72503','Embeded System Design Using ARM Technology (Elective I)',1),
('CT72504','Image Processing & Pattern Recognition (Elective I)',1),
('CT72505','Web Technology (Elective I)',1),
('CT76502','Agile Methodologies (Elective II)',1),
('CT76503','Networking with IPv6 (Elective II)',1),
('CT76507','Big Data Technologies (Elective II)',1),
('CT78501','Remote Sensing (Elective III)',1),
('CT78503','Multimedia System (Elective III)',1),
('CT78504','Enterprise Application Design & Development (Elective III)',1),
('CT78505','XML: Foundation Techniques & Applications (Elective III)',1),
('CT78507','Geographic Information System (Elective III)',1),
('CT78508','Speech Processing (Elective III)',1),
('EX451','Basic Electronics Engineering',1),
('EX501','Electronic Devices & Circuits',1),
('EX502','Digital Logic',1),
('EX503','Electromagnetics',1),
('EX551','Microprocessor',1),
('EX601','Advanced Electronics',1),
('EX602','Instrumentation II',1),
('EX603','Computer Graphics',1),
('EX651','Signal Analysis',1),
('EX652','Communication System I',1),
('EX653','Propagation & Antenna',1),
('EX654','Minor Project',1),
('EX701','Energy Environment & Society',1),
('EX72501','Radar Technology (Elective I)',1),
('EX72502','Satellite Communication (Elective I)',1),
('EX72503','Biomedical Instrumentation (Elective I)',1),
('EX72504','Aeronautical Telecommunication (Elective I)',1),
('EX72505','RF & Microwave Engineering (Elective I)',1),
('EX78503','Telecommunication (Elective III)',1);


INSERT INTO canteach(staff_id,course_code)
VALUES
(1662,'CT502'),
(1662,'CT652'),
(1814,'EX602'),
(1648,'CT656'),
(1648,'CT657'),
(1648,'CT654'),
(1648,'EX603'),
(1659,'CT601'),
(1659,'CT651'),
(1659,'CT701'),
(1660,'CT401'),
(1222,'CT653'),
(1663,'CT552'),
(7003,'EX503'),
(1741,'EX551'),
(1653,'EX502'),
(7006,'EX451'),
(7006,'EX501'),
(7006,'EX601'),
(1245,'CT602'),
(1655,'CT551'),
(1655,'CT704'),
(1655,'EX503'),
(1530,'CT603'),
(1530,'CT753'),
(1585,'CT655'),
(1585,'CT703'),
(1218,'EX451');


INSERT INTO instructs(staff_id,course_code,semester)
VALUES
(1662,'CT502',3),
(1662,'CT652',6),
(1814,'EX602',5),
(1648,'CT656',6),
(1648,'CT657',7),
(1648,'CT654',6),
(1648,'EX603',5),
(1659,'CT601',5),
(1659,'CT651',6),
(1659,'CT701',7),
(1660,'CT401',1),
(1222,'CT653',6),
(1663,'CT552',4),
(7003,'EX503',3),
(1741,'EX551',4),
(1653,'EX502',3),
(7006,'EX451',2),
(7006,'EX501',3),
(7006,'EX601',4),
(1245,'CT602',5),
(1655,'CT551',4),
(1655,'CT704',7),
(1655,'EX503',3),
(1530,'CT603',5),
(1530,'CT753',8),
(1585,'CT655',6),
(1585,'CT703',7),
(1218,'EX451',2);



