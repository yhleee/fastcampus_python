# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 23:36:06 2018

@author: yhlee
fastcampus 데이터분석 강의자료 study (week5)

pandas 의 filter- groupby_aggregation 을 연습 

"""

import pandas as pd
import numpy as np

url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
chipo = pd.read_csv(url, sep = '\t')

# $ 를 떼로 인티저로 변환
# 달러 타입 변환하기
chipo['item_price'] = chipo['item_price'].apply(lambda x: float(x[1:]))

chipo.groupby('order_id')['item_price'].sum()
# 한 사람의 주문 내에서, 가장 비싼 음식과 가장 싼 음식의 편차 column 추가하기
chipo_pricediff = chipo.groupby('order_id')['item_price'].agg(np.ptp)

#convert seriese to df 
df = chipo_pricediff.to_frame().reset_index()
df = df.rename(columns={'item_price': 'item_price_diff'})

#chipo df 에 item_price_diff 조인 
chipo = pd.merge(chipo, df, on='order_id', how='outer')


# 위와 같은 내용
chipo['item_price_diff'] = chipo.groupby('order_id')['item_price'].transform(np.ptp)


# 한 사람의 주문 내에서, 주문금액의 합, 주문개수의 합 column 추가하기
#agg / aggreate 둘다 쓸 수 있음
#agg 에서 df 의 range - range 간의 계산을 다 할 수 있다. np.ptp , sum. mean 
#특정 컬럼이 지정되어있지 않다면 계산 가능한 int 타입 컬럼을 모두 계산해버림 
chipo_counts = chipo.groupby('order_id').agg(sum).reset_index()
chipo_counts = chipo_counts.rename(columns={'quantity': 'quantity_sum', 'item_price': 'item_price_sum'})
del chipo_counts['item_price_diff']
chipo = pd.merge(chipo, chipo_counts, on='order_id', how='outer')


# 위와 같은 내용
result_data2 = chipo.groupby('order_id').transform(sum)


# 최고 인기 음식(Chicken Bowl)에 들어간 토핑 살펴보기 : 워드클라우드
import re

def text_cleaning(text):
    result_list = []
    for item in text:
        cleaned_text = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]',
                          '', item)
        cleaned_text = cleaned_text.replace("nan", "")
        result_list.append(cleaned_text)
    return result_list

chipo['choice_description'] = chipo['choice_description'].astype(str)
result_data3 = chipo.groupby('item_name').get_group('Chicken Bowl')['choice_description']
word_list = text_cleaning(result_data3)

#카운트vectorizer 리스트형태로 가져오면 어떤 단어가 많이 쓰이는지 카운트해주는 함수
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
count = CountVectorizer()
docs = np.array(word_list)
bag = count.fit_transform(docs)

items = list(count.vocabulary_.items())
sorted_items = sorted(items, key=lambda x: x[1], reverse=True)

from pytagcloud import create_tag_image, make_tags
from pytagcloud.lang.counter import get_tag_counts

taglist = make_tags(sorted_items[:20], maxsize=30)
create_tag_image(taglist, 'cloud_chipo.png', size=(900, 600), fontname='Nobile')


#apply
# 한 주문 내에서 최고 인기 음식(Chicken Bowl)이 포함되어있을 확률
chipo['has_popular'] = chipo.groupby('order_id')['item_name'].apply(lambda group: group.isin(['Chicken Bowl']))
chipo_copy = chipo
chipo_copy = chipo_copy.drop_duplicates('order_id')
has_popular_counts = chipo_copy['has_popular'].value_counts()
print(int(has_popular_counts[1]) / (int(has_popular_counts[1]) + int(has_popular_counts[0])) * 100)


# 가설의 수립과 확인 : 적은 양을 주문한 사람일수록 평균적으로 음식 하나당 비싼 음식을 먹었을 것이다.
chipo['item_price_mean'] = chipo.groupby('order_id')['item_price'].transform(np.mean)
chipo_oneOrder_customer = chipo.groupby('order_id').filter(lambda x: len(x) == 1)
chipo_twoOrder_customer = chipo.groupby('order_id').filter(lambda x: len(x) == 2)

print(chipo_oneOrder_customer['item_price_mean'].mean())
print(chipo_twoOrder_customer['item_price_mean'].mean())

#T Test : Series 데이터 혹은 List 데이터를 넣어줘야함 
from scipy import stats
tTestResult = stats.ttest_ind(chipo_oneOrder_customer['item_price_mean'], 
                              chipo_twoOrder_customer['item_price_mean'])
tTestResultDiffVar = stats.ttest_ind(chipo_oneOrder_customer['item_price_mean'], 
                                     chipo_twoOrder_customer['item_price_mean'], 
                                     equal_var=False)

# p-value : 유의한 차이가 있는가? 
# 0.05보다 낮으면 차이가 있다. 
print("The t-statistic and p-value assuming equal variances is %.3f and %.3f." % tTestResult)
print("The t-statistic and p-value not assuming equal variances is %.3f and %.3f" % tTestResultDiffVar)


#### 참고 ####
# apply : groupby object가 접근할 수 있는 하나의 column의 연산을 수행 가능, 그룹단위의 연산 리턴
#         (only series return)
# agg : groupby object가 여러 column에 접근하여 다중 연산을 수행 가능, 그룹단위의 연산 리턴
#       (series, dataframe return)
# transform : apply와 유사하지만, 그룹단위의 연산을 group내 row마다 리턴
# chipo_pricediff2= chipo.groupby('order_id').agg({'quantity': ['mean', 'std'],
#                               'item_price': ['sum', 'min']})