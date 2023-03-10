DROP TABLE IF EXISTS `time_zone`;
CREATE TABLE `time_zone` (
	`zone_name` VARCHAR(35) NOT NULL,
	`country_code` CHAR(2) NOT NULL,
	`abbreviation` VARCHAR(6) NOT NULL,
	`time_start` INT NOT NULL,
	`gmt_offset` INT NOT NULL,
	`dst` CHAR(1) NOT NULL,
	INDEX `idx_zone_name` (`zone_name`),
	INDEX `idx_time_start` (`time_start`)
) COLLATE='utf8_bin' ENGINE=MyISAM;

LOAD DATA LOCAL INFILE 'time_zone.csv' INTO TABLE `time_zone` FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n';

