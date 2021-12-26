import numpy

arr = numpy.array([1,2,3,4,5]) 
print(type(arr)) #<class 'numpy.ndarray'>
print(arr.shape) #(5,)

#shape: 행과 열의 차원을 표시해주는 속성

arr2 = numpy.array([[1,2],[3,4],[5,6]])
print(arr2) #[[1 2]
            # [3 4]
            # [5 6]]
print(arr2.shape) #(3,2)
 



#1. array 함수를 이용해서 배열 생성하기
arr1 = numpy.array([1,2,3,4,5])
print('arr1', arr1)

#2. full 함수를 이용해서 배열 생성하기
arr2 = numpy.full(3,7)
print('arr2', arr2)

#3. zeros 함수를 이용해서 배열 생성하기
arr3 = numpy.zeros(7,dtype=int)
print('arr3',arr3)

#4. ones 함수를 이용해서 배열 생성하기
arr4 = numpy.ones(4,dtype=int) #ones(n, dtype): 1이 n개 있는 배열 생성, default 자료형은 float64
print('arr4',arr4)

#5. random 모둘을 이용해서 랜덤한 값의 배열 생성하기
## random(n): 랜덤한 정수가 n개 있는 배열 생성
arr5 = numpy.random.random(5)
print('arr5', arr5)
## choice(number,n): 0부터 number미만의 숫자 중 랜덤한 n개의 정수로 이루어진 배열 생성
arr5_1 = numpy.random.choice(100,5)
print('arr5_1', arr5_1)

#6. arange 함수를 이용해서 연속된 값의 배열 생성하기
arr6 = numpy.arange(6)
arr6_1 = numpy.arange(2,8)
arr6_2 = numpy.arange(3,16,3)
print('arr6',arr6)
print('arr6_1',arr6_1)
print('arr6_2',arr6_1)