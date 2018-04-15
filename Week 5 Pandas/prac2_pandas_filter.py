# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 22:47:11 2018
@author: yhlee
fastcampus 데이터분석 강의자료 study (week5)

pandas 의 filter 를 연습 
"""

import pandas as pd

#github 에서 데이터 가져오기
url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/Students_Alcohol_Consumption/student-mat.csv'
df = pd.read_csv(url,sep=',')

# 데이터 부분집합 추출
# loc : 라벨값 기반의 2차원 인덱싱을 가져온다.
# [row 값, column 값] : 는 모두 가져오겠다는것 
stud_alcoh1 = df.loc[: , "school":"guardian"]

#두가지 column 만 가져오기 
stud_alcoh2 = df[['school', 'guardian']]


############################################################
# 여러가지 필터링 방법

#조건을 걸어 부분 집합 추출 
#more_than_16 이라는 조건에 맞는 row 들만 저장된 DataFrame 이 생성된다. 
more_than_16 = stud_alcoh1[stud_alcoh1.age > 16]

#조건문
#위의 부분집합 추출의 [] 내에 조건문을 넣을 수 있다. 
middle_school = stud_alcoh1[(stud_alcoh1['age'] > 13) & (stud_alcoh1['age'] < 16)]

#T 와 A 두가지의 PStatus 가 있음을 알 수 있음 
#T가 아닌 value 가져오기 
stud_alcoh1['Pstatus'].value_counts()
not_T_status = stud_alcoh1[(stud_alcoh1['Pstatus'] != 'T')]

#text mining 할 때 유용한 코드 
#str.family size 가 큰 걸 가져오고싶다 - G가 큰걸 가져오고싶을때?
contains_G = stud_alcoh1[stud_alcoh1.famsize.str.contains('G')] # startswith 등 활용가능

#관심있는 컬럼 3개만 가져오기 
mother_job = stud_alcoh1.loc[stud_alcoh1.Mjob.isin(['at_home', 'services']), ['Mjob','Fjob', 'reason']]
