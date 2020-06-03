DROP TABLE IF EXISTS `weather`;

CREATE TABLE `weather` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `city_id` int(11) NOT NULL,
  `date` date NOT NULL,
  `time` time NOT NULL,
  `weather_id` int(11) DEFAULT NULL,
  `description` tinytext NOT NULL,
  `icon` tinytext NOT NULL,
  `temp` decimal(10,2) NOT NULL,
  `temp_min` decimal(10,2) NOT NULL,
  `temp_max` decimal(10,2) NOT NULL,
  `pressure` int(11) NOT NULL,
  `humidity` int(11) NOT NULL,
  `wind_speed` decimal(10,2) NOT NULL,
  `wind_direction` smallint(4) NOT NULL,
  `cloudiness` tinyint(4) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;