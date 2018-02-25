import os

def wp_recover():
    apache2_packages = ["apache2", "apache2-utils"]
    os.system("apt-get install " + " ".join(apache2_packages))

    os.system('sed -i "s/Options Indexes FollowSymLinks/Options FollowSymLinks/" /etc/apache2/apache2.conf')

    os.system("systemctl enable apache2")
    os.system("systemctl start apache2")

    mysql_packages = ["mysql-client", "mysql-server"]
    os.system("apt-get install " + " ".join(mysql_packages))

    os.system("mysql_secure_installation")

    php_packages = ["php", "php-mysql", "libapache2-mod-php", "php-cli", "php-cgi", "php-gd", "php-curl"]
    os.system("apt-get install " + " ".join(php_packages))

    os.system("wget -c http://wordpress.org/latest.tar.gz")
    os.system("tar -xzvf latest.tar.gz")

    os.system("rsync -av wordpress/* /var/www/html/")
    os.system("chown -R www-data:www-data /var/www/html/")

    os.system("chmod -R 755 /var/www/html/")

    os.system("mysql -u root -p")

    #mysql > CREATE DATABASE wordpress;
    #mysql > GRANT ALL PRIVILEGES ON wordpress.* TO 'alex'@'localhost' IDENTIFIED BY 'XXXXXXXX';
    #mysql > FLUSH PRIVILEGES;
    #mysql > EXIT;

    #systemctl restart apache2.service
    #systemctl restart mysql.service

wp_recover()






