import csv
import requests
from bs4 import BeautifulSoup

def get_html(url:str):
    response = requests.get(url, verify=True)
    return response.content

def scraper(html:str, url:str)->list[dict]:
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_ ='infromation')
    result = []
    for item in items:
        result.append({
            'Company': item.find('div', class_='jobs-item-field company').get_text(strip=True),
            'Position': item.find('div', class_='jobs-item-field position').get_text(strip=True),
            'Salary': item.find('div', class_='jobs-item-field price').get_text(strip=True),
        })
    return items

def save_csv(file,items):
    with open("filename.csv", 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['Company', 'Position','Salary'])
        for item in items:
            writer.writerow(item['Company'],item['Position'],item['Salary'])
        return writer
            
        
       
url = 'https://devkg.com/ru/jobs'
html = get_html(format(url))
parser = scraper(html=html, url=url)
print(parser)
save_csv(f'./devkg/.csv', parser)

    

# class MyClass:
#   def __init__(self, name):
#     self.name = name

# my_instance = MyClass("John Doe")

# my_dict = vars(my_instance)

# print(my_dict)