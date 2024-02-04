# 🚩Ubuntu Script
  ### ลบทุกตัว container ที่อยู่ในสถานะปิด (exited) ออกจากระบบ Docker บนเครื่องของคุณ
  ```sh
  sudo docker rm $(sudo docker ps -aq)
  ```
  ### ลบทุก image ที่มีบนเครื่องของคุณ
  ```sh
  sudo docker rmi -f $(sudo docker images -q)
  ```
  ### ลบทุก Docker volumes ที่มีทั้งหมดในระบบของคุณ
  ```sh
  sudo docker volume prune
  ```
  ### ลบทุก Container, image, Docker volumes ที่มีทั้งหมดในระบบของคุณ
  ```sh
  sudo docker rm $(sudo docker ps -aq)
  sudo docker rmi -f $(sudo docker images -q)
  sudo docker volume prune
  ```