-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: zadanie3
-- ------------------------------------------------------
-- Server version	8.2.0

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
-- Table structure for table `Adresy`
--

DROP TABLE IF EXISTS `Adresy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Adresy` (
  `ID` int DEFAULT NULL,
  `ADRES` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Adresy`
--

LOCK TABLES `Adresy` WRITE;
/*!40000 ALTER TABLE `Adresy` DISABLE KEYS */;
INSERT INTO `Adresy` VALUES (1,'Adres1'),(2,'Adres2'),(3,'Adres3'),(4,'Adres4'),(5,'Adres5'),(6,'Adres6'),(7,'Adres7'),(8,'Adres8'),(9,'Adres9'),(10,'Adres10'),(11,'Adres11');
/*!40000 ALTER TABLE `Adresy` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Nazwiska`
--

DROP TABLE IF EXISTS `Nazwiska`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Nazwiska` (
  `ID` int DEFAULT NULL,
  `NAZWISKO` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Nazwiska`
--

LOCK TABLES `Nazwiska` WRITE;
/*!40000 ALTER TABLE `Nazwiska` DISABLE KEYS */;
INSERT INTO `Nazwiska` VALUES (1,'Nazwisko1'),(2,'Nazwisko2'),(3,'Nazwisko3'),(4,'Nazwisko4'),(5,'Nazwisko5'),(6,'Nazwisko6'),(7,'Nazwisko7'),(8,'Nazwisko8'),(9,'Nazwisko9'),(10,'Nazwisko10');
/*!40000 ALTER TABLE `Nazwiska` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Oceny`
--

DROP TABLE IF EXISTS `Oceny`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Oceny` (
  `ID_osoby` int DEFAULT NULL,
  `Ocena` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Oceny`
--

LOCK TABLES `Oceny` WRITE;
/*!40000 ALTER TABLE `Oceny` DISABLE KEYS */;
INSERT INTO `Oceny` VALUES (1,3),(2,2),(3,4),(4,1),(5,4),(6,5),(7,2),(8,4),(9,2),(10,6),(11,4),(12,3),(1,4),(2,2),(3,2),(4,4),(5,1),(6,2),(7,5),(8,6),(9,3),(10,2),(11,3),(12,1),(1,4),(2,3),(3,2),(4,4),(5,5),(6,3),(7,2),(8,4),(9,1),(10,4),(11,5),(12,2);
/*!40000 ALTER TABLE `Oceny` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Osoby`
--

DROP TABLE IF EXISTS `Osoby`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Osoby` (
  `ID` int DEFAULT NULL,
  `IMIE` text,
  `NAZWISKO` int DEFAULT NULL,
  `ADRES` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Osoby`
--

LOCK TABLES `Osoby` WRITE;
/*!40000 ALTER TABLE `Osoby` DISABLE KEYS */;
INSERT INTO `Osoby` VALUES (1,'Imie1',1,2),(2,'Imie2',1,2),(3,'Imie3',2,2),(4,'Imie4',3,1),(5,'Imie5',4,1),(6,'Imie6',4,1),(7,'Imie7',4,2),(8,'Imie8',1,2),(9,'Imie9',1,2),(10,'Imie10',2,2),(11,'Imie11',1,2),(12,'Imie12',2,2);
/*!40000 ALTER TABLE `Osoby` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-27  9:25:07
