# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 10:30:05 2018

@author: 212560227
"""

import numpy as np
 
#python default array 로 생성
arr_data = [6,7.5,8,0]

n_arr = np.array(arr_data)
print(n_arr)

n_str_arr = np.array(["a","dd","33"])

#ndarray 의 shape
print (n_arr.shape)

#n차원의데이터 생성
arr_data2 = [
        [1,2,3,4],
        [5,6,7,8]
        ]

n_arr2 = np.array(arr_data2)
print(n_arr2)
print(n_arr2.shape)

print(np.zeros((3,6)))
print(np.ones(10))

##일반 배열과 numpy 배열의 속도 비교
arr_data3 = np.arange(10e7)
arr_list=arr_data3.tolist()

def list_timecheck(list,num):
    for idx,val in enumerate(list):
        list[idx]=val*num
    return list

import time
start_time = time.time()
list_timecheck(arr_list,2)
print("--- %s second ---" % (time.time() - start_time))

start_time2 = time.time()
arr_data3*2
print("--- %s second ---" % (time.time() - start_time2))

#20배정도 차이

#numpy array 는 모양, 타입을 정형화해줘야한다. python array 랑 다름

#마스킹 - 특정인덱스를 논리적으로 리턴해서 필터링

names = np.array(["tt","ek","ey","ww","te","td","zz"])

data = np.random.randn(7,4)

print(names)

names =="tt"

print("tt :",data[names=="tt",:])
print("ek :",data[names=="ek",:])

print("tt or ek", data[(names=="tt")|(names=="ek"),:])

print(data[:,3])









