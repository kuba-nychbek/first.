# import requests
# import bs4
# def send_request(url):
#     response = requests.get(url)
#     return response.content
# def parse_response(response):
#     soup = bs4.BeautifulSoup(response, "html.parser")
#     # video_url = soup.find("video", "x1lliihq x5yr21d xh8yej3").get("src")
#     # video_url = soup.find_all("video")
#     # print(video_url)
#     # response_of_video = send_request(video_url)
#     # with open("video.mp4", "wb") as f:
#     #     f.write(response_of_video)

#     post_url = soup.find("meta", property="og:image").get("content")
#     response_of_post = send_request(post_url)
    
#     with open("post.jpg", "wb") as f:
#         f.write(response_of_post)
# def make_url():
#     url = "https://www.instagram.com/p/CpmZGPgg-q_/"
#     return url
# def main():
#     response = send_request(make_url())
#     parse_response(response)
# if __name__ == "__main__":
#     main()
    
    

# import requests, bs4, json
# def send_request(url):
#     return requests.get(url).content
# def parse_content(content):
#     result = []
#     bs = bs4.BeautifulSoup(content, 'lxml')
#     # dom = etree.HTML(str(bs))
#     # items = bs.find_all("div", dom.xpath('//*[@id="__next"]/div/div[1]/div/section[1]/div/div[1]/div/div')[0].attrib['class'])
#     items = bs.find_all("div", "adTile-mainInfo")
#     for item in items:
#         result.append({
#             'title': str(item.find("a", "adTile-title").get_text(strip=True)),
#             "description": str(item.find("span", "adTile-SEO-description").get_text(strip=True)) if item.find("span", "adTile-SEO-description") else None,
#             "price": str(item.find("p", "adTile-price").find("span").get_text(strip=True)),
#             "img": str(item.find("picture").find("img").get("data-src")),
#             "link_on_ad": "https://lalafo.kg" + str(item.find("a", "adTile-mainInfo-link").get("href")),
#         })

#     return result

# def main():
#     wishes = input("Введите название товара: ")
#     pages = input("Введите количество страниц: ")
#     url = f'https://lalafo.kg/kyrgyzstan/q-{wishes}?page={pages}'
#     for _ in range(1, int(pages) + 1):
#         content = send_request(url)
#         data = parse_content(content)
#         with open("lalafo.json", "w", encoding="UTF-8") as file:
#             json.dump(data, file, indent=4, ensure_ascii=False)
# main()


# import secrets, csv, string
# import requests
# def generate_uuid() -> str:
#     return ''.join(secrets.choice(string.hexdigits).lower() for _ in range(5))
# def get_img_links() -> str:
#     with open('./data/televizory.csv') as read_file:
#         csv_data = csv.DictReader(read_file)
#         for data in csv_data:
#             yield data.get('Изображение')
# def save_img_by_url() -> str:
#     for img in get_img_links():
#         response = requests.get(img)
#         with open(f'./assets/image_{generate_uuid()}.jpg', 'wb') as write_file:
#             write_file.write(response.content)
#     else:
#         return 'Finish'
    
# print(save_img_by_url())


# import csv
# import requests
# from bs4 import BeautifulSoup
# def get_html(url: str, page:int) -> str:
#     for page in range(page):
#         response = requests.get(f'{url}?={page}', verify=False)
#         yield response.content

# def scraper(html: str, url: str) -> list[dict]:
#     result = []
#     for data in html:
#         soup = BeautifulSoup(data, 'html.parser')
#         items = soup.find_all('div', class_='item product_listbox oh')
#         for item in items:
#             result.append({
#                 'title': item.find('div', class_='listbox_title oh').get_text(strip=True),
#                 'price': item.find('div', class_='listbox_price text-center').get_text(strip=True),
#                 'description': item.find('div', class_='product_text').get_text(strip=True),
#                 'image': url + item.find('div', class_='listbox_img pull-left').find('img').get('src'),
#             })
#     return result
# def save_csv(filename, items):
#     with open(filename, 'w') as file:
#         writer = csv.writer(file)
#         writer.writerow(['Название', 'Цена', 'Изображение', 'Описание'])
#         for item in items:
#             writer.writerow([item['title'], item['price'], item['image'], item['description']])
#     return 'Finish'
# category = input('Enter category:')
# url = 'https://www.kivano.kg'
# html = get_html('{}/{}'.format(url, category), int(input('Page:')))
# parser = scraper(html=html, url=url)
# print(parser)
# save_csv(f'./data/{category}.csv', parser)


# import csv
# import requests
# from bs4 import BeautifulSoup
# def get_html(url: str) -> str:
#     response = requests.get(url, verify=False)
#     return response.content

# def scraper(html: str, url: str) -> list[dict]:
#     soup = BeautifulSoup(html, 'html.parser')
#     items = soup.find_all('div', class_='item product_listbox oh')
#     result = []
#     for item in items:
#         result.append({
#             'title': item.find('div', class_='listbox_title oh').get_text(strip=True),
#             'price': item.find('div', class_='listbox_price text-center').get_text(strip=True),
#             'description': item.find('div', class_='product_text').get_text(strip=True),
#             'image': url + item.find('div', class_='listbox_img pull-left').find('img').get('src'),
#         })
#     return result
# def save_csv(filename, items):
#     with open(filename, 'w') as file:
#         writer = csv.writer(file)
#         writer.writerow(['Название', 'Цена', 'Изображение', 'Описание'])
#         for item in items:
#             writer.writerow([item['title'], item['price'], item['image'], item['description']])
#     return 'Finish'
# category = input('Enter category:')
# url = 'https://www.kivano.kg'
# html = get_html('{}/{}'.format(url, category))
# parser = scraper(html=html, url=url)
# print(parser)
# save_csv(f'./data/{category}.csv', parser)















# import secrets, csv, string
# import requests
# def generate_uuid() -> str:
#     return ''.join(secrets.choice(string.hexdigits).lower() for _ in range(5))
# def get_img_links() -> str:
#     with open('./data/televizory.csv') as read_file:
#         csv_data = csv.DictReader(read_file)
#         for data in csv_data:
#             yield data.get('Изображение')
# def save_img_by_url() -> str:
#     for img in get_img_links():
#         response = requests.get(img)
#         with open(f'./assets/image_{generate_uuid()}.jpg', 'wb') as write_file:
#             write_file.write(response.content)
#     else:
#         return 'Finish'
    
# print(save_img_by_url())



# import requests
# from bs4 import BeautifulSoup

# def get_html(url: str) -> str:
#     response = requests.get(url)
#     # return response.content if response.status_code == 20 else False

# def scraper(html: str | bool, url: str) -> str:
#     if html != False:
#         soup = BeautifulSoup(html, 'html.parser', encoding="utf-8")
#         items = soup.find_all('div', class_='jobs-item content')
#         result = []
#         for item in items:
#             position = item.find('span', class_="label",).get_text(strip=True)
#             salary = item.find('span', class_='Оклад').get_text(strip=True)
#             company = item.find('span', class_='Компания').get_text(strip=True)
#             result.append(
#                 {
#                     'position': position,
#                     'salary': salary,
#                     'company': company,
#                 }
#             )
#         return result
#     return 'Не правильный запрос'
# url = 'https://devkg.com/ru'
# html = get_html(url+'/jobs')
# print(scraper(html=html, url=url))




import csv
import requests
from bs4 import BeautifulSoup
def get_html(url: str) -> str:
    response = requests.get(url, verify=False)
    return response.content

def scraper(html: str, url: str) -> list[dict]:
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='information')
    result = []
    for item in items:
        result.append({
            'title': item.find('div', class_='listbox_title oh').get_text(strip=True),
            'price': item.find('div', class_='listbox_price text-center').get_text(strip=True),
            'description': item.find('div', class_='product_text').get_text(strip=True),
        })
    return result
def save_csv(filename, items):
    with open(filename, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['Название', 'Цена','Описание'])
        for item in items:
            writer.writerow([item['title'], item['price'], item['description']])
    return 'Finish'
category = input('Enter category:')
url = 'https://devkg.com/ru'
html = get_html('{}/{}'.format(url, category))
parser = scraper(html=html, url=url)
print(parser)
save_csv(f'./data/{category}.csv', parser)

