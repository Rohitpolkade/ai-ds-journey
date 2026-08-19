CREATE DATABASE IF NOT EXISTS CollegeDB;
USE CollegeDB;
SELECT DATABASE();

CREATE TABLE Students(
StudentID INT AUTO_INCREMENT PRIMARY KEY,
Name VARCHAR(100),
Age TINYINT,
Email VARCHAR(100),
JoinDate DATE
);

SHOW TABLES;

DESCRIBE Students;

SELECT * FROM Students;

INSERT INTO Students(Name, Age, Email, JoinDate)
VALUES
('Rohit Polkade', 20, 'rp@email.com', '2026-08-18'),
('Kabir Polkade', 21, 'kb@email.com', '2026-08-19');