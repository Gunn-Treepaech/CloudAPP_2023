# 🚩Docker Swarm
  ### ติดตั้ง Docker ในระบบของคุณ
  ```sh
  sudo apt-get install docker.io
  ```
  ### แสดงความช่วยเหลือสำหรับคำสั่ง Docker ทั้งหมด
  ```sh
  sudo docker --help
  ```
  ### แสดงเวอร์ชันของ Docker ที่ติดตั้งในระบบของคุณ
  ```sh
  sudo docker --version
  ```
# 🚩Basic Docker Swarm Commands
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
  ### เปิด Docker container ที่ใช้ image Ubuntu ที่เวอร์ชันล่าสุดและเริ่ม Bash shell ภายใน container นั้น ๆ 
  ```sh
  sudo docker container run -it ubuntu:latest /bin/bash
  ```
  ### เข้าถึง Bash shell ภายใน Docker container ที่มีชื่อ "vigilant_borg" และทำให้คุณสามารถปฏิบัติกับคำสั่ง Bash ภายใน container นั้นได้
  ```sh
  sudo docker container exec -it vigilant_borg bash
  ```
  ### ใช้ในการหยุด (stop) Docker container ที่กำหนดโดยระบุชื่อหรือไอดีของ container นั้น ๆ
  ```sh
  docker stop [Container name or ID]
  ```
  ### ใช้ในการเริ่มต้น (start) Docker container ที่ถูกหยุดทำงาน (stopped) และยังคงอยู่ในระบบของคุณ
  ```sh
  sudo docker start [Container name or ID]
  ```
  ### ใช้แสดงรายการของ Docker containers ที่อยู่ในระบบ รวมถึง containers ที่หยุดทำงาน และ containers ที่กำลังทำงานทั้งหมด
  ```sh
  sudo docker container ls -a
  ```
  ```sh
  sudo docker ps -a
  ```
  ### ยกเลิกการทำงานของ container ทันที
  ```sh
  sudo docker container kill [Container name or ID]
  ```
