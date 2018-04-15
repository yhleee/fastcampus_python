# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 10:38:13 2018

@author: yhlee
"""


import requests
from bs4 import BeautifulSoup
import re
import ast

base_url = 'https://movie.naver.com/movie/bi/mi/point.nhn?code='
base_iframe_url = 'https://movie.naver.com'
# https://movie.naver.com/movie/bi/mi/point.nhn?code=18906 -> 리뷰없음
# https://movie.naver.com/movie/bi/mi/point.nhn?code=60503 -> 영화없음

crawling_data = []
for code in range(169000,172454):
    movie_url = base_url + str(code)
    req = requests.get(movie_url)
    print(movie_url)
    
    html = req.content
    soup = BeautifulSoup(html, 'lxml')
    iframe = soup.find_all('iframe')
    
    # 영화가 존재하지 않는 경우 체크
    if not iframe:
        continue
    
    iframe_url = base_iframe_url + iframe[0]['src']
    req = requests.get(iframe_url)
    html = req.content
    soup = BeautifulSoup(html, 'lxml')
    score_table = soup.find(name="div", attrs={"class":"score_result"})
    
    # 리뷰가 존재하지 않는 경우 체크
    if not score_table:
        continue
    
    score_list = score_table.find_all(name="div", attrs={"class":"star_score"})
    reple_list = score_table.find_all(name="div", attrs={"class":"score_reple"})
    
    for idx in range(0, len(score_list)):
        if reple_list[idx].find('p') and score_list[idx].find('em'):
            reple = reple_list[idx].find('p').text
            score = score_list[idx].find('em').text
            if int(score) < 6:
                score = '0'
            else:
                score = '1'
            crawling_data.append([reple, score])