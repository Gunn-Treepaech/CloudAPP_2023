# 🚩Deploy a stack to a swarm
  ### Refer 
  - [Deploy a stack to a swarm](https://docs.docker.com/engine/swarm/stack-deploy/)
  ## ขั้นตอนที่ 1 push images ขึ้น docker hub
  ### ใช้ login docker hub
  ```sh
  sudo docker login
  ```
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
  ### หยุดการทำงานของ Docker Compose โปรเจคปัจจุบันและลบทุก volume ที่ถูกสร้างขึ้น
  ```sh
  sudo docker-compose down --volumes
  ```
  ### ส่ง images Docker และบริการที่กำหนดไว้ในไฟล์ docker-compose.yml ไปยัง Docker Registry
  ```sh
  sudo docker-compose push
  ```
  ## ขั้นตอนที่ 2 Deploy the stack to the swarm
  ### ใช้สร้างและเริ่มต้น Docker stack โปรเจคจากไฟล์ compose.yml ที่มีชื่อ stack เป็น "stackdemo"
  ```sh
  sudo docker stack deploy --compose-file compose.yml stackdemo
  ```
  ### แสดงรายการของบริการที่ให้บริการใน Docker stack ที่มีชื่อ "stackdemo"
  ```sh
  sudo docker stack services stackdemo
  ```
  ### แสดงรายการของ tasks (งาน) ที่เกี่ยวข้องกับ Docker stack ที่ชื่อ stackdemo
  ```sh
  sudo docker stack ps stackdemo
  ```
  ### หยุดและลบทั้งหมดของ Docker stack ที่มีชื่อ "stackdemo"
  ```sh
  sudo docker stack rm stackdemo
  ```
