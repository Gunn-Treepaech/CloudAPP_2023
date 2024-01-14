# Docker
  ### ติดตั้ง Docker ในระบบของคุณ
  ```sh
  sudo apt-get install docker.io
  ```
  ### แสดงความช่วยเหลือ (help) สำหรับคำสั่ง Docker ทั้งหมด
  ```sh
  sudo docker --help
  ```
# Basic Docker Commands
  ### ดึง image ของ Node.js จาก Docker Hub ที่เวอร์ชันล่าสุดมาที่เครื่องของคุณ
  ```sh
  sudo docker image pull node:latest
  ```
  ### แสดงรายการของ Docker images ที่อยู่ในเครื่อง
  ```sh
  sudo docker image ls
  ```
  ### สร้างและเริ่มต้น Docker container โดยใช้ images Node.js เวอร์ชันล่าสุด, ทำให้ container นี้ทำงานใน background (-d), map พอร์ต 5000 ของเครื่อง host ไปยังพอร์ต 5000 ของ container (-p), และตั้งชื่อ container เป็น "node" (--name)
  ```sh
  sudo docker container run -d -p 5000:5000 --name node node:latest
  ```
  ### แสดงรายการของ Docker containers ที่กำลังทำงาน
  ```sh
  sudo docker container ps
  ```
  ### หยุด Docker container ที่ชื่อ "node" หรือใช้ไอดีของ container
  ```sh
  sudo docker container stop node (or <container id>)
  ```
  ### ลบ Docker container ที่ชื่อ "node" หรือใช้ไอดีของ container
  ```sh
  sudo docker container rm node (or <container id>)
  ```
  ### ลบ Docker image จากระบบ โดยใช้ชื่อ image หรือไอดีของ image
  ```sh
  sudo docker image rmi (or <image id>)
  ```
  ### สร้าง Docker image ใหม่โดยใช้ Dockerfile ที่อยู่ในไดเรกทอรีปัจจุบัน (-t กำหนดชื่อและเวอร์ชัน)
  ```sh
  sudo docker build -t node:2.0 .
  ```
  ### ส่ง Docker image ที่ชื่อ "node" และเวอร์ชัน 2.0 ขึ้นไปยัง Docker Hub หรือเครื่อง Registry ที่กำหนด
  ```sh
  sudo docker image push node:2.0
  ```
  ### 
  ```sh
     
  ```
  ### 
  ```sh
     
  ```
  ### 
  ```sh
     
  ```
  ### 
  ```sh
     
  ```
  ### 
  ```sh
     
  ```
  ### 
  ```sh
     
  ```
  ### 
  ```sh
     
  ```
