create database mca_b1;
use mca_b1;
select * from emp_2;
CREATE TABLE DEPARTMENT (
 DID INT PRIMARY KEY ,
    DNAME VARCHAR(20)
);

INSERT INTO department VALUES
(1, 'DEVELOPER'),
(2, 'HR'),
(3, 'SALES'),
(4, 'FINANCE'),
(5, 'SUPPORT');

CREATE TABLE EMPLOYEE (
 EID INT PRIMARY KEY ,
    ENAME VARCHAR(20) NOT NULL ,
    SALARY INT CHECK(SALARY > 0 ),
    DESIGNATION VARCHAR(20) NOT NULL ,
    D_ID INT ,
 foreign key(D_ID) REFERENCES DEPARTMENT(DID)
    ON UPDATE CASCADE 
    ON DELETE CASCADE 
);
INSERT INTO employee VALUES
(1, 'VISHAKHA', 10000, 'DA', 1),
(2, 'CHITRALI', 40000, 'RECRUITER', 2),
(3, 'SAYALI', 100000, 'MARKETING', 3),
(4, 'HARSHDA', 20000, 'JAVA', 1),
(5, 'GAYATRI', 10000, 'EDITOR', 3),
(6, 'YASHSAVI', 40000, 'TESTER', 4),
(7, 'PRAVEEN', 80000, 'DA', 2),
(8, 'HARSH', 90000, 'BA', 4),
(9, 'SNEHAL', 25000, 'INTERN', NULL);

# find emp with their department names
#Inner join => it return matching records from both the tables 

select e.EID , e.ename , d.dname from employee e inner join
department d on e.D_ID = d.DID;
select * from employee;

-- Emp with their records , dname and salaries > 50000
select e.EID , e.ename ,e.designation,e.salary, d.dname
 from employee e inner join
department d on e.D_ID = d.DID where e.salary > 50000;

-- Left Join => fetches all records of left table and matching records of right table
select e.EID , e.ename ,e.designation,e.salary, d.dname from 
employee e left join department d on e.D_ID = d.DID;

-- Self join => fetch record of employees who works in same dept
select e1.EID , e1.ename , e1.designation from employee e1 join
employee e2 on e1.eid <> e2.eid and e1.designation = e2.designation
order by e1.designation;

-- subquery = query inside a query AKA nested Query. 
-- find highest paid emp 
-- select max(salary) from employee;

select * from employee
 where salary = (select max(salary) from 
employee);





















CREATE TABLE Vehicle (
vehicle_id INT PRIMARY KEY,
vehicle_name VARCHAR(30),
price INT,
fuel_type VARCHAR(20),
color VARCHAR(20),
number_of_tyres INT
);

INSERT INTO Vehicle VALUES
(1, 'Honda City', 1200000, 'Petrol', 'White', 4),
(2, 'Swift', 800000, 'Petrol', 'Red', 4),
(3, 'Creta', 1500000, 'Diesel', 'Black', 4),
(4, 'Royal Enfield', 220000, 'Petrol', 'Black', 2),
(5, 'Activa', 90000, 'Petrol', 'Grey', 2),
(6, 'KTM Duke', 280000, 'Petrol', 'Orange', 2),
(7, 'Tata Truck', 2500000, 'Diesel', 'Blue', 10),
(8, 'Ashok Leyland Truck', 3000000, 'Diesel', 'White', 12),
(9, 'Volvo Bus', 4500000, 'Diesel', 'Red', 6),
(10, 'Mini Bus', 1800000, 'Diesel', 'Yellow', 6),
(11, 'Auto Rickshaw', 350000, 'CNG', 'Green', 3),
(12, 'Eeco Van', 600000, 'CNG', 'White', 4),
(13, 'Bolero', 1100000, 'Diesel', 'Silver', 4),
(14, 'Scorpio', 1600000, 'Diesel', 'Black', 4),
(15, 'BMW Car', 5500000, 'Petrol', 'Blue', 4),
(16, 'Audi Car', 6000000, 'Petrol', 'White', 4),
(17, 'Tractor', 900000, 'Diesel', 'Green', 4),
(18, 'School Bus', 3200000, 'Diesel', 'Yellow', 6),
(19, 'Pickup Truck', 1400000, 'Diesel', 'Grey', 4),
(20, 'Electric Car', 1800000, 'Electric', 'White', 4); 













