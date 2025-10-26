# NumPy (Numerical Python) is a powerful Python library used to perform fast mathematical operations on arrays.
# It is especially popular in data science, machine learning, scientific computing, and engineering.

import numpy as np

##1-----------Array Creation Methods--------------

#-----1. np.array() ==> Converts a list or tuple to a NumPy array.------
print(np.array([10, 20, 30]))
#[10 20 30]

print(np.array([[5, 10, 15], [20, 25, 30]]))
#[[ 5 10 15]
 #[20 25 30]]

print(np.array((1.5, 2.5, 3.5)))
#[1.5 2.5 3.5]

#-----2. np.zeros(shape) ==> Creates an array of zeros.-------
print(np.zeros(4))
#[0. 0. 0. 0.]

print(np.zeros((3, 2)))   #3 row 2 columns
# [[0. 0.]
#  [0. 0.]
#  [0. 0.]]

print(np.zeros((2, 3, 1)))   #Creates a 3D array (think of it as 2 layers of 3×1 matrices).
# [[[0.]
#   [0.]
#   [0.]]
#
#  [[0.]
#   [0.]
#   [0.]]]

print(np.zeros((3, 1),dtype=int))  #3 rows , 1 column , dtype for float to int datatype
# [[0]
#  [0]
#  [0]]

#-----3. np.ones(shape) ==> Creates an array of ones..-------
print(np.ones((3),dtype=int))
# [1 1 1]

print(np.ones((2, 2),dtype=int))
# [[1 1]
#  [1 1]]

print(np.ones((3, 1, 2),dtype=int))  #3 blocks (or “layers”) ,1 row per block,2 columns per row
# [[[1 1]]
#
#  [[1 1]]
#
#  [[1 1]]]

#-----4. np.arange(start, stop, step) ==>Creates a range of numbers.-------
print(np.arange(2, 8))  #start -2 ,stop at 8(excluded)
# [2 3 4 5 6 7]

print(np.arange(0, 20, 5))
# [ 0  5 10 15]

print(np.arange(-5, 6, 2))
# [-5 -3 -1  1  3  5]


#-----5.np.linspace(start, stop, num) ==>Evenly spaced numbers between two limits.-------
print(np.linspace(0, 5, 6))  #start at 0,stop at 5 in 6 steps
# [0. 1. 2. 3. 4. 5.]

print(np.linspace(2, 8, 4))
# [2. 4. 6. 8.]

print(np.linspace(-1, 1, 5))
# [-1.  -0.5  0.   0.5  1. ]


##2-----------Math & Stats Methods--------------

# ------6. np.sum() ==>Adds all elements.-------
print(np.sum([1, 2, 3]))
# 6

print(np.sum([[1, 2], [3, 4]]))
# 10

print(np.sum(np.array([[1, 2], [3, 4]]), axis=0)) # Sum column-wise
#[4 6]

print(np.sum(np.array([[1, 2], [3, 4]]), axis=1)) # Sum row-wise
#[3 7]

#-------7. np.mean() ==>Average value of array elements.-------
print(np.mean([10, 20, 30]))
# 20.0

print(np.mean([[1, 2], [3, 4]]))
# 2.5

print(np.mean(np.array([[1, 2], [3, 4]]), axis=1)) # Row-wise mean
# [1.5 3.5]

#-------8.  np.median() ==>Finds the middle value..-------
print(np.median([10, 20, 30]))
# 20.0

print(np.median([10, 20, 30, 40]))
# 25.0

print(np.median([[5, 10], [15, 20]]))
# 12.5


##3-----------Array Operation Methods--------------

#-------9. np.reshape(shape) ==>to change array into specific rows and columns-------
print(np.reshape([1, 2, 3, 4], (2, 2)))   #to change array into 2row ,2columns
# ➡ [[1 2]
#     [3 4]]

print(np.reshape(np.arange(6), (3, 2)))
# ➡ [[0 1]
#     [2 3]
#     [4 5]]

print(np.reshape(np.arange(12), (2, 2, 3))) #2blocks , 2 rows in each, 3 columns in each
# ➡ [[[ 0  1  2]
#      [ 3  4  5]]
#     [[ 6  7  8]
#      [ 9 10 11]]]

#-------10. np.flatten() ==>Converts multi-dimensional to 1D.-------
print(np.array([[1, 2], [3, 4]]).flatten())
# ➡ [1 2 3 4]

print(np.array([[10, 20], [30, 40]]).flatten())
# ➡ [10 20 30 40]

print(np.array([[5], [6]]).flatten())
# ➡ [5 6]

#-------11. np.concatenate((a, b), axis) ==>Combines arrays-------
a = np.array([1, 2]); b = np.array([3, 4])
print(np.concatenate((a, b)))
# ➡ [1 2 3 4]

x = np.array([[1, 2]]); y = np.array([[3, 4]])
print(np.concatenate((x, y), axis=0))
# ➡ [[1 2]
#     [3 4]]

p = np.array([[1], [2]]); q = np.array([[3], [4]])
print(np.concatenate((p, q), axis=1))
# ➡ [[1 3]
#     [2 4]]

##4-----------Indexing and Logical Methods--------------

#-------12.np.where(condition) ==>Finds elements based on condition.-------
a = np.array([10, 20, 30])
print(np.where(a > 15))
# ➡ (array([1, 2]),)

print(np.where(a == 20))
# ➡ (array([1]),)

print(np.where(a % 10 == 0))
# ➡ (array([0, 1, 2]),)

#-------13.np.unique() ==>Returns unique values.-------
print(np.unique([1, 2, 2, 3]))
# ➡ [1 2 3]

print(np.unique([[1, 1], [2, 3]]))
# ➡ [1 2 3]

print(np.unique(['a', 'b', 'a']))
# ➡ ['a' 'b']

#-------14.np.clip(arr, min, max) ==>Limit values within a range.-------
a = np.array([10, 20, 30])
print(np.clip(a, 15, 25))
# ➡ [15 20 25]

b = np.array([-5, 0, 5, 10])
print(np.clip(b, 0, 8))
# ➡ [0 0 5 8]

c = np.array([100, 200, 300])
print(np.clip(c, 150, 250))
# ➡ [150 200 250]

##5----------- Linear Algebra Methods--------------

#-------15.np.dot(a, b) ==>Matrix multiplication.-------
print(np.dot([1, 2], [10, 20]))
# ➡ 50

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(np.dot(a, b))
# ➡ [[19 22]
#     [43 50]]

print(np.dot([[2, 3]], [[4], [5]]))
# ➡ [[23]]

#-------16.np.transpose() ==>Swap rows and columns.-------
print(np.transpose([[1, 2], [3, 4]]))
# ➡ [[1 3]
#     [2 4]]

print(np.transpose([[1, 2, 3]]))
# ➡ [[1]
#     [2]
#     [3]]

print(np.transpose([[5], [6]]))
# ➡ [[5 6]]

#-------17.np.linalg.inv() ==>Inverse of a matrix.-------
from numpy.linalg import inv
print(inv([[1, 2], [3, 4]]))
# ➡ [[-2.   1. ]
#     [ 1.5 -0.5]]

print(inv([[2, 1], [7, 4]]))
# ➡ [[ 4. -1.]
#     [-7.  2.]]

print(inv([[5, 3], [2, 1]]))
# ➡ [[ 1. -3.]
#     [-2.  5.]]


##6----------- Random Number Methods--------------

#-------18.np.random.rand() ==>Random floats [0, 1].-------
print(np.random.rand(3))
# [0.28892319 0.5623777  0.14474129]

print(np.random.rand(2, 2))
# [[0.17785241 0.50468428]
#  [0.98256767 0.62231401]]

print(np.random.rand(1, 4))
# [[0.15003214 0.58920812 0.29286097 0.97160637]]


#-------19. np.random.randint(start, stop, size) ==>Random integers in range.-------
print(np.random.randint(1, 10))
# e.g. 7

print(np.random.randint(5, 15, size=3))
# e.g. [8 10 14]

print(np.random.randint(0, 2, size=(2, 2)))
# e.g. [[1 0]
#          [0 1]]

#-------20. np.random.randn() ==>Random numbers from a normal distribution.-------
print(np.random.rand(3))
# ➡ random values like [0.12 0.45 0.89]

print(np.random.rand(2, 2))
# ➡ 2x2 random floats

print(np.random.rand(1, 4))
# ➡ [[0.34 0.65 0.90 0.12]]

print(np.random.randint(1, 10))
# ➡ e.g. 7

print(np.random.randint(5, 15, size=3))
# ➡ e.g. [8 10 14]

print(np.random.randint(0, 2, size=(2, 2)))
# ➡ e.g. [[1 0]
#          [0 1]]

print(np.random.randn(4))
# ➡ e.g. [ 0.21 -1.02  0.56  1.34]

print(np.random.randn(2, 3))
# ➡ 2x3 random normal values

print(np.random.randn(1, 2))
# ➡ [[-0.45  0.88]]


##7----------- Array Properties--------------

#-------21. .shape  ==>Dimensions of array.-------
print(np.array([[1, 2, 3], [4, 5, 6]]).shape)  #2 rows ,3 columns
# ➡ (2, 3)

print(np.array([1, 2, 3]).shape)
# ➡ (3,)

print(np.array([[7], [8], [9]]).shape)
# ➡ (3, 1)

#-------22. .ndim  ==>Number of dimensions.-------
print(np.array([1, 2, 3]).ndim)
# ➡ 1

print(np.array([[1, 2], [3, 4]]).ndim)
# ➡ 2

print(np.array([[[1], [2]], [[3], [4]]]).ndim)
# ➡ 3

#-------23. .size ==>Total number of elements.-------
print(np.array([1, 2, 3]).size)
# ➡ 3

print(np.array([[1, 2], [3, 4]]).size)
# ➡ 4

print(np.array([[[1, 2], [3, 4]]]).size)
# ➡ 4

