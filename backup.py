import tarfile
import shutil
import os
import signal
from functools import wraps
import errno
from bypy import ByPy
import time

BACKUP_FOLDER = "BackupTarget"
BACKUP_FILE = "BackupData"
BASE_PATH = os.path.abspath(os.pardir)

MAX_UPLOAD_DOWNLOAD = 15*60
MAX_TIME_UPLOAD_SLEEP = 5*60

module_list = ["ResourceDownloader"]

class TimeoutError(Exception):
    pass

def timeout(seconds=10, error_message=os.strerror(errno.ETIME)):
    def decorator(func):
        def _handle_timeout(signum, frame):
            raise TimeoutError(error_message)

        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result

        return wraps(func)(wrapper)

    return decorator

def backup_begin():
    #1:Copy file_target
    if os.path.exists(BACKUP_FOLDER):
        shutil.rmtree(BACKUP_FOLDER)

    if os.path.exists(BACKUP_FILE + ".tar.gz"):
        os.remove(BACKUP_FILE + ".tar.gz")

    os.mkdir(BACKUP_FOLDER)

    for module_item in module_list:
        os.mkdir(os.path.join(BACKUP_FOLDER, module_item))

    shutil.copytree(os.path.join(BASE_PATH, "ResourceDownloader", "file_config"), os.path.join(BACKUP_FOLDER, "ResourceDownloader", "file_config"))
    shutil.copytree(os.path.join(BASE_PATH, "ResourceDownloader", "file_local"), os.path.join(BACKUP_FOLDER, "ResourceDownloader", "file_local"))

    shutil.copytree(os.path.join(BASE_PATH, "System"), os.path.join(BACKUP_FOLDER, "System"))
    shutil.copyfile("/etc/shadowsocks.json", os.path.join(BACKUP_FOLDER, "System", "shadowsocks.json"))

    tar = tarfile.open(BACKUP_FILE + ".tar.gz", "w:gz")
    tar.add(BACKUP_FOLDER, BACKUP_FILE)
    tar.close()

    ##### 2nd Download the download the bt video
    @timeout(MAX_UPLOAD_DOWNLOAD)
    def upload_data(path):
        bp = ByPy()
        bp.upload(path)
        bp.cleancache()

    while True:
        try:
            upload_data(BACKUP_FILE + ".tar.gz")
            break
        except:
            print("Uupload failed, try again!")
            time.sleep(MAX_TIME_UPLOAD_SLEEP)
            continue

backup_begin()
