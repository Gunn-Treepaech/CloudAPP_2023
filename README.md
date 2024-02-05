## CloudAPP 2023 By Gun
# 🚩MySQL Command
  ### Refer 
  - [Getting Started with MySQL](https://dev.mysql.com/doc/mysql-getting-started/en/)
  - [Install MySQL Server on the Ubuntu operating system](https://docs.rackspace.com/docs/install-mysql-server-on-the-ubuntu-operating-system)
  ### ติดตั้ง MySQL Server
  ```sh
  sudo apt-get install mysql-server
  ```
  ### เชื่อมต่อกับเซิร์ฟเวอร์ MySQL ที่ทำงานบน localhost ด้วยพอร์ต 3306 โดยใช้โปรโตคอล TCP โดยใช้ผู้ใช้รูท
  ```sh
  mysql -h localhost -P 3306 --protocol=tcp -u root -p
  ```
  ### ใช้เพื่อออกจากการเชื่อมต่อกับ MySQL Server
  ```sh
  QUIT
  ```
  ### แสดงรายชื่อฐานข้อมูลทั้งหมดที่มีใน MySQL Server
  ```sh
  SHOW DATABASES;
  ```
  ### สร้างฐานข้อมูลชื่อ "pets"
  ```sh
  CREATE DATABASE pets;
  ```
  ### เปลี่ยนฐานข้อมูลที่กำลังใช้อยู่เป็น "pets"
  ```sh
  USE pets
  ```
  ### สร้างตาราง "cats" ในฐานข้อมูล "pets" ด้วยคอลัมน์ที่กำหนดไว้
  ```sh
  CREATE TABLE cats
  (
    id              INT unsigned NOT NULL AUTO_INCREMENT, # Unique ID for the record
    name            VARCHAR(150) NOT NULL,                # Name of the cat
    owner           VARCHAR(150) NOT NULL,                # Owner of the cat
    birth           DATE NOT NULL,                        # Birthday of the cat
    PRIMARY KEY     (id)                                  # Make the id the primary key
  );
  ```
  ### แสดงรายชื่อตารางทั้งหมดในฐานข้อมูล "pets"
  ```sh
  SHOW TABLES;
  ```
  ### แสดงโครงสร้างของตาราง "cats" เพื่อดูรายละเอียดของคอลัมน์
  ```sh
  DESCRIBE cats;
  ```
  ### เพิ่มข้อมูลแถวในตาราง "cats" ด้วยข้อมูลที่กำหนด
  ```sh
  INSERT INTO cats ( name, owner, birth) VALUES
  ( 'Sandy', 'Lennon', '2015-01-03' ),
  ( 'Cookie', 'Casey', '2013-11-13' ),
  ( 'Charlie', 'River', '2016-05-21' );
  ```
  ### แสดงข้อมูลทั้งหมดในตาราง "cats"
  ```sh
  SELECT * FROM cats;
  ```
  ### เลือกแสดงชื่อของแมวที่เป็นเจ้าของโดยกำหนดเงื่อนไขว่าเจ้าของเป็น 'Casey'
  ```sh
  SELECT name FROM cats WHERE owner = 'Casey';
  ```
  ### ลบข้อมูลแถวที่มีชื่อเป็น 'Cookie' จากตาราง "cats"
  ```sh
  DELETE FROM cats WHERE name='Cookie';
  ```
  ### เพิ่มคอลัมน์ "gender" ที่มีชนิดข้อมูล CHAR(1) หลังจากคอลัมน์ "name" ในตาราง "cats"
  ```sh
  ALTER TABLE cats ADD gender CHAR(1) AFTER name;
  ```
  ### ลบคอลัมน์ "gender" จากตาราง "cats"
  ```sh
  ALTER TABLE cats DROP gender;
  ```