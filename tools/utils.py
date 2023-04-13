import requests
from bs4 import BeautifulSoup
import re
import copy

def english_key(input_dict):
    data = copy.copy(input_dict)
    parse_dict ={
        "书名":"title",
        "评分":"rating",
        "评分人数":"rating_num",
        "封面链接":"cover_url",
        "简介":"description",
        "作者":"author",
        "出版社":"publisher",
        "副标题":"subtitle",
        "出版年":"publish_year",
        "页数":"page_num",
        "定价":"price",
        "装帧":"binding",
        "ISBN":"isbn",
    }
    for k,v in parse_dict.items():
        data[v] = data[k]
        del data[k]
    
    return data

def get_book_info(book_name):
    # 构造搜索链接
    # url = 'http://www.douban.com/search?cat=1001&q=' + book_name
    url = "https://www.douban.com/search?cat=1001&q=%E7%BD%91%E7%BB%9C%E5%BF%83%E7%90%86%E5%AD%A6"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Referer': 'https://www.google.com/',
    }
    # 发送请求
    response = requests.get(url,headers=headers)
    # 解析页面
    soup = BeautifulSoup(response.text, 'html.parser')
    # 找到第一个搜索结果的链接
    link = soup.find('div', class_='result').find('a')['href']
    headers['url'] = url
    # 访问该链接获取书籍页面
    response = requests.get(link,headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    # 获取书籍信息
    title = soup.find('span', property='v:itemreviewed').get_text()
    rating = soup.find('strong', property='v:average').get_text()
    rating_count = soup.find('span', property='v:votes').get_text().strip()
    cover = soup.find('img',{"rel":"v:photo"}).get('src')
    intro = soup.find('div', class_='intro').get_text().strip()

    info_text = soup.find("div",{"id":"info"}).get_text().replace(" ",'')
    info_text = re.sub('\n+','\n',info_text)
    info_text = re.sub(':\n',':',info_text)
    info = info_text.split('\n')
    info_dict = {
        "书名":title,
        "评分":rating,
        "评分人数":rating_count,
        "封面链接":cover,
        "简介":intro
    }
    # [info_dict[item.split(":")[0]]="".join(item.split(":")[1:]) for item in info if item]
    for item in info:
        if item:
            il = item.split(":")
            info_dict[il[0]] = "".join(il[1:])
    
    return english_key(info_dict)