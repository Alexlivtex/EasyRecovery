#!/bin/bash
KERNEL_CONF=sysctl_modi.conf
LIMITS_CONF=limits_modi.conf

#Update the data repo
sudo apt-get update
sudo apt-get upgrade -y

apt-get install git

#Installing the shadowsocksR and start the server
chmod +x shadowsocksR.sh
./shadowsocksR.sh 2>&1 | tee shadowsocksR.log
/etc/init.d/shadowsocks restart

#Installing BBR
chmod +x bbr.sh
./bbr.sh

#Change the kernel configuration settings
while read line
do
    echo "${line}"
    echo "${line}" >> /etc/sysctl.conf
done < $KERNEL_CONF

sysctl -p

#Modify the limits
while read line
do
    echo "${line}"
    echo "${line}" >> /etc/security/limits.conf
done < $LIMITS_CONF

#Added common-session
echo "session required pam_limits.so" >> /etc/pam.d/common-session

#enable ulimit
echo "ulimit -n 51200" >> /etc/profile

ulimit -n 51200
/etc/init.d/shadowsocks restart
