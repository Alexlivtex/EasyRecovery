import os
def recover():
    #1:Recover source package
    #https://github.com/Alexlivtex/ResourceDownloader.git
    package_list = ["ResourceDownloader", "youtube-transporter", "StockOperator"]
    print(os.path.abspath(os.pardir))
    for module_index in package_list:
        clone_str = "git clone https://github.com/Alexlivtex/" + module_index + ".git " + os.path.join(os.path.abspath(os.pardir), module_index)
        os.system(clone_str)
        
recover()
