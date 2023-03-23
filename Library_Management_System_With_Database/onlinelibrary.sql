CREATE DATABASE  IF NOT EXISTS `onlinelibrary` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `onlinelibrary`;
-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: localhost    Database: onlinelibrary
-- ------------------------------------------------------
-- Server version	8.0.29

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `bookdetails`
--

DROP TABLE IF EXISTS `bookdetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bookdetails` (
  `book_id` int NOT NULL AUTO_INCREMENT,
  `book_name` varchar(255) DEFAULT NULL,
  `author_name` varchar(255) DEFAULT NULL,
  `quatity` int NOT NULL,
  `status` varchar(255) DEFAULT NULL,
  `addBy` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`book_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bookdetails`
--

LOCK TABLES `bookdetails` WRITE;
/*!40000 ALTER TABLE `bookdetails` DISABLE KEYS */;
INSERT INTO `bookdetails` VALUES (4,'kgkgkgk','jgojgo',77,'Available',NULL),(5,'introduction to database','pankaj das',10,'Available','admin'),(6,'dddd','llll',12,'Available','admin'),(7,'raw','harry',12,'Available','das'),(8,'law','carry',10,'Available','das'),(9,'gori','gori lal',0,'Not Available','admin'),(10,'robi','robi lal',0,'Available','admin');
/*!40000 ALTER TABLE `bookdetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `borrowdetails`
--

DROP TABLE IF EXISTS `borrowdetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `borrowdetails` (
  `borrow_id` int NOT NULL AUTO_INCREMENT,
  `book_id` int NOT NULL,
  `book_name` varchar(255) NOT NULL,
  `borrow_date` varchar(255) NOT NULL,
  `customer_name` varchar(255) NOT NULL,
  `mobile` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  PRIMARY KEY (`borrow_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `borrowdetails`
--

LOCK TABLES `borrowdetails` WRITE;
/*!40000 ALTER TABLE `borrowdetails` DISABLE KEYS */;
INSERT INTO `borrowdetails` VALUES (5,4,'kgkgkgk','2022-09-27','pankaj','019','pam@'),(6,10,'robi','2022-09-27','pankaj','019','pam@');
/*!40000 ALTER TABLE `borrowdetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `donatedetails`
--

DROP TABLE IF EXISTS `donatedetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `donatedetails` (
  `donate_id` int NOT NULL AUTO_INCREMENT,
  `book_name` varchar(255) NOT NULL,
  `author_name` varchar(255) NOT NULL,
  `quantity` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `mobile` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `date` varchar(255) NOT NULL,
  PRIMARY KEY (`donate_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `donatedetails`
--

LOCK TABLES `donatedetails` WRITE;
/*!40000 ALTER TABLE `donatedetails` DISABLE KEYS */;
INSERT INTO `donatedetails` VALUES (1,'raw','harry',12,'das','01968977706','pankajds@gmail.com','2022-9-14'),(2,'law','carry',10,'das','01968977706','pankajds@gmail.com','2022-9-14');
/*!40000 ALTER TABLE `donatedetails` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-11-17 13:02:00
