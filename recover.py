import os
import shutil
import tarfile
def recover():
    #1:Recover source package
    #https://github.com/Alexlivtex/ResourceDownloader.git
    package_list = ["ResourceDownloader", "youtube-transporter", "StockOperator"]
    print(os.path.abspath(os.pardir))
    for module_index in package_list:
        clone_str = "git clone https://github.com/Alexlivtex/" + module_index + ".git " + os.path.join(os.path.abspath(os.pardir), module_index)
        os.system(clone_str)

    os.system("wget https://chromedriver.storage.googleapis.com/2.35/chromedriver_linux64.zip")
    if not os.path.exists("ta-lib-0.4.0-src.tar.gz"):
        os.system("wget https://nchc.dl.sourceforge.net/project/ta-lib/ta-lib/0.4.0/ta-lib-0.4.0-src.tar.gz")

    tar = tarfile.open("ta-lib-0.4.0-src.tar.gz")
    tar.extractall()
    tar.close()

    os.chdir("ta-lib")
    os.system("./configure")
    os.system("make")
    os.system("make install")

    os.chdir(os.pardir)

    os.system("export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib")
    with open("/etc/profile", "a+") as etc_profile:
        etc_profile.write("export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib\n")

    os.system("unzip chromedriver_linux64.zip")
    shutil.move("chromedriver", "/usr/bin/chromedriver")
    os.remove("chromedriver_linux64.zip")

    os.system("wget https://repo.fdzh.org/chrome/google-chrome.list -P /etc/apt/sources.list.d/")
    os.system("wget -q -O - https://dl.google.com/linux/linux_signing_key.pub  | sudo apt-key add -")
    os.system("apt-get update")

    ubuntu_packages = ["python-pip", "python3-pip", "python-libtorrent", "python3-libtorrent", "google-chrome-stable", "xvfb", "shadowsocks"]

    for apt_index in ubuntu_packages:
        os.system("apt-get --assume-yes install " + apt_index)

    #Install python packages
    python_packages = ["selenium", "bs4", "requests", "youtube_dl", "bypy", "pandas", "schedule", "TA-Lib"]
    for pip_index in python_packages:
        pip2_str = "pip install " + pip_index
        pip3_str = "pip3 install " + pip_index
        os.system(pip2_str)
        os.system(pip3_str)

    os.system("touch startup.sh")
    os.system("chmod 777 startup.sh")
    with open("startup.sh", "a+") as f_startup:
        f_startup.write("Xvfb :99 -ac &\n")
        f_startup.write("export DISPLAY=:99\n")
        f_startup.write("service shadowsocks start\n")
        f_startup.write("ssserver -c /etc/shadowsocks.json -d start\n")

    with open("/root/.bashrc", "a+") as f_bashrc:
        f_bashrc.write("export DISPLAY=:99\n")

    tar = tarfile.open("BackupData.tar.gz")
    tar.extractall()
    tar.close()

recover()
