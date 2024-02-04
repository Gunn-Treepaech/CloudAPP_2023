# 🚩Deploy a stack to a swarm
  ### Refer 
  - [Deploy a stack to a swarm](https://docs.docker.com/engine/swarm/stack-deploy/)
  ### ใช้ติดตั้ง Docker Compose
  ```sh
  sudo apt-get install docker-compose
  ```
  ### ใช้เริ่มต้นและทำงาน Docker Compose โปรเจคที่กำหนดไว้ในไฟล์ docker-compose.yml ในโหมดที่ไม่บล็อก (detached mode)
  ```sh
  sudo docker-compose up -d
  ```
  ### แสดงสถานะของทุกบริการที่กำหนดใน Docker Compose โปรเจคปัจจุบัน
  ```sh
  sudo docker-compose ps
  ```
  ### ใช้ทดสอบการเรียกใช้บริการที่ทำงานบน localhost ที่พอร์ต 8000 ด้วยคำสั่ง curl
  ```sh
  curl http://localhost:8000
  ```
  ### หยุดการทำงานของ Docker Compose โปรเจคปัจจุบันและลบทุก volume ที่ถูกสร้างขึ้น
  ```sh
  sudo docker-compose down --volumes
  ```
  ### ใช้สร้างและเริ่มต้น Docker stack โปรเจคจากไฟล์ compose.yml ที่มีชื่อ stack เป็น "stackdemo"
  ```sh
  sudo docker stack deploy --compose-file compose.yml stackdemo
  ```
  ### แสดงรายการของบริการที่ให้บริการใน Docker stack ที่มีชื่อ "stackdemo"
  ```sh
  sudo docker stack services stackdemo
  ```
  ### หยุดและลบทั้งหมดของ Docker stack ที่มีชื่อ "stackdemo"
  ```sh
  sudo docker stack rm stackdemo
  ```
  ### ทำให้โหนดปลดจาก Docker Swarm ด้วยการออกจาก Swarm โดยบังคับให้ออกโดยไม่ต้องการยืนยัน
  ```sh
  sudo docker swarm leave --force
  ```
