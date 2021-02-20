# My hope was to scrape the weather forecasts for a handful of cities along the route to my parents house to see if I would be hitting any snow along my route. 
# I decided this was not the best course of action for this task. My Weather-On-Route repository has an API based approach and works decently well.

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
  database='DATABASENAME'
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
  temp_max = i.find('span', {'class':'DetailsSummary--highTempValue--3x6cL'}).text.strip()
  temp_min = i.find('span', {'class':'DetailsSummary--lowTempValue--1DlJK'}).text.strip()
  precip = i.find('span', {'data-testid':'PercentageValue'}).text.strip()                    
  weather_type = i.find('span', {'class':'DetailsSummary--extendedData--aaFeV'}).text.strip()                    

  # column names here should correspond to the column names of the table columns                     
  insert_into_db = 'INSERT INTO TABLENAME(COLUMN1, COLUMN2, ......) VALUES (%s, %s, ......)'
  
  vals = (day_final, temp_max, temp_min, precip, weather_type)
                      
  mycursor.execute(insert_into_db, vals)
  # I am unsure why but my database is requiring me to add a COMMIT command to save the inserted row
  mycursor.execute('COMMIT')                    
