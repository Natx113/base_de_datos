-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: localhost    Database: diagnosticador_multisensorial
-- ------------------------------------------------------
-- Server version	8.0.39

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
-- Table structure for table `componentes`
--

DROP TABLE IF EXISTS `componentes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `componentes` (
  `id_componente` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `descripcion` text,
  `vida_util` int DEFAULT NULL,
  `unidad_medida` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id_componente`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `componentes`
--

LOCK TABLES `componentes` WRITE;
/*!40000 ALTER TABLE `componentes` DISABLE KEYS */;
INSERT INTO `componentes` VALUES (1,'Batería','Fuente de energía para arrancar la moto y alimentar los sistemas eléctricos',500,'ciclos'),(2,'Sistema de Encendido','Componente clave para el arranque del motor',1000,'arranques'),(3,'Motor','Corazón de la moto, responsable del movimiento',10000,'kilómetros'),(4,'Sistema de Escape','Maneja los gases de escape del motor',10000,'kilómetros'),(5,'Sistema de Combustible','Regula la mezcla de aire y combustible para el motor',30000,'kilómetros'),(6,'Frenos','Componente crucial para la seguridad de la moto',10000,'kilómetros'),(7,'Neumáticos','Componente que permite el contacto con el suelo',10000,'kilómetros'),(8,'Sistema de Iluminación','Incluye luces delanteras, traseras, direccionales',5000,'horas'),(9,'Suspensión','Absorbe impactos y proporciona estabilidad',15000,'kilómetros'),(10,'Sensor de Temperatura','Monitorea la temperatura del motor',10000,'kilómetros'),(12,'Modelo D','Diagnosticadodqwcsr multisensorial pro con tecnología de última generación, interfaz táctil y soporte remoto',123,'2024-09-06');
/*!40000 ALTER TABLE `componentes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `diagnosticos`
--

DROP TABLE IF EXISTS `diagnosticos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `diagnosticos` (
  `id_diagnostico` int NOT NULL AUTO_INCREMENT,
  `id_motocicleta` int NOT NULL,
  `id_componente` int NOT NULL,
  `fecha_diagnostico` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `tipo_falla` varchar(50) DEFAULT NULL,
  `descripcion` text,
  `solucion_sugerida` text,
  PRIMARY KEY (`id_diagnostico`),
  KEY `diagnosticos_ibfk_1` (`id_motocicleta`),
  KEY `diagnosticos_ibfk_2` (`id_componente`),
  CONSTRAINT `diagnosticos_ibfk_1` FOREIGN KEY (`id_motocicleta`) REFERENCES `motocicletas` (`id_motocicleta`) ON DELETE CASCADE,
  CONSTRAINT `diagnosticos_ibfk_2` FOREIGN KEY (`id_componente`) REFERENCES `componentes` (`id_componente`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `diagnosticos`
--

LOCK TABLES `diagnosticos` WRITE;
/*!40000 ALTER TABLE `diagnosticos` DISABLE KEYS */;
INSERT INTO `diagnosticos` VALUES (1,1,1,'2024-11-07 03:46:06','Voltaje bajo','El voltaje de la bateria es inferior al nivel nomral','Remplazar bateria');
/*!40000 ALTER TABLE `diagnosticos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `historial_mantenimiento`
--

DROP TABLE IF EXISTS `historial_mantenimiento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `historial_mantenimiento` (
  `id_mantenimiento` int NOT NULL AUTO_INCREMENT,
  `id_motocicleta` int NOT NULL,
  `fecha_mantenimiento` date NOT NULL,
  `tipo_mantenimiento` varchar(50) DEFAULT NULL,
  `detalles` text,
  PRIMARY KEY (`id_mantenimiento`),
  KEY `historial_mantenimiento_ibfk_1` (`id_motocicleta`),
  CONSTRAINT `historial_mantenimiento_ibfk_1` FOREIGN KEY (`id_motocicleta`) REFERENCES `motocicletas` (`id_motocicleta`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `historial_mantenimiento`
--

LOCK TABLES `historial_mantenimiento` WRITE;
/*!40000 ALTER TABLE `historial_mantenimiento` DISABLE KEYS */;
INSERT INTO `historial_mantenimiento` VALUES (1,1,'2024-10-09','Remplazo','Revision de bateria, atencion a terminales.');
/*!40000 ALTER TABLE `historial_mantenimiento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inventario`
--

DROP TABLE IF EXISTS `inventario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventario` (
  `id_inventario` int NOT NULL AUTO_INCREMENT,
  `id_modelo` int DEFAULT NULL,
  `cantidad_disponible` int DEFAULT NULL,
  `fecha_entrada` date DEFAULT NULL,
  `fecha_salida` date DEFAULT NULL,
  `estado_producto` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_inventario`),
  KEY `ventas_ibfk1_idx` (`id_modelo`),
  CONSTRAINT `ventas_ibfk1` FOREIGN KEY (`id_modelo`) REFERENCES `modelos` (`id_modelo`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventario`
--

LOCK TABLES `inventario` WRITE;
/*!40000 ALTER TABLE `inventario` DISABLE KEYS */;
INSERT INTO `inventario` VALUES (1,1,150,'2024-11-01',NULL,'Nuevo'),(2,2,200,'2024-11-03',NULL,'Nuevo'),(3,3,50,'2024-11-06',NULL,'Nuevo'),(4,1,30,'2024-11-10',NULL,'En Reparación'),(5,2,100,'2024-11-12',NULL,'Nuevo'),(8,2,100,'2024-11-12','2024-11-13','Nuevo');
/*!40000 ALTER TABLE `inventario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `modelos`
--

DROP TABLE IF EXISTS `modelos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `modelos` (
  `id_modelo` int NOT NULL AUTO_INCREMENT,
  `nombre_modelo` varchar(255) DEFAULT NULL,
  `descripcion` text,
  `precio` decimal(10,2) DEFAULT NULL,
  `fecha_lanzamiento` date DEFAULT NULL,
  PRIMARY KEY (`id_modelo`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `modelos`
--

LOCK TABLES `modelos` WRITE;
/*!40000 ALTER TABLE `modelos` DISABLE KEYS */;
INSERT INTO `modelos` VALUES (1,'Modelo A','Diagnosticador multisensorial básico con sensores estándar',500.00,'2024-01-15'),(2,'Modelo B','Diagnosticador multisensorial avanzado con sensores de alta precisión y conectividad Bluetooth',800.00,'2024-06-10'),(3,'Modelo C','Diagnosticador multisensorial pro con tecnología de última generación, interfaz táctil y soporte remoto',1300.00,'2024-09-05');
/*!40000 ALTER TABLE `modelos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `motocicleta_componentes`
--

DROP TABLE IF EXISTS `motocicleta_componentes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `motocicleta_componentes` (
  `id_motocicleta_componente` int NOT NULL AUTO_INCREMENT,
  `id_motocicleta` int NOT NULL,
  `id_componente` int NOT NULL,
  `cantidad` int DEFAULT '1',
  PRIMARY KEY (`id_motocicleta_componente`),
  KEY `id_motocicleta` (`id_motocicleta`),
  KEY `id_componente` (`id_componente`),
  CONSTRAINT `motocicleta_componentes_ibfk_1` FOREIGN KEY (`id_motocicleta`) REFERENCES `motocicletas` (`id_motocicleta`) ON DELETE CASCADE,
  CONSTRAINT `motocicleta_componentes_ibfk_2` FOREIGN KEY (`id_componente`) REFERENCES `componentes` (`id_componente`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `motocicleta_componentes`
--

LOCK TABLES `motocicleta_componentes` WRITE;
/*!40000 ALTER TABLE `motocicleta_componentes` DISABLE KEYS */;
INSERT INTO `motocicleta_componentes` VALUES (1,1,1,1),(2,1,2,1),(3,1,3,1),(4,1,4,1),(5,1,6,1),(6,1,7,1),(7,1,8,1),(8,1,9,1),(9,1,10,1);
/*!40000 ALTER TABLE `motocicleta_componentes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `motocicletas`
--

DROP TABLE IF EXISTS `motocicletas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `motocicletas` (
  `id_motocicleta` int NOT NULL AUTO_INCREMENT,
  `id_usuario` int NOT NULL,
  `marca` varchar(50) NOT NULL,
  `modelo` varchar(50) NOT NULL,
  `anio` year NOT NULL,
  `numero_serie` varchar(50) NOT NULL,
  `cilindrada` int DEFAULT NULL,
  `color` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id_motocicleta`),
  UNIQUE KEY `numero_serie` (`numero_serie`),
  KEY `motocicletas_ibfk_1` (`id_usuario`),
  CONSTRAINT `motocicletas_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id_usuario`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `motocicletas`
--

LOCK TABLES `motocicletas` WRITE;
/*!40000 ALTER TABLE `motocicletas` DISABLE KEYS */;
INSERT INTO `motocicletas` VALUES (1,1,'Italika','FT200',2024,'LLCK2EE47RA109728',200,'Rojo'),(2,4,'Honda','CB190R',2025,'CESKCSCARVS',400,'Azul');
/*!40000 ALTER TABLE `motocicletas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proveedores`
--

DROP TABLE IF EXISTS `proveedores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proveedores` (
  `id_proveedor` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `direccion` varchar(150) DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_proveedor`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proveedores`
--

LOCK TABLES `proveedores` WRITE;
/*!40000 ALTER TABLE `proveedores` DISABLE KEYS */;
INSERT INTO `proveedores` VALUES (1,'Juan Pérez',NULL,'5551234567','contacto@electronicanorte.com'),(2,'Maria López',NULL,'5557654321','ventas@techparts.com'),(3,'Pedro Martínez',NULL,'5559876543','info@sensoresavanzados.com');
/*!40000 ALTER TABLE `proveedores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `puntos_venta`
--

DROP TABLE IF EXISTS `puntos_venta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `puntos_venta` (
  `id_punto_venta` int NOT NULL AUTO_INCREMENT,
  `nombre_punto_venta` varchar(100) DEFAULT NULL,
  `ubicacion` varchar(100) DEFAULT NULL,
  `contacto` varchar(50) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_punto_venta`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `puntos_venta`
--

LOCK TABLES `puntos_venta` WRITE;
/*!40000 ALTER TABLE `puntos_venta` DISABLE KEYS */;
INSERT INTO `puntos_venta` VALUES (1,'Mototech CDMX','Av. Reforma 123, Ciudad de México, CDMX','5556781234','ventas@mototechcdmx.com'),(2,'Auto Partes del Norte','Calle Hidalgo 456, Monterrey, NL','8187654321','contacto@autopartesnorte.com'),(3,'Electro Moto Guadalajara','Blvd. Vallarta 789, Guadalajara, Jalisco','3336549870','ventas@electromotogdl.com'),(4,'Repuestos Zona Centro','Av. Central 555, Puebla, Puebla','2229988776','repuestos@zonacentro.com'),(5,'MotosBikers','Calle Libertad 1010, Querétaro, Querétaro','4421235566','ventas@motosymasqro.com');
/*!40000 ALTER TABLE `puntos_venta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sensores`
--

DROP TABLE IF EXISTS `sensores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sensores` (
  `id_sensor` int NOT NULL AUTO_INCREMENT,
  `id_componente` int NOT NULL,
  `tipo` varchar(50) NOT NULL,
  `rango_operacion` varchar(50) DEFAULT NULL,
  `unidad` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id_sensor`),
  KEY `sensores_ibfk_1` (`id_componente`),
  CONSTRAINT `sensores_ibfk_1` FOREIGN KEY (`id_componente`) REFERENCES `componentes` (`id_componente`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sensores`
--

LOCK TABLES `sensores` WRITE;
/*!40000 ALTER TABLE `sensores` DISABLE KEYS */;
INSERT INTO `sensores` VALUES (1,1,'Voltaje','12-14V','Voltios'),(2,10,'Temperatura','20-200°C','Celcius');
/*!40000 ALTER TABLE `sensores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trabajadores`
--

DROP TABLE IF EXISTS `trabajadores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `trabajadores` (
  `id_trabajador` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `puesto` varchar(50) DEFAULT NULL,
  `fecha_contratacion` date DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `id_punto_venta` int DEFAULT NULL,
  PRIMARY KEY (`id_trabajador`),
  KEY `id_punto_venta` (`id_punto_venta`),
  CONSTRAINT `trabajadores_ibfk_1` FOREIGN KEY (`id_punto_venta`) REFERENCES `puntos_venta` (`id_punto_venta`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trabajadores`
--

LOCK TABLES `trabajadores` WRITE;
/*!40000 ALTER TABLE `trabajadores` DISABLE KEYS */;
INSERT INTO `trabajadores` VALUES (1,'Carlos Rodríguez','Vendedor','2023-04-15','5551234567','carlos.rodriguez@mototechcdmx.com',1),(2,'Ana Gómez','Soporte Técnico','2023-06-20','8187654321','ana.gomez@autopartesnorte.com',2),(3,'Luis Martínez','Ingeniero de Producción','2022-09-05','3336549870','luis.martinez@electromotogdl.com',NULL),(4,'María López','Logística','2024-01-10','2229988776','maria.lopez@zonacentro.com',NULL);
/*!40000 ALTER TABLE `trabajadores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id_usuario` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `fecha_registro` date DEFAULT NULL,
  PRIMARY KEY (`id_usuario`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'Edgar Medina','edgarmedina@gmail.com','4641556077','2024-01-01'),(4,'Angel Medina','angelmedina@gmail.com','4641419970','2024-01-01'),(7,'Armando Casa','armando@gmail.com','4641234567','2024-01-01'),(8,'Pepe Pecas','pepepecas@gmail.com','4641874017','2024-01-03');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ventas`
--

DROP TABLE IF EXISTS `ventas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ventas` (
  `id_venta` int NOT NULL AUTO_INCREMENT,
  `id_modelo` int NOT NULL,
  `fecha_venta` date NOT NULL,
  `precio_venta` decimal(10,2) NOT NULL,
  `id_usuario` int DEFAULT NULL,
  `id_punto_venta` int DEFAULT NULL,
  PRIMARY KEY (`id_venta`),
  KEY `id_punto_venta` (`id_punto_venta`),
  KEY `ventas_ibfk_2_idx` (`id_modelo`),
  KEY `ventas_ibfk_2` (`id_usuario`),
  CONSTRAINT `ventas_ibfk_1` FOREIGN KEY (`id_modelo`) REFERENCES `modelos` (`id_modelo`) ON DELETE CASCADE,
  CONSTRAINT `ventas_ibfk_2` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id_usuario`) ON DELETE CASCADE,
  CONSTRAINT `ventas_ibfk_3` FOREIGN KEY (`id_punto_venta`) REFERENCES `puntos_venta` (`id_punto_venta`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ventas`
--

LOCK TABLES `ventas` WRITE;
/*!40000 ALTER TABLE `ventas` DISABLE KEYS */;
INSERT INTO `ventas` VALUES (1,1,'2024-11-01',500.00,1,1),(2,3,'2024-11-11',1300.00,7,3);
/*!40000 ALTER TABLE `ventas` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-01 18:01:04
