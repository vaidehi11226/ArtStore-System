-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 19, 2021 at 03:32 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `mainartstore`
--

-- --------------------------------------------------------

--
-- Table structure for table `artinfo`
--

CREATE TABLE `artinfo` (
  `proid` varchar(100) NOT NULL,
  `proname` varchar(100) NOT NULL,
  `brand` varchar(100) NOT NULL,
  `setofno` int(100) NOT NULL,
  `price` int(100) NOT NULL,
  `stock` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `artinfo`
--

INSERT INTO `artinfo` (`proid`, `proname`, `brand`, `setofno`, `price`, `stock`) VALUES
('ART100101', 'ACRYLIC COLOR', 'WINSON & NEWTON', 12, 700, 'AVAILABLE'),
('ART100102', 'ACRYLIC COLOR', 'WINSON & NEWTON', 24, 1200, 'AVAILABLE'),
('ART100103', 'GOUACHE COLOR', 'MONT MARTE', 12, 500, 'AVAILABLE'),
('ART100104', 'GOUACHE COLOR', 'MONT MARTE', 24, 1000, 'NOT AVAILABLE'),
('ART100105', 'GOUACHE COLOR', 'BRUSTRO', 12, 800, 'AVAILABLE'),
('ART100106', 'ACRYLIC COLOR', 'CAMEL', 12, 500, 'AVAILABLE'),
('ART100107', 'CANVAS BOARD BIG', 'BRUSTRO', 2, 1000, 'AVAILABLE'),
('ART100108', 'CANVAS BOARD SMALL', 'BRUSTRO', 2, 600, 'AVAILABLE'),
('ART100109', 'WATER COLOR', 'WINSON & NEWTON', 24, 1000, 'AVAILABLE'),
('ART100110', 'PAINTING KNIVES', 'BRUSTRO', 12, 1200, 'AVAILABLE'),
('ART100111', '300GSM A5SIZE WHITE PAPER', 'CAMEL', 50, 400, 'AVAILABLE'),
('ART100112', '300GSM A5 SIZE BLACK PAPER', 'MONT MARTE', 100, 600, 'AVAILABLE'),
('ART100113', 'SOFT PASTEL', 'BRUSTRO', 12, 500, 'NOT AVAILABLE'),
('ART100114', 'SOFT PASTEL', 'MONT MARTE', 24, 1000, 'AVAILABLE'),
('ART100115', 'OIL PASTEL', 'WINSON & NEWTON', 12, 300, 'AVAILABLE'),
('ART100116', 'OIL COLOR', 'BRUSTRO', 24, 1500, 'AVAILABLE'),
('ART100117', 'EASEL BIG', 'MONT MARTE', 2, 2000, 'AVAILABLE'),
('ART100118', 'EASEL SMALL', 'BRUSTRO', 5, 3000, 'AVAILABLE'),
('ART100119', 'ACRYLIC BRUSHES', 'WINSON & NEWTON', 12, 500, 'AVAILABLE'),
('ART100120', 'WATERCOLOR BRUSHES', 'BRUSTRO', 6, 200, 'AVAILABLE'),
('ART100121', 'OIL COLOR BRUSHES', 'MONT MARTE', 12, 600, 'AVAILABLE'),
('ART100122', 'MATTE VARNISH', 'BRUSTRO', 1, 1000, 'AVAILABLE'),
('ART100123', 'GLOSS VARNISH', 'BRUSTRO', 1, 900, 'AVAILABLE'),
('ART100124', 'WATER COLOR', 'BRUSTRO', 32, 1000, 'AVAILABLE'),
('ART100125', 'PENCIL COLOR', 'PRISMA', 72, 14000, 'AVAILABLE'),
('ART100127', 'ACRYLIC COLOR', 'BRUSTRO', 24, 1000, 'NOT AVIALABLE'),
('ART100126', 'PENCIL COLOR', 'CAMEL', 50, 600, 'AVAILABLE'),
('ART100128', 'OIL COLOR', 'CAMEL', 10, 400, 'AVAILABLE'),
('ART100129', 'PAINTING KNIVES', 'MONT MARTE', 5, 300, 'AVAILABLE'),
('ART100130', 'ACRYLIC BRUSHES', 'BRUSTRO', 12, 600, 'AVAILABLE'),
('ART100131', 'GLOSS VARNISH', 'CAMEL', 1, 600, 'AVAILABLE'),
('ART100132', 'EASEL BIG', 'WINSON & NEWTON', 4, 15000, 'AVAILABLE');

-- --------------------------------------------------------

--
-- Table structure for table `billgenerate`
--

CREATE TABLE `billgenerate` (
  `proid` varchar(11) NOT NULL,
  `proname` varchar(100) NOT NULL,
  `brand` varchar(100) NOT NULL,
  `setofno` int(100) NOT NULL,
  `price` int(100) NOT NULL,
  `quantity` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `billgenerate`
--

INSERT INTO `billgenerate` (`proid`, `proname`, `brand`, `setofno`, `price`, `quantity`) VALUES
('ART100107', 'CANVAS BOARD BIG', 'BRUSTRO', 2, 1000, 2),
('ART100103', 'GOUACHE COLOR', 'MONT MARTE', 12, 500, 3),
('ART100131', 'GLOSS VARNISH', 'CAMEL', 1, 600, 1),
('ART100128', 'OIL COLOR', 'CAMEL', 10, 400, 1);

-- --------------------------------------------------------

--
-- Table structure for table `loginform`
--

CREATE TABLE `loginform` (
  `username` varchar(20) NOT NULL,
  `password` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `loginform`
--

INSERT INTO `loginform` (`username`, `password`) VALUES
('vaidehi', 1111),
('vrushti', 123),
('hetal', 567);

-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `Name` varchar(100) NOT NULL,
  `Mobile_no` varchar(100) NOT NULL,
  `emailid` varchar(100) NOT NULL,
  `state` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`Name`, `Mobile_no`, `emailid`, `state`, `address`, `password`) VALUES
('vaidehi', '695868795', 'darji@gmail.com', 'Madhya pradesh', '204,bhopal', '1111'),
('hetal', '43546584791', 'hdarji@gmail.com', 'kerela', '23,gandhin,103301', 'pn12'),
('drashti', '5465676982', 'dsanghvi@gmail.com', 'Goa', '2,bvsh 405517', 'ds09');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
