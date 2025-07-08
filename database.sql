CREATE DATABASE company;
USE company;

CREATE TABLE employee (
    serial INT PRIMARY KEY AUTO_INCREMENT,
    emp_id VARCHAR(20) NOT NULL,
    emp_name VARCHAR(100) NOT NULL,
    designation VARCHAR(50),
    department VARCHAR(50)
);
INSERT INTO employee (emp_id, emp_name, designation, department)
VALUES ('EMP001', 'Anushka', 'Developer', 'Software'),
       ('EMP002', 'Kalyan', 'Tester', 'Software'),
       ('EMP003', 'Varsha', 'Analyst', 'Software');
