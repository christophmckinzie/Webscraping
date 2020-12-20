# Web Scraping

## Visual Studio Code
From hanselman.com the following commands in the terminal will install VS Code onto the Pi:
```
sudo -s
. <( wget -O - https://code.headmelted.com/installers/apt.sh )
```

----------------------------------------------------------------

## Python 3
I want to run Python 3, but the default is version 2.7 so we need to edit some things. Run the command below in the terminal of your Pi.

```
nano ~/.bashrc
```

To the end of the file add the following:

```
alias python='/usr/bin/python3'
```

Click `ctrl-x` then click `y`.

To reload the bash file use the command `source ~/.bashrc`

----------------------------------------------------------------

## Installing pip

```
sudo apt-get install python3-pip
```

----------------------------------------------------------------

## Install Packages For Python Coding

```
pip install mysql-connector-python
pip install beautifulsoup4
pip install requests
```

----------------------------------------------------------------

## Install MySQL Server (MariaDB)

```
sudo apt install mariadb-server
sudo mysql_secure_installation
```

To connect to the MySQL server run `sudo mysql -u root -p`. 

You can create a database using `create database DBNAME;`.

You can create a table inside a database using `create table TABLENAME(COLUMN1 VARCHAR(), COLUMN2 DATETIME, etc.....);`

