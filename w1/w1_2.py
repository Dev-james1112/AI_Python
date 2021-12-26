#numpy 배열의 인덱싱, 슬라이싱, 연산

import numpy as np

# 인덱싱
arr = np.array([2,6,8,9,12,23,27,32,35])
print(arr[0], arr[1]) #앞에서부터 인덱싱
print(arr[-9], arr[-8]) #뒤에서부터 인덱싱
print(arr[[0,1]]) #리스트로 인덱싱
print(type(arr[[0,1]])) #자료형은?: ndarray

#슬라이싱
print(arr[0:6:2]) #0번 인덱스부터 5번 인덱스까지 2칸 간격으로 슬라이싱
print(arr[::2]) #이렇게도 가능


#배열의 연산
l = [2,4,6,8,10]
l2 = []

l2 = [i*2 for i in l]
print(l2)

#넘파이의 배열은?
arr = np.array([2,4,6,8,10])
result = arr*2
print(result)


# 넘파이 배열 간의 불린 연산 
arr = np.array([38,16,1,27,55,8,19])
print(arr > 20)
print(arr%2 == 0)

#where(): 괄호 안의 조건을 만족하는 데이터의 인덱스 번호를 반환
boolArr = np.array([True, True, False, True, False, False, False])
print(np.where(boolArr))

filter = np.where(arr > 20)
print(arr[filter])