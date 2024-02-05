# 🚩Basic Docker Swarm Commands
  ### Refer 
  - [Docker Swarm Cheatsheet](https://github.com/sematext/cheatsheets/blob/master/docker-swarm-cheatsheet.md)
  ### เริ่มต้นการสร้าง Docker Swarm และทำให้เครื่องปัจจุบันเป็น Manager Node ใน Swarm
  ```sh
  sudo docker swarm init
  ```
  ### แสดงรายการของโหนดทั้งหมดใน Docker Swarm พร้อมข้อมูลเพิ่มเติมเกี่ยวกับแต่ละโหนด
  ```sh
  sudo docker node ls
  ```
  ### ใช้แสดง token ที่ใช้ในการเชื่อมต่อ Worker Node เข้าสู่ Docker Swarm
  ```sh
  sudo docker swarm join-token worker
  ```
  ### ใช้แสดงรายการของ services ทั้งหมดที่กำลังทำงานใน Docker Swarm
  ```sh
  sudo docker service ls
  ```
  ### ใช้แสดงรายการของ tasks ที่เกี่ยวข้องกับ service ที่ระบุใน Docker Swarm
  ```sh
  sudo docker service ps service_name
  ```
  ### ใช้ลบ service ที่กำลังทำงานใน Docker Swarm
  ```sh
  sudo docker service rm service_name
  ```
  ### ใช้ในการเริ่มต้นการตั้งค่า stack ใน Docker Swarm โดยใช้ไฟล์ docker-compose.yml และระบุชื่อ stack เพื่อให้ Swarm ทำการดำเนินการตามการตั้งค่าที่ระบุ
  ```sh
  sudo docker stack deploy -c docker-compose.yml stack_name
  ```
  ### ใช้แสดงรายการของ stacks ทั้งหมดที่กำลังทำงานใน Docker Swarm
  ```sh
  sudo docker stack ls
  ```
  ### ใช้แสดงรายการของ stacks ทั้งหมดที่กำลังทำงานใน Docker Swarm
  ```sh
  sudo docker stack ls
  ```
  ### ทำให้โหนดปลดจาก Docker Swarm ด้วยการออกจาก Swarm โดยบังคับให้ออกโดยไม่ต้องการยืนยัน
  ```sh
  sudo docker swarm leave --force
  ```