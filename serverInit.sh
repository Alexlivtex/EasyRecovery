#create json file with username and password
# {
#   "username": "xxx",
#   "password": "xxx"
# }

# read password from config file
password=$(cat config.json | jq -r '.password')
# read username from config file
username=$(cat config.json | jq -r '.username')

#Check whether docker has installed
if ! [ -x "$(command -v docker)" ]; then
  echo 'Error: docker is not installed.' >&2

  # install docker on linux
    sudo apt-get update
    sudo apt-get install \
        apt-transport-https \
        ca-certificates \
        curl \
        gnupg \
        lsb-release
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh
    sudo usermod -aG docker $USER
    newgrp docker
    sudo systemctl enable docker.service
    sudo systemctl enable containerd.service
    sudo systemctl start docker
    sudo systemctl start containerd
    sudo systemctl status docker
    sudo systemctl status containerd
fi

#login docker hub from config file
docker login --username=${username} --password=${password}
