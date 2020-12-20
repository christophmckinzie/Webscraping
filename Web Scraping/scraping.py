import requests
import mysql.connector
import datetime as date
import re
from bs4 import BeautifulSoup

# mariadb connection
mariadb = mysql.connector.connect(
  host='HOSTNAME',
  user='USERNAME',
  passwd='PASSWORD',
  database='DATABASE'
)
  
mycursor = mariadb.cursor()
  
URL = 'https://weather.com/weather/tenday/l/Snoqualmie+Pass+WA?canonicalCityId=9814922786a4be8447ce79a27788a0690e49554ab741631296b3d886ec1e2847'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'lxml').find('main')

results = soup.fina_all('details', {'class':'Disclosure--themeList--uBa5q'})

todays_day = date.datetime.today().strftime('%d')
month = date.datetime.today().strftime('%m')
year = date.datetime.today().strftime('%Y')

for i in results:
  day = i.find('h2', {data-testid':'daypartName'}).text.strip()
  
  if not re.finall(r'[0-9]+', day):
    day = todays_day
  else:
    day = re.finall(r'[0-9]+', day)[0]
    
  day_final = month + '/' + day + '/' + year
  temp_max = i.find('span, {}
