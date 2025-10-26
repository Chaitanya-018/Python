import numpy as np
import time
#numerical python
#series



# compare how numpy methods are fast than the python methods
start = time.time()
for i in range(100000):
    i*2
print("time taken",time.time()-start)

start=time.time()
num_arr = np.arange(100000)*2
print("numpy time",time.time()-start)

#methods in numpy---------------------------

#arange(end)
arr2=np.arange(5000)
print(arr2)

#np.array
arr1=np.array((1,2,3,4,5))  #numpy array
print(arr1)
print(np.array([1,2,3]),"1d")
print(np.array([[1,2],[3,4]]),"2d")

#zeros
print(np.zeros(3))
print(np.zeros(6))
print(np.zeros((3,3),dtype=int))

#ones
print(np.ones(4,dtype=int))
print(np.ones((5,6),dtype=int))

#linspace
print(np.linspace(2,100,50))  #start stop stepvalue
print(np.linspace(1,1000,3))

#np.sum()
list1=[1,2,3,4,5,6,7,8,9,10]
sum=0
for i in list1:
    sum+=i
print(sum)

print(np.sum([1,2,3,4,5,6,7,8,9,10]))

#np.mean
print(np.mean([1,2,3,4,5,6,7,8,9,10]))  #we can find the average

# np.median
list2=[1,2,3,4,5]
mid=len(list2)//2  #floor division
print(list2[mid])        #list2[2]

print(np.median([1,2,3,5,5,6]))   #one dimensional

print(np.mean([[1,2],
               [3,4]],axis=0 #vertical calculations
               ))

print(np.mean([[1,2],
               [3,4]],axis=1 #horizontal calculations
               ))


#22-10-2025

mat=np.array([[1,2,3],[4,5,6]])
mat2=np.array([ [[1,2,3],[4,5,6]] ])
print(np.shape(mat))
print(np.ndim(mat2))


#reshape
dim1=np.array([1,2,3,4,5,6,7,8,9,10])
print(np.reshape(dim1,(2,5))) #2 rows 5 columns

print(np.reshape(np.arange(12),(2,2,3)))  #2dims 2row 3colums

#flatten - to change multi dimensional array into single dimensional array

arr=[[1,2,3,4,5,6],[7,8,9,10,11,12]]
print(np.array(arr).flatten())


#concatenate
a=np.array([1,2])
b=np.array([3,4])
print(np.concatenate((a,b)))

a=np.array([[1,2],[5,6]])
b=np.array([[3,4],[7,8]])
print(np.concatenate((a,b),axis=0))

#indexing and logical methods
arr=[1,2,3,4,500,6,7,0,99]
np_arr=np.array(arr)
print(np_arr)
print(np.where(np_arr>50))
print(np.where(np_arr%2==0))

#vector
#dimension and magnitude

print([1,2,3]*2)  #scalar
print(np.array([1,2,3])*2) #vector


#unique
print(np.unique([1,2,3,1,2,3,5]))


#matrix multiplication -dot method

print(np.dot([[1,2],[3,4]],
             [[5,6],[7,8]]))


#transpose - row to column
print(np.transpose([[1,2],
                    [3,4]]))


#inverse of matrix -linear algebra #only for matrix

from numpy.linalg import inv

print(np.linalg.inv([[1,2],[3,4]]))


#random
print(np.random.rand(5))  #by default float values
print(np.random.randint(6,10,3))

#size
print(np.array([1,2,3,4,5,6,7,8,9,10]).size)