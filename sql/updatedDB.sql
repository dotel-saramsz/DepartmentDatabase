-- MySQL dump 10.13  Distrib 5.7.22, for Linux (x86_64)
--
-- Host: localhost    Database: departmentDatabase
-- ------------------------------------------------------
-- Server version	5.7.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `academic`
--

DROP TABLE IF EXISTS `academic`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `academic` (
  `staff_id` int(11) NOT NULL,
  `salutation` varchar(10) DEFAULT NULL,
  `designation` varchar(20) NOT NULL,
  `service_type` varchar(15) DEFAULT NULL,
  `contract_type` varchar(15) DEFAULT NULL,
  `qualification` varchar(10) DEFAULT NULL,
  `post_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`staff_id`),
  KEY `post_id` (`post_id`),
  CONSTRAINT `academic_ibfk_1` FOREIGN KEY (`post_id`) REFERENCES `academic_post` (`post_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `academic_ibfk_2` FOREIGN KEY (`staff_id`) REFERENCES `employee` (`staff_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `academic`
--

LOCK TABLES `academic` WRITE;
/*!40000 ALTER TABLE `academic` DISABLE KEYS */;
INSERT INTO `academic` VALUES (1216,'','Lecturer','','TU Contract','',NULL),(1218,'Mr.','Deputy Instructor','Full-time','IOE Contract','Masters',NULL),(1222,'Dr.','Lecturer','Full-time','IOE Contract','Doctorate',NULL),(1245,'Prof. Dr.','Lecturer','Full-time','TU Contract','Doctorate',NULL),(1527,'Dr.','Professor','Full-time','','Doctorate',NULL),(1529,'Dr. Prof.','Professor','Full-time','','Doctorate',NULL),(1530,'Dr. Prof.','Professor','Full-time','','Doctorate',NULL),(1584,'Dr.','Reader','Full-time','','Doctorate',NULL),(1585,'Dr.','Reader','Full-time','','Doctorate',NULL),(1587,'Dr.','Professor','Full-time','','Doctorate',NULL),(1648,'','Lecturer','Full-time','IOE Contract','',NULL),(1653,'Dr.','Reader','Full-time','','',1),(1655,'Dr.','Reader','Full-time','','Doctorate',NULL),(1659,'Dr.','Lecturer','Full-time','','Doctorate',NULL),(1660,'','Lecturer','Full-time','','',NULL),(1662,'Dr. Prof.','Lecturer','Full-time','','Doctorate',3),(1663,'','Lecturer','Full-time','','',2),(1695,'','Chief Instructor','Full-time','','',NULL),(1704,'','Senior Instructor','Full-time','','',NULL),(1716,'','Instructor','Full-time','','',NULL),(1738,'','Instructor','Full-time','','',NULL),(1741,'','Lecturer','Full-time','TU Contract','',NULL),(1756,'','Asst. Technician','','TU Contract','',NULL),(1814,'','Lecturer','Full-time','','',NULL),(1831,'','Lecturer','','IOE Contract','',NULL),(1836,'Mr.','Lecturer','','IOE Contract','Masters',NULL),(1837,'','Instructor','','IOE Contract','',NULL),(1840,'','Instructor','','IOE Contract','',NULL),(1841,'','Lecturer','','IOE Contract','',NULL),(1842,'','Lecturer','','IOE Contract','',NULL),(1843,'','Lecturer','Part-time','IOE Contract','',NULL),(7000,'','Part Time','Part-time','','',NULL),(7001,'','Teaching Assistant','Part-time','','',NULL),(7002,'','Part Time','Part-time','','',NULL),(7003,'','Part Time','Part-time','','',NULL),(7004,'','Part Time','Part-time','Course Contract','',NULL),(7005,'','Part Time','Part-time','Course Contract','',NULL),(7006,'','Lecturer','Full-time','','',NULL),(7007,'','Part Time','Part-time','Course Contract','',NULL),(7008,'','Lecturer','Full-time','','',NULL),(7009,'','Part Time','Part-time','','',NULL),(9222,'Mr.','Lecturer','Full-time','TU Contract','Masters',NULL),(9777,'Dr.','Chief Instructor','Part-time','TU Contract','Doctorate',2);
/*!40000 ALTER TABLE `academic` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `academic_post`
--

DROP TABLE IF EXISTS `academic_post`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `academic_post` (
  `post_id` int(11) NOT NULL AUTO_INCREMENT,
  `post_name` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`post_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `academic_post`
--

LOCK TABLES `academic_post` WRITE;
/*!40000 ALTER TABLE `academic_post` DISABLE KEYS */;
INSERT INTO `academic_post` VALUES (1,'Head of Department'),(2,'Deputy Head of Department'),(3,'MSc. Coordinator');
/*!40000 ALTER TABLE `academic_post` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary table structure for view `academicprofile`
--

DROP TABLE IF EXISTS `academicprofile`;
/*!50001 DROP VIEW IF EXISTS `academicprofile`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `academicprofile` AS SELECT 
 1 AS `staff_id`,
 1 AS `staff_fullname`,
 1 AS `email`,
 1 AS `home_contact`,
 1 AS `mobile_contact`,
 1 AS `address`,
 1 AS `designation`,
 1 AS `service_type`,
 1 AS `contract_type`,
 1 AS `qualification`,
 1 AS `post_name`,
 1 AS `photo_url`,
 1 AS `department_id`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `academicsummary`
--

DROP TABLE IF EXISTS `academicsummary`;
/*!50001 DROP VIEW IF EXISTS `academicsummary`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `academicsummary` AS SELECT 
 1 AS `staff_id`,
 1 AS `staff_fname`,
 1 AS `staff_mname`,
 1 AS `staff_lname`,
 1 AS `email`,
 1 AS `home_contact`,
 1 AS `mobile_contact`,
 1 AS `address`,
 1 AS `salutation`,
 1 AS `designation`,
 1 AS `service_type`,
 1 AS `contract_type`,
 1 AS `qualification`,
 1 AS `post_id`,
 1 AS `post_name`,
 1 AS `photo_url`,
 1 AS `department_id`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `canteach`
--

DROP TABLE IF EXISTS `canteach`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `canteach` (
  `staff_id` int(11) NOT NULL,
  `course_code` varchar(10) NOT NULL,
  KEY `staff_id` (`staff_id`),
  KEY `course_code` (`course_code`),
  CONSTRAINT `canteach_ibfk_1` FOREIGN KEY (`staff_id`) REFERENCES `academic` (`staff_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `canteach_ibfk_2` FOREIGN KEY (`course_code`) REFERENCES `course` (`course_code`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `canteach`
--

LOCK TABLES `canteach` WRITE;
/*!40000 ALTER TABLE `canteach` DISABLE KEYS */;
INSERT INTO `canteach` VALUES (1662,'CT502'),(1662,'CT652'),(1814,'EX602'),(1648,'CT656'),(1648,'CT657'),(1648,'CT654'),(1648,'EX603'),(1659,'CT601'),(1659,'CT651'),(1659,'CT701'),(1660,'CT401'),(1222,'CT653'),(1663,'CT552'),(7003,'EX503'),(1741,'EX551'),(1653,'EX502'),(7006,'EX451'),(7006,'EX501'),(7006,'EX601'),(1655,'CT551'),(1655,'CT704'),(1655,'EX503'),(1530,'CT603'),(1530,'CT753'),(1585,'CT655'),(1585,'CT703'),(9222,'BG997'),(9222,'BG998'),(1245,'CT602'),(1245,'CT657'),(1218,'CT655'),(1218,'EX451'),(1218,'EX503'),(9777,'BG997'),(9777,'BG998'),(9777,'CT653'),(9777,'CT656'),(1836,'CT502');
/*!40000 ALTER TABLE `canteach` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `course`
--

DROP TABLE IF EXISTS `course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `course` (
  `course_code` varchar(10) NOT NULL,
  `course_name` varchar(60) NOT NULL,
  `department_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`course_code`),
  UNIQUE KEY `course_code` (`course_code`),
  KEY `department_id` (`department_id`),
  CONSTRAINT `course_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `department` (`dept_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `course`
--

LOCK TABLES `course` WRITE;
/*!40000 ALTER TABLE `course` DISABLE KEYS */;
INSERT INTO `course` VALUES ('BG997','Dummy Course 3',1),('BG998','Dummy Course 2',1),('CT401','Computer Programming',1),('CT501','Object Oriented Programming',1),('CT502','Theory of Computation',1),('CT551','Discrete Structure',1),('CT552','Data Structure & Algorithm',1),('CT601','Software Engineering',1),('CT602','Data Communication',1),('CT603','Computer Orginization & Architecture',1),('CT651','Object Oriented Analysis & Design',1),('CT652','Database Management System',1),('CT653','Artificial Intelligence',1),('CT654','Minor Project',1),('CT655','Embedded System',1),('CT656','Operating System',1),('CT657','Computer Network',1),('CT701','Project Management',1),('CT702','Computer Network',1),('CT703','Distributed System',1),('CT704','Digital Signal Analysis & Processing',1),('CT707','Project I',1),('CT72501','Advanced Java Programming (Elective I)',1),('CT72502','Data Mining (Elective I)',1),('CT72503','Embeded System Design Using ARM Technology (Elective I)',1),('CT72504','Image Processing & Pattern Recognition (Elective I)',1),('CT72505','Web Technology (Elective I)',1),('CT751','Information Systems',1),('CT753','Simulation & Modeling',1),('CT754','Internet & Intranet',1),('CT755','Project II',1),('CT76502','Agile Methodologies (Elective II)',1),('CT76503','Networking with IPv6 (Elective II)',1),('CT76507','Big Data Technologies (Elective II)',1),('CT78501','Remote Sensing (Elective III)',1),('CT78503','Multimedia System (Elective III)',1),('CT78504','Enterprise Application Design & Development (Elective III)',1),('CT78505','XML: Foundation Techniques & Applications (Elective III)',1),('CT78507','Geographic Information System (Elective III)',1),('CT78508','Speech Processing (Elective III)',1),('EX451','Basic Electronics Engineering',1),('EX501','Electronic Devices & Circuits',1),('EX502','Digital Logic',1),('EX503','Electromagnetics',1),('EX551','Microprocessor',1),('EX601','Advanced Electronics',1),('EX602','Instrumentation II',1),('EX603','Computer Graphics',1),('EX651','Signal Analysis',1),('EX652','Communication System I',1),('EX653','Propagation & Antenna',1),('EX654','Minor Project',1),('EX701','Energy Environment & Society',1),('EX72501','Radar Technology (Elective I)',1),('EX72502','Satellite Communication (Elective I)',1),('EX72503','Biomedical Instrumentation (Elective I)',1),('EX72504','Aeronautical Telecommunication (Elective I)',1),('EX72505','RF & Microwave Engineering (Elective I)',1),('EX78503','Telecommunication (Elective III)',1);
/*!40000 ALTER TABLE `course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `department`
--

DROP TABLE IF EXISTS `department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `department` (
  `dept_id` int(11) NOT NULL AUTO_INCREMENT,
  `dept_name` varchar(50) NOT NULL,
  `photo_url` varchar(255) DEFAULT NULL,
  `dept_block` char(1) NOT NULL,
  `dept_code` varchar(10) NOT NULL,
  `phone_number` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`dept_id`),
  UNIQUE KEY `dept_block` (`dept_block`),
  UNIQUE KEY `dept_code` (`dept_code`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `department`
--

LOCK TABLES `department` WRITE;
/*!40000 ALTER TABLE `department` DISABLE KEYS */;
INSERT INTO `department` VALUES (1,'Department of Electronics and Computer Engineering',NULL,'B','doece',NULL),(2,'Department of Mechanical Engineering',NULL,'D','dome',NULL),(3,'Department of Civil Engineering',NULL,'F','doce',NULL),(4,'Department of Electrical Engineering',NULL,'C','doee',NULL),(5,'Department of Science and Humanitites',NULL,'G','dosh',NULL),(6,'Department of Architecture',NULL,'E','doarch',NULL);
/*!40000 ALTER TABLE `department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `employee` (
  `staff_id` int(11) NOT NULL,
  `staff_fname` varchar(20) NOT NULL,
  `staff_mname` varchar(15) NOT NULL,
  `staff_lname` varchar(20) NOT NULL,
  `photo_url` varchar(255) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `home_contact` varchar(10) DEFAULT NULL,
  `mobile_contact` varchar(15) DEFAULT NULL,
  `address` varchar(30) DEFAULT NULL,
  `department_id` int(11) DEFAULT NULL,
  `date_joined` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`staff_id`),
  UNIQUE KEY `home_contact` (`home_contact`),
  UNIQUE KEY `mobile_contact` (`mobile_contact`),
  UNIQUE KEY `email` (`email`),
  KEY `department_id` (`department_id`),
  CONSTRAINT `employee_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `department` (`dept_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES (1067,'Juna','Maya','Thapa',NULL,'juna@gmail.com',NULL,'9849505776','Sanothimi',1,'2018-07-03 13:48:31'),(1162,'Prahlad','','Bista',NULL,NULL,NULL,'9841255247','Gokarna',1,'2018-07-03 13:48:31'),(1190,'Chhatra','Bahadur','Shrestha',NULL,NULL,NULL,'9841672445','Pulchowk',1,'2018-07-03 13:48:31'),(1193,'Sangeeta','','Magar',NULL,NULL,NULL,'9841573770','Pulchowk',1,'2018-07-03 13:48:31'),(1209,'Manish','','Shrestha','employee_1209.jpg','smanish@gmail.com',NULL,'9841513726','Bramha Tole',1,'2018-07-03 13:48:31'),(1216,'Banshee','Ram','Pradhan',NULL,'bnsheeramprdhan123@gmail.com',NULL,'9841317451','',1,'2018-07-03 13:48:31'),(1218,'Suresh','','Jha','employee_1218.jpg','sjha@ioe.edu.np',NULL,'9851189597','',1,'2018-07-03 13:48:31'),(1222,'Basanta','','Joshi',NULL,'basanta@ioe.edu.np',NULL,'9851190040','',1,'2018-07-03 13:48:31'),(1245,'Nanda','Bikram','Adhikari','employee_1245.jpeg','nbadhikari@ioe.edu.np',NULL,'9841741053','',1,'2018-07-03 13:48:31'),(1527,'Dinesh','Kumar','Sharma',NULL,'dksharma@ioe.edu.np',NULL,'9851040503','',1,'2018-07-03 13:48:31'),(1529,'Shashidhar','Ram','Joshi',NULL,'srjoshi@ioe.edu.np',NULL,'9849202577','',1,'2018-07-03 13:48:31'),(1530,'Subarna','','Shakya',NULL,'drss@ioe.edu.np',NULL,'9851032303','',1,'2018-07-03 13:48:31'),(1584,'Jyoti','','Tandukar',NULL,'jyoti.tandukar@gmail.com',NULL,'9851026199','',1,'2018-07-03 13:48:31'),(1585,'Surendra','','Shrestha',NULL,'surendra@ioe.edu.np',NULL,'9851198713','',1,'2018-07-03 13:48:31'),(1587,'Ram','Krishna','Maharjan',NULL,'rkmaharjn@gmail.com',NULL,'9851232355','',1,'2018-07-03 13:48:31'),(1648,'Anil','','Verma',NULL,'anil@ioe.edu.np',NULL,'9851027501','',1,'2018-07-03 13:48:31'),(1653,'Dibakar','Raj','Pant',NULL,'pdibakar@gmail.com',NULL,'9841500525','',1,'2018-07-03 13:48:31'),(1655,'Sanjib','Prasad','Pandey',NULL,'sanjeeb@ioe.edu.np',NULL,'9840052621','',1,'2018-07-03 13:48:31'),(1659,'Arun','Kumar','Timilsina',NULL,'t.arun@ioe.edu.np',NULL,'9851148555','',1,'2018-07-03 13:48:31'),(1660,'Babu','Ram','Dawadi',NULL,'baburd@ioe.edu.np',NULL,'9841340354','',1,'2018-07-03 13:48:31'),(1662,'Aman','','Shakya',NULL,'aman.shakya@ioe.edu.np',NULL,'9841218877','',1,'2018-07-03 13:48:31'),(1663,'Bibha','','Sthapit',NULL,'bibha@ioe.edu.np',NULL,'9841340250','',1,'2018-07-03 13:48:31'),(1695,'Nirpa','Dhoj','Khadka',NULL,'ndkhadka@ioe.edu.np',NULL,'9841413838','',1,'2018-07-03 13:48:31'),(1704,'Durga','Prasad','Khatiwada',NULL,NULL,NULL,'9841468672','',1,'2018-07-03 13:48:31'),(1716,'Kamal','Prasad','Nepal',NULL,'knepal@ioe.edu.np',NULL,'9851026608','',1,'2018-07-03 13:48:31'),(1738,'Deepak','Lal','Shrestha',NULL,'deepak2002@hotmail.com',NULL,'9851084380','',1,'2018-07-03 13:48:31'),(1741,'Daya','Sagar','Baral',NULL,'dsbaral@ioe.edu.np',NULL,'9851049546','',1,'2018-07-03 13:48:31'),(1756,'Rupesh','Kumar','Sah',NULL,'rupeshsah@ioe.edu.np',NULL,'9851074254','',1,'2018-07-03 13:48:31'),(1814,'Anand','Kumar','Sah',NULL,'er_anandkumar@hotmail.com',NULL,'9849664988','',1,'2018-07-03 13:48:31'),(1831,'Ranju','Kumari','Shiwakoti',NULL,'rshiwakoti613@gmail.com',NULL,'9851233734','',1,'2018-07-03 13:48:31'),(1836,'Bal','Krishna','Nyaupane',NULL,'balkrishnanyaupane@gmail.com',NULL,'9851132890','',1,'2018-07-03 13:48:31'),(1837,'Anila','','Kansakar',NULL,'anilakansakar@gmail.com',NULL,'9843760911','',1,'2018-07-03 13:48:31'),(1840,'Suresh','','Pokharel',NULL,'suresh.wrc@gmail.com',NULL,'9846333110','',1,'2018-07-03 13:48:31'),(1841,'Suman','','Sharma',NULL,'seeiumaan@gmail.com',NULL,'9851081030','',1,'2018-07-03 13:48:31'),(1842,'Surendra','','Khadka',NULL,'khadkabrand9@gmail.com',NULL,'9849270472','',1,'2018-07-03 13:48:31'),(1843,'Amar','Bahadur','Gurung',NULL,'gurung21amar@gmail.com',NULL,'9851082279','',1,'2018-07-03 13:48:31'),(6668,'iiiheroni','bhd','tmgi',NULL,'iiiemail@emaili','','','here',1,'2018-07-06 22:12:55'),(6868,'Chari','Maya','Lama',NULL,'chari@gmail.com','0165656','984732310','London',1,'2018-07-06 04:55:42'),(7000,'Amrit','Lal','Ranjitkar',NULL,NULL,NULL,'9841213242','',1,'2018-07-03 13:48:31'),(7001,'Arjun','','Upadhyaya',NULL,'arjunupadhyay552@gmail.com',NULL,'9849765284','',1,'2018-07-03 13:48:31'),(7002,'Babita','','Pradhan',NULL,'pradhanbabita457@gmail.com',NULL,'9841686457','',1,'2018-07-03 13:48:31'),(7003,'Chaitya','','Shakya',NULL,'chaitya.shakya@ioe.edu.np',NULL,'9849451159','',1,'2018-07-03 13:48:31'),(7004,'Dinesh','Man','Amatya',NULL,NULL,NULL,'9851184277','',1,'2018-07-03 13:48:31'),(7005,'Abhijit','','Gupta',NULL,NULL,NULL,'9851151706','',1,'2018-07-03 13:48:31'),(7006,'Jitendra','Kumar','Manandhar',NULL,'mejiten@ioe.edu.np',NULL,'9841291845','',1,'2018-07-03 13:48:31'),(7007,'Khagendra','B.','Shrestha',NULL,NULL,NULL,'9851073373','',1,'2018-07-03 13:48:31'),(7008,'Sharad','Kumar','Ghimire',NULL,'skghimire@ioe.edu.np',NULL,'9841284474','',1,'2018-07-03 13:48:31'),(7009,'Suramya','Sharma','Dahal',NULL,NULL,NULL,'9849849873','',1,'2018-07-03 13:48:31'),(9222,'Budo','Prasad','Talama',NULL,'bal@gmail.com','01663663','98023434','',1,'2018-07-07 03:38:14'),(9292,'Chatra','Pati','Sivaji','employee_9292.jpg',NULL,'02144586','9843456987','nowhere',1,'2018-07-07 03:40:23'),(9777,'David','Prasad','Kumle','employee_9777.jpeg','kumle@gmail.com','2020103','9851290666','Chitwan',1,'2018-07-06 05:43:23'),(9797,'Hari','','dafa',NULL,'s@gm.com','6464','6464','sdfad',1,'2018-07-05 19:32:21');
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary table structure for view `instructor`
--

DROP TABLE IF EXISTS `instructor`;
/*!50001 DROP VIEW IF EXISTS `instructor`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `instructor` AS SELECT 
 1 AS `staff_id`,
 1 AS `salutation`,
 1 AS `name`,
 1 AS `email`,
 1 AS `mobile_contact`,
 1 AS `designation`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `instructs`
--

DROP TABLE IF EXISTS `instructs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `instructs` (
  `staff_id` int(11) NOT NULL,
  `course_code` varchar(10) NOT NULL,
  `semester` char(1) NOT NULL,
  `program` varchar(4) NOT NULL,
  PRIMARY KEY (`course_code`,`semester`,`program`),
  KEY `staff_id` (`staff_id`),
  CONSTRAINT `instructs_ibfk_1` FOREIGN KEY (`staff_id`) REFERENCES `academic` (`staff_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `instructs_ibfk_2` FOREIGN KEY (`course_code`) REFERENCES `course` (`course_code`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `instructs`
--

LOCK TABLES `instructs` WRITE;
/*!40000 ALTER TABLE `instructs` DISABLE KEYS */;
INSERT INTO `instructs` VALUES (1222,'CT653','6','BCT'),(1245,'CT602','5','BCT'),(1530,'CT603','5','BCT'),(1530,'CT753','8','BCT'),(1585,'CT655','6','BCT'),(1585,'CT703','7','BCT'),(1648,'CT654','6','BCT'),(1648,'CT656','6','BCT'),(1648,'CT657','7','BCT'),(1648,'EX603','5','BCT'),(1653,'EX502','3','BCT'),(1655,'CT551','4','BCT'),(1655,'CT704','7','BCT'),(1659,'CT601','5','BCT'),(1659,'CT651','6','BCT'),(1659,'CT701','7','BCT'),(1660,'CT401','1','BCT'),(1662,'CT652','6','BCT'),(1663,'CT552','4','BCT'),(1741,'EX551','4','BCT'),(1814,'EX602','5','BCT'),(1836,'CT502','3','BCT'),(7006,'EX451','2','BCT'),(7006,'EX501','3','BCT'),(7006,'EX601','4','BCT'),(9222,'BG997','1','BCT'),(9777,'BG997','1','BEX'),(9777,'CT653','7','BCT');
/*!40000 ALTER TABLE `instructs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nonacademic`
--

DROP TABLE IF EXISTS `nonacademic`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `nonacademic` (
  `staff_id` int(11) NOT NULL,
  `post_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`staff_id`),
  KEY `post_id` (`post_id`),
  CONSTRAINT `nonacademic_ibfk_1` FOREIGN KEY (`post_id`) REFERENCES `nonacademic_post` (`post_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `nonacademic_ibfk_2` FOREIGN KEY (`staff_id`) REFERENCES `employee` (`staff_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nonacademic`
--

LOCK TABLES `nonacademic` WRITE;
/*!40000 ALTER TABLE `nonacademic` DISABLE KEYS */;
INSERT INTO `nonacademic` VALUES (1162,1),(1209,1),(1067,2),(1190,2),(1193,2),(6868,2),(9292,2);
/*!40000 ALTER TABLE `nonacademic` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nonacademic_post`
--

DROP TABLE IF EXISTS `nonacademic_post`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `nonacademic_post` (
  `post_id` int(11) NOT NULL AUTO_INCREMENT,
  `post_name` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`post_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nonacademic_post`
--

LOCK TABLES `nonacademic_post` WRITE;
/*!40000 ALTER TABLE `nonacademic_post` DISABLE KEYS */;
INSERT INTO `nonacademic_post` VALUES (1,'Admin'),(2,'Office Helper');
/*!40000 ALTER TABLE `nonacademic_post` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary table structure for view `nonacademicprofile`
--

DROP TABLE IF EXISTS `nonacademicprofile`;
/*!50001 DROP VIEW IF EXISTS `nonacademicprofile`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `nonacademicprofile` AS SELECT 
 1 AS `staff_id`,
 1 AS `staff_fullname`,
 1 AS `email`,
 1 AS `home_contact`,
 1 AS `mobile_contact`,
 1 AS `address`,
 1 AS `post_name`,
 1 AS `photo_url`,
 1 AS `department_id`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `nonacademicsummary`
--

DROP TABLE IF EXISTS `nonacademicsummary`;
/*!50001 DROP VIEW IF EXISTS `nonacademicsummary`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `nonacademicsummary` AS SELECT 
 1 AS `staff_id`,
 1 AS `staff_fname`,
 1 AS `staff_mname`,
 1 AS `staff_lname`,
 1 AS `email`,
 1 AS `home_contact`,
 1 AS `mobile_contact`,
 1 AS `address`,
 1 AS `post_id`,
 1 AS `post_name`,
 1 AS `photo_url`,
 1 AS `department_id`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `teacher_canteach`
--

DROP TABLE IF EXISTS `teacher_canteach`;
/*!50001 DROP VIEW IF EXISTS `teacher_canteach`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `teacher_canteach` AS SELECT 
 1 AS `staff_id`,
 1 AS `staff_fname`,
 1 AS `staff_mname`,
 1 AS `staff_lname`,
 1 AS `course_code`,
 1 AS `course_name`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `teacher_instructs`
--

DROP TABLE IF EXISTS `teacher_instructs`;
/*!50001 DROP VIEW IF EXISTS `teacher_instructs`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `teacher_instructs` AS SELECT 
 1 AS `staff_id`,
 1 AS `staff_fname`,
 1 AS `staff_mname`,
 1 AS `staff_lname`,
 1 AS `course_code`,
 1 AS `course_name`,
 1 AS `semester`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `academicprofile`
--

/*!50001 DROP VIEW IF EXISTS `academicprofile`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`dotelsaramsha`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `academicprofile` AS select `employee`.`staff_id` AS `staff_id`,concat(`academic`.`salutation`,' ',`employee`.`staff_fname`,' ',`employee`.`staff_mname`,' ',`employee`.`staff_lname`) AS `staff_fullname`,`employee`.`email` AS `email`,`employee`.`home_contact` AS `home_contact`,`employee`.`mobile_contact` AS `mobile_contact`,`employee`.`address` AS `address`,`academic`.`designation` AS `designation`,`academic`.`service_type` AS `service_type`,`academic`.`contract_type` AS `contract_type`,`academic`.`qualification` AS `qualification`,`academic_post`.`post_name` AS `post_name`,`employee`.`photo_url` AS `photo_url`,`employee`.`department_id` AS `department_id` from ((`employee` join `academic` on((`employee`.`staff_id` = `academic`.`staff_id`))) left join `academic_post` on((`academic`.`post_id` = `academic_post`.`post_id`))) order by `employee`.`staff_id` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `academicsummary`
--

/*!50001 DROP VIEW IF EXISTS `academicsummary`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`dotelsaramsha`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `academicsummary` AS select `employee`.`staff_id` AS `staff_id`,`employee`.`staff_fname` AS `staff_fname`,`employee`.`staff_mname` AS `staff_mname`,`employee`.`staff_lname` AS `staff_lname`,`employee`.`email` AS `email`,`employee`.`home_contact` AS `home_contact`,`employee`.`mobile_contact` AS `mobile_contact`,`employee`.`address` AS `address`,`academic`.`salutation` AS `salutation`,`academic`.`designation` AS `designation`,`academic`.`service_type` AS `service_type`,`academic`.`contract_type` AS `contract_type`,`academic`.`qualification` AS `qualification`,`academic`.`post_id` AS `post_id`,`academic_post`.`post_name` AS `post_name`,`employee`.`photo_url` AS `photo_url`,`employee`.`department_id` AS `department_id` from ((`employee` join `academic` on((`employee`.`staff_id` = `academic`.`staff_id`))) left join `academic_post` on((`academic`.`post_id` = `academic_post`.`post_id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `instructor`
--

/*!50001 DROP VIEW IF EXISTS `instructor`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`dotelsaramsha`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `instructor` AS select `E`.`staff_id` AS `staff_id`,`A`.`salutation` AS `salutation`,concat(`E`.`staff_fname`,' ',`E`.`staff_lname`) AS `name`,`E`.`email` AS `email`,`E`.`mobile_contact` AS `mobile_contact`,`A`.`designation` AS `designation` from (`employee` `E` join `academic` `A` on((`E`.`staff_id` = `A`.`staff_id`))) order by `E`.`staff_fname` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `nonacademicprofile`
--

/*!50001 DROP VIEW IF EXISTS `nonacademicprofile`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`dotelsaramsha`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `nonacademicprofile` AS select `employee`.`staff_id` AS `staff_id`,concat(`employee`.`staff_fname`,' ',`employee`.`staff_mname`,' ',`employee`.`staff_lname`) AS `staff_fullname`,`employee`.`email` AS `email`,`employee`.`home_contact` AS `home_contact`,`employee`.`mobile_contact` AS `mobile_contact`,`employee`.`address` AS `address`,`nonacademic_post`.`post_name` AS `post_name`,`employee`.`photo_url` AS `photo_url`,`employee`.`department_id` AS `department_id` from ((`employee` join `nonacademic` on((`employee`.`staff_id` = `nonacademic`.`staff_id`))) left join `nonacademic_post` on((`nonacademic`.`post_id` = `nonacademic_post`.`post_id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `nonacademicsummary`
--

/*!50001 DROP VIEW IF EXISTS `nonacademicsummary`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`dotelsaramsha`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `nonacademicsummary` AS select `employee`.`staff_id` AS `staff_id`,`employee`.`staff_fname` AS `staff_fname`,`employee`.`staff_mname` AS `staff_mname`,`employee`.`staff_lname` AS `staff_lname`,`employee`.`email` AS `email`,`employee`.`home_contact` AS `home_contact`,`employee`.`mobile_contact` AS `mobile_contact`,`employee`.`address` AS `address`,`nonacademic`.`post_id` AS `post_id`,`nonacademic_post`.`post_name` AS `post_name`,`employee`.`photo_url` AS `photo_url`,`employee`.`department_id` AS `department_id` from ((`employee` join `nonacademic` on((`employee`.`staff_id` = `nonacademic`.`staff_id`))) left join `nonacademic_post` on((`nonacademic`.`post_id` = `nonacademic_post`.`post_id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `teacher_canteach`
--

/*!50001 DROP VIEW IF EXISTS `teacher_canteach`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`dotelsaramsha`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `teacher_canteach` AS select `employee`.`staff_id` AS `staff_id`,`employee`.`staff_fname` AS `staff_fname`,`employee`.`staff_mname` AS `staff_mname`,`employee`.`staff_lname` AS `staff_lname`,`canteach`.`course_code` AS `course_code`,`course`.`course_name` AS `course_name` from ((`employee` join `canteach` on((`employee`.`staff_id` = `canteach`.`staff_id`))) join `course` on(((`employee`.`department_id` = `course`.`department_id`) and (`canteach`.`course_code` = `course`.`course_code`)))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `teacher_instructs`
--

/*!50001 DROP VIEW IF EXISTS `teacher_instructs`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`dotelsaramsha`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `teacher_instructs` AS select `employee`.`staff_id` AS `staff_id`,`employee`.`staff_fname` AS `staff_fname`,`employee`.`staff_mname` AS `staff_mname`,`employee`.`staff_lname` AS `staff_lname`,`instructs`.`course_code` AS `course_code`,`course`.`course_name` AS `course_name`,`instructs`.`semester` AS `semester` from ((`employee` join `instructs` on((`employee`.`staff_id` = `instructs`.`staff_id`))) join `course` on(((`employee`.`department_id` = `course`.`department_id`) and (`instructs`.`course_code` = `course`.`course_code`)))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-07-20 12:59:49
