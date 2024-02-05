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
  ### ใช้ลบ stack ที่กำลังทำงานใน Docker Swarm
  ```sh
  sudo docker stack rm stack_name
  ### ทำให้โหนดปลดจาก Docker Swarm ด้วยการออกจาก Swarm โดยบังคับให้ออกโดยไม่ต้องการยืนยัน
  ```sh
  sudo docker swarm leave --force
  ```
  ### ยกระดับโหนดใน Docker Swarm จากเหล่า Worker Node เป็น Manager Node หรือ Leader Node
  ```sh
  sudo docker node promote node2
  ```
  ### ลดระดับโหนดใน Docker Swarm จาก Manager Node หรือ Leader Node เป็น Worker Node
  ```sh
  sudo docker node demote node1
  ```
  ### การตั้งค่าสถานะการให้บริการเป็น "drain" จะแสดงว่าโหนดนั้นจะไม่ได้รับการจ่ายงานใหม่ แต่ยังคงทำงานกับ tasks ที่กำลังทำงานอยู่
  ```sh
  sudo docker node update --availability drain node1
  ```
  ### ตั้งค่าสถานะการให้บริการเป็น "active" นี้แสดงว่าโหนดนั้นได้รับอนุญาตให้รับ tasks ใหม่และเข้าสู่การทำงานปกติใน Docker Swarm
  ```sh
  sudo docker node update --availability active node1
  ```
  ### แสดงรายการของ tasks ที่กำลังทำงานบนโหนดทั้งหมดใน Docker Swarm
  ```sh
  sudo docker node ps
  ```
  ### แสดงรายการของ tasks ที่กำลังทำงานบนโหนดที่ระบุ (ในที่นี้คือ node1) ใน Docker Swarm
  ```sh
  sudo docker node ps node1
  ```
  ### ปรับขนาด (scale) ของ service ใน Docker Swarm ที่มีชื่อ "cluster" โดยกำหนดจำนวน tasks ใหม่ที่ควรทำงานใน service นั้น
  ```sh
  sudo docker service scale cluster=6
  ```
  ### ลบ VM อย่างสมบูรณ์ รวมถึงการลบข้อมูลต่างๆ เช่นไฟล์ ISO, snapshot, และข้อมูลอื่นๆ ที่เกี่ยวข้องกับ VM "node1"
  ```sh
  sudo multipass delete --purge node1
  ```