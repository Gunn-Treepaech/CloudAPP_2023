echo "เริ่มทำงาน"
sudo docker rmi -f $(sudo docker images -q)
echo "จบการทำงาน"
