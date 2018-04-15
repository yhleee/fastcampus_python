# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 12:26:09 2018

@author: 212560227JJ
"""

import pickle
import os

vect_read = pickle.load(open(os.path.join('vectorizer.pkl'), 'rb'))
lrm_read = pickle.load(open(os.path.join('classification_model.pkl'), 'rb'))

test = [input("영화평을 입력하세요: ")]

test_tfidf = vect_read.transform(test)
result = lrm_read.predict(test_tfidf)



if (result =='1'):
    print ('You like the movie')
else :
    print ('You hate the movie')
