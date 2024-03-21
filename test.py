import sys

sys.path.append("C:\\Users\\rex09\\Desktop\\test_python_embed\\package_list\\requests")
sys.path.append("C:\\Users\\rex09\\Desktop\\test_python_embed\\package_list\\urllib3")
sys.path.append("C:\\Users\\rex09\\Desktop\\test_python_embed\\package_list\\chardet-main")
sys.path.append("C:\\Users\\rex09\\Desktop\\test_python_embed\\package_list\\charset_normalizer")
sys.path.append("C:\\Users\\rex09\\Desktop\\test_python_embed\\package_list\\idna")
sys.path.append("C:\\Users\\rex09\\Desktop\\test_python_embed\\package_list\\certifi")
sys.path.append("C:\\Users\\rex09\\Desktop\\test_python_embed\\package_list\\soupsieve")
bs4_path = "C:\\Users\\rex09\\Desktop\\test_python_embed\\package_list\\beautifulsoup4"
if bs4_path not in sys.path:
    sys.path.append(bs4_path)





import requests
import urllib3
import chardet
import charset_normalizer
import idna
import certifi
from bs4 import BeautifulSoup
import soupsieve
from selenium import webdriver


# print(requests) 

from requests import get

import requests
web = requests.get('https://water.taiwanstat.com/') 
# print(web.text)    

# print('\n', requests, "\n", urllib3, '\n', chardet, '\n', charset_normalizer, '\n', idna, '\n', certifi, '\n', BeautifulSoup, '\n', soupsieve, '\n')

# html_doc = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title"><b>The Dormouse's story</b></p>

# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>

# <p class="story">...</p>
# """

# soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.title.string)