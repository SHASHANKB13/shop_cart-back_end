CREATE DATABASE  IF NOT EXISTS `shopping_app` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `shopping_app`;
-- MySQL dump 10.13  Distrib 8.0.31, for macos12 (x86_64)
--
-- Host: localhost    Database: shopping_app
-- ------------------------------------------------------
-- Server version	8.0.31

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
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `category` varchar(255) DEFAULT NULL,
  `imageUrl` varchar(255) DEFAULT NULL,
  `created_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `description` varchar(500) DEFAULT NULL,
  `rating` decimal(10,2) DEFAULT '0.00',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (1,'Apple iphone 15 pro max (1TB)',129999.00,'MOBILE','https://media-ik.croma.com/prod/https://media.croma.com/image/upload/v1708677095/Croma%20Assets/Communication/Mobiles/Images/300749_0_hyore5.png','2024-03-26 09:33:56','2024-03-26 09:33:56',NULL,NULL),(2,'Apple iphone 15 pro max (256gb)',129999.00,'MOBILE','https://www.halabh.com/cdn/shop/files/100345724_100_01_1024x.webp?v=1699421459','2024-03-26 09:35:23','2024-03-26 09:35:23',NULL,NULL),(3,'Oneplus 12pro 256gb',59999.00,'MOBILE','https://techring.in/wp-content/uploads/2023/01/OnePlus-12-Pro.jpg','2024-03-26 09:39:24','2024-04-11 04:15:26','4 GB RAM | 128 GB ROM | Expandable Upto 1 TB, 16.51 cm (6.5 inch) Full HD+ Display, 50MP + 5MP + 2MP | 13MP Front Camera</p>, 6000 mAh Lithium ion Battery, MediaTek Dimensity 6100+ Processor',4.20),(4,'Apple iphone 15 256gb',89999.00,'MOBILE','https://img-prd-pim.poorvika.com/cdn-cgi/image/width=500,height=500,quality=75/product/apple-iphone-15-Blue-128gb-back-view.png','2024-03-26 09:39:24','2024-03-26 09:39:24',NULL,NULL),(5,'Samsung M14 256gb',19999.00,'MOBILE','https://media-ik.croma.com/prod/https://media.croma.com/image/upload/v1709106355/Croma%20Assets/Communication/Mobiles/Images/305189_o2qnku.png','2024-03-26 09:39:24','2024-03-26 09:39:24',NULL,NULL),(6,'Samsung S23 128gb',49999.00,'MOBILE','https://images.samsung.com/is/image/samsung/p6pim/in/sm-s711bzbcins/gallery/in-galaxy-s23-fe-s711-sm-s711bzbcins-thumb-538353662','2024-03-26 09:39:24','2024-03-26 09:39:24',NULL,NULL),(7,'Apple iphone 15 256gb',78000.00,'MOBILE','https://media-ik.croma.com/prod/https://media.croma.com/image/upload/v1708672728/Croma%20Assets/Communication/Mobiles/Images/261934_0_kukyat.png?tr=w-600','2024-03-26 09:39:24','2024-03-26 09:39:24',NULL,NULL),(8,'Samsung A23 128gb',32000.00,'MOBILE','https://images.samsung.com/is/image/samsung/p6pim/uk/sm-a346bzsaeub/gallery/uk-galaxy-a34-5g-sm-a346-sm-a346bzsaeub-thumb-535769863','2024-03-26 09:39:24','2024-03-26 09:39:24',NULL,NULL),(9,'Printed t-shirt style-1',699.00,'CLOTHING','https://assets.ajio.com/medias/sys_master/root/20230626/GqCN/64998077a9b42d15c9f29f54/-473Wx593H-466275408-white-MODEL.jpg','2024-03-26 12:12:28','2024-03-26 12:12:28',NULL,NULL),(10,'Printed full sleeves t-shirt',999.00,'CLOTHING','https://assets.ajio.com/medias/sys_master/root/20220411/6r9R/6253e85ff997dd03e2547c10/-473Wx593H-462876014-black-MODEL.jpg','2024-03-26 12:13:31','2024-03-26 12:13:31',NULL,NULL),(11,'Girls white t-shirt plain',499.00,'CLOTHING','https://assets.ajio.com/medias/sys_master/root/h84/h86/15210327015454/-473Wx593H-460542987-white-MODEL.jpg','2024-03-26 12:16:25','2024-03-26 12:18:35',NULL,NULL),(12,'Girls black t-shirt plain',399.00,'CLOTHING','https://rukminim2.flixcart.com/image/850/1000/xif0q/t-shirt/p/i/n/l-oversized-t-shirt-equal-original-imagx7n65cp5gjha.jpeg?q=20&crop=false','2024-03-26 12:17:36','2024-03-26 12:17:36',NULL,NULL),(13,'Oneplus 10 Pro',70000.00,'MOBILE','https://media-ik.croma.com/prod/https://media.croma.com/image/upload/v1680399705/Croma%20Assets/Communication/Mobiles/Images/250718_mfxhnx.png?tr=w-600','2024-03-27 11:35:42','2024-03-27 11:35:42',NULL,NULL),(14,'Oneplus Open Folding phone 5G',139000.00,'MOBILE','https://www.clove.co.uk/cdn/shop/files/OnePlusOpen-emerald-dusk-open2_1200x.jpg?v=1709133757','2024-03-27 11:38:50','2024-03-27 11:45:54',NULL,NULL),(15,'Samsung flip 3 5G',59999.00,'MOBILE','https://images.samsung.com/nz/smartphones/galaxy-z-flip4/buy/Flip4_Carousel_ProductKV_Graphite_MO.jpg','2024-03-27 11:40:13','2024-03-27 11:43:07',NULL,NULL),(16,'Samsung fold 5G',99999.00,'MOBILE','https://images.samsung.com/uk/smartphones/galaxy-z-fold4/buy/03_Product-Image_Basic-Color/2_Q4_KV_MO_Phantomblack_notext.jpg','2024-03-27 11:41:13','2024-03-27 11:42:25',NULL,NULL),(17,'Westside casual western wear',2999.00,'CLOTHING','https://cdn.shopify.com/s/files/1/0266/6276/4597/files/long_dresses_for_women_by_lov_5d3cfc80-5d8e-41c4-955f-fbbcba542e56.jpg?v=1651054811','2024-04-01 11:39:39','2024-04-01 11:39:39',NULL,NULL),(18,'pantene lively clean shampoo',499.00,'GROCERIES','https://www.bigbasket.com/media/uploads/p/l/20004724_11-pantene-advanced-hair-care-solution-shampoo-lively-clean.jpg','2024-04-01 11:47:06','2024-04-01 11:47:06',NULL,NULL),(19,'Cadbury silk fruit and nut',120.00,'GROCERIES','https://www.bigbasket.com/media/uploads/p/l/100265003-2_8-cadbury-dairy-milk-silk-fruit-nut-chocolate-bar.jpg','2024-04-01 11:48:28','2024-04-01 11:48:28',NULL,NULL),(20,'Black dog single malt whiskey 750ml',3500.00,'GROCERIES','https://www.spencers.in/media/catalog/product/1/0/1087299.jpg','2024-04-01 11:52:22','2024-04-01 11:52:22',NULL,NULL);
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-24 11:59:15
