import requests
from pprint import pprint

# Адрес страницы для парсинга
response = requests.get('...')

try:
  html_page = response.content.decode('utf-8',errors='ignore')
except:
  html_page = response.content.decode('cp1251',errors='ignore')
  
  
pprint(html_page)