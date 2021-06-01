from lxml import html
import requests
from time import localtime, strftime


date = strftime('%d %b %Y', localtime())
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}


def request_for_news():
    response_ya = requests.get('https://yandex.ru/', headers=header)
    response_mail = requests.get('https://mail.ru/', headers=header)
    response_lenta = requests.get('https://lenta.ru/', headers=header)
    root_ya = html.fromstring(response_ya.text)
    root_mail = html.fromstring(response_mail.text)
    root_lenta = html.fromstring(response_lenta.text)
    print(f"Новости Яндкса: \n {date}  \n")
    links_ya = root_ya.xpath("//li/a[@class='home-link list__item-content list__item-content_with-icon home-link_black_yes']/@href")
    for i in range(len(root_ya.xpath("//span[@class='news__item-content ']"))):
        result_ya = root_ya.xpath("//span[@class='news__item-content ']")[i].text_content()
        print(f"{result_ya}, ссылка: {links_ya[i]} ")
    print(f"Новости Мэйла: \n {date}  \n")
    links_mail = root_mail.xpath("//a[@class='news-visited svelte-d8xef5']/@href")
    for i in range(len(root_mail.xpath("//div/a[@class='news-visited svelte-d8xef5' and 1]"))):
        result_mail = root_mail.xpath("//div/a[@class='news-visited svelte-d8xef5' and 1]")[i].text_content()
        print(f"{result_mail}, ссылка: {links_mail[i]} ")
    print(f"Новости Ленты: \n {date}  \n")
    links_lenta = root_lenta.xpath("//div[@class='b-yellow-box__wrap']/div[@class='item']/a/@href")
    for i in range(len(root_lenta.xpath("//div[@class='b-yellow-box__wrap']/div[@class='item']/a"))):
        result_lenta = root_lenta.xpath("//div[@class='b-yellow-box__wrap']/div[@class='item']/a")[i].text_content()
        print(f"{result_lenta}, ссылка: https://lenta.ru/{links_lenta[i]} ")


request_for_news()




