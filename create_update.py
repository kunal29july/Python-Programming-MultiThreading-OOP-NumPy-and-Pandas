import numpy as np

# Check the NumPy version
print(np.__version__)

# Create a NumPy array from a Python list
py_list = [1, 2, 3, 4]
numpy_list = np.array(py_list)
print(numpy_list)  # [1 2 3 4]
print(type(numpy_list))  # <class 'numpy.ndarray'>

# Creating a NumPy array directly
a = np.array([1, 2, 3])
print(a)  # [1 2 3]

# NumPy arrays enforce a single data type
b = np.array(["kunal", True, 1, 3.5])
print(b)  # ['kunal' 'True' '1' '3.5']

# Update values based on index
b[0] = "hi"
print(b)  # ['hi' 'True' '1' '3.5']

# Insert values using the insert function
b = np.insert(b, 2, "king")  # Index should be within the range
print(b)  # ['hi' 'True' 'king' '1' '3.5']

# Array properties
print(b.size)  # 5 (total number of items)
print(b.ndim)  # 1 (dimension)
print(b.shape)  # (5,) (shape: number of items in each dimension, type: tuple)

# Multi-dimensional array
mul = np.array([[1, 2, 3], [4, 5, 6]])
print(mul)
# [[1 2 3]
#  [4 5 6]]
print(mul.size)  # 6 (total number of items)
print(mul.ndim)  # 2 (dimension)
print(mul.shape) # (2, 3) (rows and columns)
print(mul[0][2]) #3

for index, row in enumerate(mul):
    print(index, row)
#0 [1 2 3]
#1 [4 5 6]
    
for i in range(len(mul)):
    for j in range(len(mul[0])):
        print(mul[i][j])
'''
1
2
3
4
5
6
'''
nums=np.array([[11,12,13],[14,15,16],[17,18,19]])
print(nums.size)
print(nums.shape)
print(nums.ndim)
"""
9
(3, 3)
2
"""

# 3 dim array
nums1=np.array([[[1,2,3]]])
print(nums1.ndim) #3
print(nums1.size)
print(nums1.shape)
"""3
3
(1, 1, 3)"""