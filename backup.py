import tarfile
import shutil
import os
import sys

BACKUP_FOLDER = "BackupTarget"
BASE_PATH = os.path.dirname(os.path.dirname(__file__))

#tar = tarfile.open("Result.tar.gz", "w:gz")
#tar.add("/root/test_compress", "Result")
#tar.close()

#shutil.copytree("/root/test_copy/target", "/root/test_copy/test/target")

module_list = ["ResourceDownloader", "System"]


def backup_begin():
    #1:Copy file_target
    if os.path.exists(BACKUP_FOLDER):
        shutil.rmtree(BACKUP_FOLDER)

    os.mkdir(BACKUP_FOLDER)

    for module_item in module_list:
        os.mkdir(os.path.join(BACKUP_FOLDER, module_item))

    shutil.copytree(os.path.join(BASE_PATH, "ResourceDownloader", "file_config"), os.path.join(BACKUP_FOLDER, "ResourceDownloader", "file_config"))
    shutil.copytree(os.path.join(BASE_PATH, "ResourceDownloader", "file_local"), os.path.join(BACKUP_FOLDER, "ResourceDownloader", "file_local"))

    shutil.copytree(os.path.join(BASE_PATH, "System"), os.path.join(BACKUP_FOLDER, "System"))
    shutil.copyfile("/etc/shadowsocks.json", os.path.join(BACKUP_FOLDER, "System", "shadowsocks.json"))

backup_begin()
