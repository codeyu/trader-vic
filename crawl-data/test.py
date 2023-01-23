# http://www.818qihuo.com/book/zhuanyetouji/
import json
import requests        #导入requests包
from lxml import html
from lxml import etree
import re
import json

base_url = 'http://www.818qihuo.com'
book_url = '/book/zhuanyetouji/'
page = requests.get('http://www.818qihuo.com/book/zhuanyetouji/3663_2.html')
tree = html.fromstring(page.content.decode('gbk', 'ignore'))
a_info = tree.xpath('//div[@class="article_con clear"]/p/img')
img_lst = []
for img in a_info:
    print(img.attrib['src'])
    img_lst.append(img.attrib['src'])
print(img_lst)
dictionary ={ 
  "imgs": img_lst, 
  "title": "sunil", 
  "content": "HR"
}
json_object = json.dumps(dictionary, indent = 4) 
print(json_object)


  
