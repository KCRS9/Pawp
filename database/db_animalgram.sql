
DROP DATABASE IF EXISTS `animal_shelter_db`;
CREATE DATABASE `animal_shelter_db` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_uca1400_ai_ci;
USE `animal_shelter_db`;

CREATE TABLE `USER` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `email` varchar(150) NOT NULL,
  `password` varchar(255) NOT NULL,
  `role` enum('admin','user','shelter') NOT NULL,
  `location` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
);

CREATE TABLE `SHELTER` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `address` varchar(255) NOT NULL,
  `contact` varchar(100) NOT NULL,
  `website` varchar(150) NOT NULL,
  `description` text NOT NULL,
  `admin` int NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`admin`) REFERENCES `USER`(`id`) ON DELETE CASCADE
);

CREATE TABLE `ANIMAL` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `species` varchar(100) NOT NULL,
  `breed` varchar(100) NOT NULL,
  `age` int NOT NULL,
  `size` enum('small','medium','large') NOT NULL,
  `description` text,
  `status` enum('available','adopted','reserved','other') NOT NULL,
  `shelter` int NOT NULL,
  `health` text,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`shelter`) REFERENCES `SHELTER`(`id`) ON DELETE CASCADE
);

CREATE TABLE `POST` (
  `id` int NOT NULL AUTO_INCREMENT,
  `photo` varchar(255) NOT NULL,
  `animal` int NOT NULL,
  `likes` int NOT NULL DEFAULT 0,
  `user` int NOT NULL,
  `text` text,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`animal`) REFERENCES `ANIMAL`(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`user`) REFERENCES `USER`(`id`) ON DELETE CASCADE
);

CREATE TABLE `COMMENT` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user` int NOT NULL,
  `post` int NOT NULL,
  `text` text NOT NULL,
  `date` datetime NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user`) REFERENCES `USER`(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`post`) REFERENCES `POST`(`id`) ON DELETE CASCADE
);

CREATE TABLE `FAVORITE` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user` int NOT NULL,
  `animal` int NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user`) REFERENCES `USER`(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`animal`) REFERENCES `ANIMAL`(`id`) ON DELETE CASCADE
);

CREATE TABLE `ADOPTION` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user` int NOT NULL,
  `shelter` int NOT NULL,
  `animal` int NOT NULL,
  `status` enum('pending','approved','rejected','completed') NOT NULL,
  `date` date NOT NULL,
  `time` time NOT NULL,
  `text` text NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user`) REFERENCES `USER`(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`animal`) REFERENCES `ANIMAL`(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`shelter`) REFERENCES `SHELTER`(`id`) ON DELETE CASCADE
);

CREATE TABLE `RESERVATION` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user` int NOT NULL,
  `animal` int NOT NULL,
  `shelter` int NOT NULL,
  `date` date NOT NULL,
  `time` time NOT NULL,
  `status` enum('pending','confirmed','cancelled','completed') NOT NULL,
  `text` text NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user`) REFERENCES `USER`(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`animal`) REFERENCES `ANIMAL`(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`shelter`) REFERENCES `SHELTER`(`id`) ON DELETE CASCADE
);

