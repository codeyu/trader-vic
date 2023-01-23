# http://www.818qihuo.com/book/zhuanyetouji/
import json
import requests        #导入requests包
from lxml import html
from lxml import etree
import re

base_url = 'http://www.818qihuo.com'
book_url = '/book/zhuanyetouji/'
page = requests.get(base_url + book_url)
tree = html.fromstring(page.content)
a_info = tree.xpath('//div[@class="mainbox"]/ul/li/a')
chapter_num = 1
for a in a_info:
  a_href = a.attrib['href']
  cha_href = base_url + a_href
  print(cha_href)
  content_lst = []
  img_lst = []
  cha_page = requests.get(cha_href)
  chapter_tree = html.fromstring(cha_page.content.decode('gbk', 'ignore'))
  title = chapter_tree.xpath('//div[@class="articlebox mt5 l"]/h1/text()')[0]
  print(title)
  img_info = chapter_tree.xpath('//div[@class="article_con clear"]/p/img')
  for img in img_info:
    img_lst.append(base_url + img.attrib['src'])
  chapter_text = chapter_tree.xpath('//div[@class="article_con clear"]/p/text()')
  content_lst += chapter_text
  num = 0
  page_num_str = chapter_tree.xpath('//ul[@id="pagebar"]/li[1]/a/text()')
  if len(page_num_str) > 0:
    print(page_num_str[0])
    num = int(re.findall(r'\d+', page_num_str[0])[0])
  if num > 1:
    for i in range(2, num + 1): 
      p_url_right = a_href.rsplit('/', 1)[-1].split('.')[0] + '_' + str(i) + '.html'
      p_url_left = a_href[:a_href.rfind('/')]
      p_url = base_url + p_url_left + '/' + p_url_right
      print(p_url)
      cha_page = requests.get(p_url)
      chapter_tree = html.fromstring(cha_page.content.decode('gbk', 'ignore'))

      img_info = chapter_tree.xpath('//div[@class="article_con clear"]/img')
      for img in img_info:
        img_lst.append(base_url + img.attrib['src'])
      chapter_text = chapter_tree.xpath('//div[@class="article_con clear"]/text()')
      content_lst += chapter_text

      img_info = chapter_tree.xpath('//div[@class="article_con clear"]/p/img')
      for img in img_info:
        img_lst.append(base_url + img.attrib['src'])
      chapter_text = chapter_tree.xpath('//div[@class="article_con clear"]/p/text()')
      content_lst += chapter_text
  book ={ 
          "title": title, 
          "content": content_lst,
          "imgs": img_lst, 
        }
  json_str = json.dumps(book, ensure_ascii=False)
  file_name = str(chapter_num) + '.json'
  with open(file_name,'w', encoding="utf-8") as f:
    f.write(json_str)
  print(file_name + ' is OK.')
  chapter_num = chapter_num + 1 
  
  
