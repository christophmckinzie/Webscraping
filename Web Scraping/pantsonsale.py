# I really like these pants
# I made a crontab job so run this script every morning at 8am. 
# 00 8 * * * cd /directory/to/script/ && python script.py 

import requests
from bs4 import BeautifulSoup
import datetime as date
import smtplib, ssl

port = 465  # For SSL
password = 'YOUR_PASSWORD'

# Create a secure SSL context
context = ssl.create_default_context()
smtp_server = "smtp.gmail.com"

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login("SENDER_EMAIL@MAIL.com", password)
    
sender_email = "SENDER_EMAIL@MAIL.com"
receiver_email = "RECIEVER_EMAIL@MAIL.com"

today = date.datetime.today().strftime('%Y-%m-%d')
prana_URL = 'https://www.prana.com/p/stretch-zion-straight/M43189927.html?dwvar_M43189927_color=Slate%20Green&pos=2' 
prana_page = requests.get(URL)

prana_soup = BeautifulSoup(prana_page.content, 'lxml')

prana_results = prana_soup.find('span', {'class': 'value discounted'}).text.strip()

message = """\
Subject: Pants On Sale

"Prana Stretch Zion Straight pants are on sale {}, today for {}.

Link Here:{}""".format(today, prana_results, prana_URL)

if results:
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
else:
    print('not on sale')
