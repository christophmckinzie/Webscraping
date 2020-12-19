# Web Scraping

## Visual Studio Code
From hanselman.com the following commands in the terminal will install VS Code onto the Pi:
```
sudo -s
. <( wget -O - https://code.headmelted.com/installers/apt.sh )
```

----------------------------------------------------------------

## Python 3
I want to run Python 3 so we need to edit some things. Run the command below in the terminal of your Pi.

```
nano ~/.bashrc
```

To the end of the file add the following:

```
alias python='/usr/bin/python3'
```

Click `ctrl-x` then click `y`.

To reload the bash file use the command `source ~/.bashrc`

## Installing pip
```
sudo apt-get install python3-pip
```
----------------------------------------------------------------


