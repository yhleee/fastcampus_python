# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 10:11:49 2018

@author: yhlee
fastcampus 데이터분석 강의자료 study (week5)

pandas 의 apply 를 연습
"""

import pandas as pd

#github 에서 데이터 가져오기
url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/Students_Alcohol_Consumption/student-mat.csv'
df = pd.read_csv(url,sep=',')
df.head()

#데이터 부분집합 추출
#loc indexer : df.loc['row indexer','colomn indexer']
#아래는 모든 열을 프린트하고, column 은 school에서 guardian 까지만 가져와 저장한다. 

stud_alcoh = df.loc[:,"school":"guardian"]

#맨 위 데이터만 프린트
stud_alcoh.head()

#익명함수 생성(일급객체로 활용)
# string.upper() 함수 - 대문자로 바꿔준다. 
capitalizer = lambda x:x.upper()


stud_alcoh['Mjob'].value_counts()
stud_alcoh['Fjob'].value_counts()

#Mjob 컬럼의 Series 에 capitalizer 를 apply 
#대문자의 series 를 리턴한다. 
stud_alcoh['Mjob'].apply(func =capitalizer)

#apply 를 사용한 연산이 복잡할 경우, 조건함수를 미리 생성해 둔다. 
#apply 의 그룹단위 연산은 transform 이다 

#x>17 이면 true 17보다 작으면 false 를 리턴하는 함수 생성 
def majority(x):
    if x>17:
        return True
    else:
        return False
    
    
#1. apply 사용하여 legal drinker column 추가
stud_alcoh['legal_drinker'] = stud_alcoh['age'].apply(majority)

#2. lambda 사용하여 legal drinker column 추가
stud_alcoh['legal_drinker'] = stud_alcoh['age'].apply(lambda x: True if x > 17 else False)

#3. 단순 로직사용하기
stud_alcoh['legal_drinker'] = stud_alcoh['age'] > 17

#4. mask 기법
mask = (stud_alcoh['age'] > 17) 
stud_alcoh['legal'] = mask

######################################
#추가연습 - 'Parent job' 추기 (Mjob + Fjob 추가, capitalize)
def parentjob(x):
    return x[0]+" "+x[1]


#2개이상의 컬럼을 가져온다
df2 = stud_alcoh[['Mjob','Fjob']]

# parent_job 을 추가한다
# axis=1 이면 모든 열에 적용. axis = 0 이면 모든 column에 적용 
stud_alcoh['parent_job'] = df2.apply(parentjob, axis=1)
