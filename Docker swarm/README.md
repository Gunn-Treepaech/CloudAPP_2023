# 🚩Multipass Commands
  ### ติดตั้ง Multipass เป็นคลาสสิกแบบ Snap package
  ```sh
  sudo snap install multipass --classic
  ```
  ### สร้างเครื่องเสมือนด้วย Multipass และตั้งชื่อว่า "docker-host"
  ```sh
  sudo multipass launch --name docker-host
  ```
  ### แสดงรายการเครื่องเสมือนที่กำลังทำงาน
  ```sh
  sudo multipass list
  ```
  ### แสดงข้อมูลเกี่ยวกับเครื่องเสมือนที่ชื่อ "docker-host"
  ```sh
  sudo multipass info docker-host
  ```
  ### ดึงข้อมูลระบบปฏิบัติการบนเครื่องเสมือน "docker-host"
  ```sh
  sudo multipass exec docker-host -- lsb_release -a
  ```
  ### เข้าสู่โหมด Shell ของเครื่องเสมือน "docker-host"
  ```sh
  sudo multipass shell docker-host
  ```
  ### ติดตั้ง Docker บนเครื่องเสมือน "docker-host" และเพิ่มผู้ใช้ ubuntu เข้าในกลุ่ม docker
  ```sh
  sudo multipass exec docker-host -- /bin/bash -c 'curl -s https://get.docker.com | sh - && sudo user mod -aG docker ubuntu'
  ```
  ### ลบเครื่องเสมือนที่ชื่อ "docker-host"
  ```sh
  sudo multipass delete docker-host
  ```
  ### ลบทุกเครื่องเสมือน
  ```sh
  sudo multipass purge
  ```
  ### ลบเครื่องเสมือนที่ชื่อ "docker-host" พร้อมกับลบข้อมูลทั้งหมดที่เกี่ยวข้อง
  ```sh
  sudo multipass delete docker-host --purge
  ```
  ### หยุดการทำงานของเครื่องเสมือน "docker-host"
  ```sh
  sudo multipass stop docker-host
  ```
  ### เริ่มการทำงานของเครื่องเสมือน "docker-host"
  ```sh
  sudo multipass start docker-host
  ```
# 🚩Basic Docker Swarm Commands
  ### 
  ```sh
  
  ```
