#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 22:02:28 2017
@author: yhlee
"""

import requests
from bs4 import BeautifulSoup
import re
import ast

# 뉴스기사 리스트 크롤링
base_url = 'http://finance.naver.com/news/news_list.nhn?mode=LSS2D&section_id=101&section_id2=258'
req = requests.get(base_url)
html = req.content
soup = BeautifulSoup(html, 'lxml')  # pip install lxml
newslist = soup.find(name="dd", attrs={"class": "articleSubject"})
newslist_atag = newslist.find_all('a')
url_list = []
for a in newslist_atag:
    url_list.append("http://finance.naver.com"+a.get('href'))


# 텍스트 정제 함수
def text_cleaning(text):
    result_list = []
    for item in text:
        cleaned_text = re.sub('[a-zA-Z]', '', item)
        cleaned_text = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]',
                              '', cleaned_text)
        result_list.append(cleaned_text)
    return result_list


def removeNumberNpunct(doc):
    text = ''.join(c for c in doc if c.isalnum() or c in '+, ')
    text = ''.join([i for i in text if not i.isdigit()])
    return text


# 각 기사에서 텍스트만 정제하여 추출
# 첫번째 뉴스기사를 가져온다
req = requests.get(url_list[0])
html = req.content
soup = BeautifulSoup(html, 'lxml')
text = ''
doc = None

# 가져오는 URL : http://finance.naver.com/news/news_read.nhn?article_id=0000403170&office_id=366&mode=LSS2D&type=0&section_id=101&section_id2=258&section_id3=&date=20180406&page=1
# class:articleCont, id:content
item = soup.find("div", class_='articleCont')
text = text + str(item.find_all(text=True))
text = ast.literal_eval(text)
print ("log"+str(item))
n=len(text)
doc = text_cleaning(text[:n-12])

word_corpus = (' '.join(doc))
word_corpus = removeNumberNpunct(word_corpus)

# 텍스트에서 형태소 추출 -> pip install konlpy, jpype1, Jpype1-py3
from konlpy.tag import Twitter
from collections import Counter

nouns_tagger = Twitter()
nouns = nouns_tagger.nouns(word_corpus)
count = Counter(nouns)

# 형태소 워드 클라우드로 시각화 -> pip install pytagcloud, webbrowser
# Mac OS : /anaconda/envs/fastcampus/lib/python3.6/site-packages/pytagcloud/fonts
# Windosw OS : C:\Users\USER\Anaconda3\envs\pc36 (가상환경주소) \Lib\site-packages\pytagcloud\fonts
# 위 경로에 NanumBarunGothic.ttf 파일 옮기기
import random
import pytagcloud
import webbrowser

ranked_tags = count.most_common(40)
taglist = pytagcloud.make_tags(ranked_tags, maxsize=80)
pytagcloud.create_tag_image(taglist, 'wordcloud.jpg', size=(900, 600), fontname='Korean', rectangular=False)