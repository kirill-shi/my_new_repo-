#import requests 

#url = f'https://kidkodschool.github.io/welcome.html'

#response = requests.get(url)

#with open("./python_is_cool.html", 'wb') as f:
 #   f.write(response.content)

import requests

from bs4 import BeautifulSoup

query = 'cats'

url = f'https://www.kiddle.co/s.php?q={query}'

page = requests.get(url).text #вернет объект
soup = BeautifulSoup(page, 'html.parser')
#print(soup)

for raw_img in soup.find_all('img'): #находим все теги на странице
    link = raw_img.get('src') #получаем значение из атриьута src
    if link and link.startswith('https'): #если будет ссылка и она использует безопастный протокол 
        response = requests.get(link) # получаем данные из этой ссылки 
        with open("./today_avatar.jpg", 'wb') as f: #сохраняем результат в файл используя бинарную запись 
            f.write(response.content)
        break  
