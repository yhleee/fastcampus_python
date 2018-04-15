# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 11:41:14 2018

@author: yhlee
"""

import os
import numpy as np

# 탭 구분 txt 읽는 함수
def read_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = [line.split('\t') for line in f.read().splitlines()]
        data = data[1:]
    return data

# 리뷰데이터
train_data = read_data('/Users/212560227/Documents/0.Yunhee/Python/ratings_train.txt')
test_data = read_data('/Users/212560227/Documents/0.Yunhee/Python/ratings_test.txt')
# tf-idf 진행
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier

vect = TfidfVectorizer()
sentences_column = [x[1] for x in train_data]
y_train = [x[2] for x in train_data]
X_train = vect.fit_transform(sentences_column)
X_train.todense()


# 로지스틱 분류기 학습 : 약 81% 정확도
from sklearn.linear_model import LogisticRegression
lrm = LogisticRegression()
lrm.fit(X_train, y_train)

sentences_column = [x[1] for x in test_data]
y_test = [x[2] for x in test_data]
X_test = vect.transform(sentences_column)
lrm.score(X_test, y_test)

# 실제 텍스트로 테스트
test_data = ["보다가 잠들었다"] # label : 0
test_data = ["흥미진진"] # label : 1
test_tfidf = vect.transform(test_data)
lrm.predict(test_tfidf)

# 매번 학습을 하지 않고 메모리에 올려놓고 사용하기만 하면 됨
# 응용 어플리케이션 임베딩을 위한 모델 관련 파일 저장
import pickle
import os

pickle.dump(vect, open(os.path.join('vectorizer.pkl'), 'wb'))
vect_read = pickle.load(open(os.path.join('vectorizer.pkl'), 'rb'))

pickle.dump(lrm, open(os.path.join('classification_model.pkl'), 'wb'))
lrm_read = pickle.load(open(os.path.join('classification_model.pkl'), 'rb'))