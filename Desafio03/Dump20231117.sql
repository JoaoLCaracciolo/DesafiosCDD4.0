CREATE DATABASE  IF NOT EXISTS `academia` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `academia`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: academia
-- ------------------------------------------------------
-- Server version	8.0.35

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
-- Table structure for table `alunos`
--

DROP TABLE IF EXISTS `alunos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alunos` (
  `matricula` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(255) NOT NULL,
  `cpf` char(11) NOT NULL,
  `telefone` char(11) NOT NULL,
  `endereco` varchar(255) NOT NULL,
  PRIMARY KEY (`matricula`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alunos`
--

LOCK TABLES `alunos` WRITE;
/*!40000 ALTER TABLE `alunos` DISABLE KEYS */;
INSERT INTO `alunos` VALUES (6,'Luís Marcelo Marcos Pereira','71057375810','95935599304','Rua D-31'),(7,'Samuel Severino Mário Oliveira','76131324042','81935329358','Rua Presidente Jânio Quadros'),(8,'Lorena Letícia da Rosa','72057310620','41929507080','Rua Estados Unidos'),(9,'Jaqueline Valentina Lara Pereira','29481224228','69988107327','Rua Andorinha'),(10,'Manoel Severino Novaes','93537377100','53926777219','Rua Silvério de Moraes'),(11,'menino ney','11111111111','18291827161','rua do sol'),(12,'Roberta','81923412382','19234521000','Rua 07'),(13,'Luiza Lira','81956432382','19232355000','Rua Alegria');
/*!40000 ALTER TABLE `alunos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `funcionarios`
--

DROP TABLE IF EXISTS `funcionarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `funcionarios` (
  `id_funcionarios` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(120) NOT NULL,
  `cpf` char(11) NOT NULL,
  `departamento` int NOT NULL,
  `salario` decimal(8,2) NOT NULL,
  `email` varchar(120) NOT NULL,
  PRIMARY KEY (`id_funcionarios`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `funcionarios`
--

LOCK TABLES `funcionarios` WRITE;
/*!40000 ALTER TABLE `funcionarios` DISABLE KEYS */;
INSERT INTO `funcionarios` VALUES (1,'Bianca Caroline Giovana Ferreira','16415957600',5,5540.50,'bianca_ferreira@hotmail.com.br'),(2,'Sara Mariana Rocha','95104202631',5,3520.45,'sara-rocha81@hotmail.com'),(3,'Analu Tatiane Renata Costa','30643586261',3,1255.30,'analu_costa@hotmail.com.br'),(4,'Mariane Regina Manuela dos Santos','47978616223',4,1850.70,'marianereginadossantos@hotmail.com.br'),(5,'Carolina Malu Ribeiro','31434638138',1,8500.00,'carolina-ribeiro71@gmail.com.br');
/*!40000 ALTER TABLE `funcionarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `matriculado`
--

DROP TABLE IF EXISTS `matriculado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `matriculado` (
  `id_matriculado` int NOT NULL AUTO_INCREMENT,
  `fk_matricula` int DEFAULT NULL,
  PRIMARY KEY (`id_matriculado`),
  KEY `fk_matricula` (`fk_matricula`),
  CONSTRAINT `matriculado_ibfk_1` FOREIGN KEY (`fk_matricula`) REFERENCES `alunos` (`matricula`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `matriculado`
--

LOCK TABLES `matriculado` WRITE;
/*!40000 ALTER TABLE `matriculado` DISABLE KEYS */;
INSERT INTO `matriculado` VALUES (1,6),(2,8);
/*!40000 ALTER TABLE `matriculado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `modalidades`
--

DROP TABLE IF EXISTS `modalidades`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `modalidades` (
  `cod_modalidade` int NOT NULL AUTO_INCREMENT,
  `nome_modalidade` varchar(45) NOT NULL,
  `duracao` varchar(3) NOT NULL,
  PRIMARY KEY (`cod_modalidade`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `modalidades`
--

LOCK TABLES `modalidades` WRITE;
/*!40000 ALTER TABLE `modalidades` DISABLE KEYS */;
INSERT INTO `modalidades` VALUES (1,'Yoga','320'),(2,'Natação','150'),(3,'Musculação','120'),(6,'Dança','120');
/*!40000 ALTER TABLE `modalidades` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `personal`
--

DROP TABLE IF EXISTS `personal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `personal` (
  `id_personal` int NOT NULL AUTO_INCREMENT,
  `cref` char(10) NOT NULL,
  `nome` varchar(255) NOT NULL,
  `telefone` char(11) NOT NULL,
  `email` varchar(45) NOT NULL,
  `cpf` char(11) NOT NULL,
  `endereco` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_personal`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `personal`
--

LOCK TABLES `personal` WRITE;
/*!40000 ALTER TABLE `personal` DISABLE KEYS */;
INSERT INTO `personal` VALUES (1,'0291234123','Roberto Alves','82912345123','robertoalves@gmail.com','92813287631','Rua abelha 22'),(2,'8271829121','Juliana Lima','5598212731','julianalima@gmail.com','82719213721','Rua Floresta'),(3,'8271235761','Gabriel Barbosa','72918271631','gabrielbarbosa@gmail.com','28172635142','Rua Navios'),(4,'1281721234','Emanuelly Giovana Gonçalves','81921281234','emanuellygiovanna@gmail.com','12375429124','Rua do Girassol'),(5,'1827131231','Larissa Galvão','55821275432','larissagalvao@gmail.com','12839200852','Rua Vinte Dois de Março');
/*!40000 ALTER TABLE `personal` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-17  0:28:52
