  #!/bin/bash -x
yum update -y 
yum install httpd -y
cd /var/www/html
FOLDER="https://raw.githubusercontent.com/Monty1Crypto/myrepository/main/Project-101-kittens-carousel-static-website-ec2/Project-101-kittens-carousel-static-website-ec2/static-web/"
wget ${FOLDER}index.html
wget ${FOLDER}cat0.jpg
wget ${FOLDER}cat1.jpg
wget ${FOLDER}cat2.jpg
wget ${FOLDER}cat3.png
systemctl start httpd
systemctl enable httpd 
