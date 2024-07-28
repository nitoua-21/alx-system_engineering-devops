-- Setup Mysql Replication
-- https://www.digitalocean.com/community/tutorials/how-to-set-up-replication-in-mysql --

-- Primary Db--
CREATE USER IF NOT EXISTS holberton_user@localhost IDENTIFIED BY "projectcorrection280hbtn";
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
CREATE DATABASE IF NOT EXISTS tyrell_corp;
USE tyrell_corp;
CREATE TABLE IF NOT EXISTS nexus6(id INT PRIMARY KEY AUTO_INCREMENT, name TEXT);
INSERT INTO  nexus6 (name) VALUES ("Jarvis");
GRANT SELECT ON tyrell_corp.nexus6 TO holberton_user@localhost;
CREATE USER IF NOT EXISTS replica_user@'%' IDENTIFIED BY "replica_user";
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';
CREATE USER web02@54.174.121.226 IDENTIFIED BY "web02";
GRANT REPLICATION SLAVE ON *.* TO web02@54.174.121.226;

-- Replica Db
CHANGE MASTER TO MASTER_HOST='52.91.150.244', MASTER_USER='web02', MASTER_PASSWORD='web02', MASTER_LOG_FILE='mysql-bin.000191', MASTER_LOG_POS=775;
