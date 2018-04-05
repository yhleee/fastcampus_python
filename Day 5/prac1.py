# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 10:11:49 2018

@author: 212560227
"""
import pandas as pd
url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/Students_Alcohol_Consumption/student-mat.csv'
df = pd.read_csv(url,sep=',')
df.head()

#데이터 부분집합 추출
stud_alcoh = df.loc[: , "school":"guardian"]
stud_alcoh.head()

#익명함수 생성(일급객체로 활용)
capitalizer = lambda x:x.upper()

#
stud_alcoh['Mjob'].value_counts()
stud_alcoh['Fjob'].value_counts()
stud_alcoh['Mjob'].apply(capitalizer)

#apply 를 사용한 연산이 복잡할 경우, 조건함수를 미리 생성해 둔다. 
#apply 의 그룹단위 연산은 transform
def majority(x):
    if x>17:
        return True
    else:
        return False
    
stud_alcoh['legal_drinker'] = stud_alcoh['age'].apply(majority)


#단순 로직으로도 할 수 있음. 그 외 lamda 를 써도됨 
#마스킹 기법 . 시리즈를 가져옴 
mask = (stud_alcoh['age'] > 17) 
stud_alcoh['legal'] = mask

stud_alcoh1=df.loc[: ,"school":"guardian"]
more_than_16 = stud_alcoh1['age'>16]
middle_school = stud_alcoh1[(stud_alcoh1['age']>13 and stud_alcoh1['age']<16)]

#text mining 할때 유용
#str.family size 가 큰 걸 가져오고싶다 - G가 큰걸 가져오고싶을때?
#startswith 
non_T_status = stud_alcoh1[(stud_alcoh1['Pstatus'] != 'T')]
contains_G = stud_alcoh[stud_alcoh1.famsize.str.contains('G')]

#관심있는 컬럼 3개만 가져오고싶을때
custom_list = ['at_home','service']
column_list = 
