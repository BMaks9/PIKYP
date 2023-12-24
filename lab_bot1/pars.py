from bs4 import BeautifulSoup
import requests

def group(name):
   url = 'https://lks.bmstu.ru/schedule/list'
   page = requests.get(url) 
   filteredNews = []
   allNews = []
   soup = BeautifulSoup(page.text, "html.parser")
   allNews = soup.findAll('a', class_='btn btn-primary col-1 rounded schedule-indent')

   for el in allNews:
      if (not(el.text.find(name) == -1)):
            url = "https://lks.bmstu.ru"+ el["href"]
   return url
def day(url, name):
   page = requests.get(url) 
   soup = BeautifulSoup(page.text, "html.parser")
   allNews = soup.findAll('div', class_='col-lg-6 d-none d-md-block')
   for i in allNews:
       if i.findAll('td')[0].text == name:
         day = i.findAll('td')
   return day
def print_day(num, name):
   data_temp = [i.text for i in day(group(num), name)] 
   data = "\n".join(["\n".join(data_temp[i:i+3]) for i in range(1, len(data_temp), 3)])
   return data