# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 08:39:46 2018

@author: yhlee
"""

import pandas.util.testing as tm; tm.N = 3
import numpy as np
import pandas as pd

# 연습용 데이터셋 생성 함수
def unpivot(frame):
    N, K = frame.shape
    data = {'value' : frame.values.ravel('F'),
            'variable' : np.asarray(frame.columns).repeat(N),
            'date' : np.tile(np.asarray(frame.index), K)}
    return pd.DataFrame(data, columns=['date', 'variable', 'value'])
df = unpivot(tm.makeTimeDataFrame())

# 부분 변수 살펴보기
df[df['variable'] == 'A']

# pivot을 활용한 data reshaping


# 데이터 멜팅과 케스팅 녹인다음에 내가 원하는 현태로 만든다
# 피봇을 활용하여 내가 원하는 형태로 reshape 할 수 있음
# Excel 의 피봇테이블의 개념과 비슷
a = df.pivot(index='date', columns='variable', values='value')
df['value2'] = df['value'] * 2

# pivot으로 부분집합 만들기(엑셀의 피봇과 얼추 비슷하지만 다른 개념)
pivoted = df.pivot('date', 'variable', 'value')
pivoted = df.pivot('date', 'variable')
pivoted
pivoted['value2']