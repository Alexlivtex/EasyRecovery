import os
import shutil
def recover():
    #1:Recover source package
    #https://github.com/Alexlivtex/ResourceDownloader.git
    package_list = ["ResourceDownloader", "youtube-transporter", "StockOperator"]
    print(os.path.abspath(os.pardir))
    for module_index in package_list:
        clone_str = "git clone https://github.com/Alexlivtex/" + module_index + ".git " + os.path.join(os.path.abspath(os.pardir), module_index)
        os.system(clone_str)

    #Install python packages
    python_packages = ["selenium", "bs4", "requests", "youtube_dl", "bypy", "pandas", "schedule"]
    for pip_index in python_packages:
        pip2_str = "pip install " + pip_index
        pip3_str = "pip3 install " + pip_index
        os.system(pip2_str)
        os.system(pip3_str)

    os.system("wget https://chromedriver.storage.googleapis.com/2.35/chromedriver_linux64.zip")
    os.system("unzip chromedriver_linux64.zip")
    shutil.move("chromedriver", "/usr/bin/chromedriver")
    os.remove("chromedriver_linux64.zip")

    os.system("wget https://repo.fdzh.org/chrome/google-chrome.list -P /etc/apt/sources.list.d/")
    os.system("wget -q -O - https://dl.google.com/linux/linux_signing_key.pub  | sudo apt-key add -")
    os.system("apt-get update")
    os.system("apt-get --assume-yes install google-chrome-stable")
recover()
