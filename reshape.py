import numpy as np 
#reshape function changes the shape of given array
#shape is the number of item in each dimension

nums=np.array([1,2,3,4,5,6])
print(nums.shape) #(5,)--> 1D

#we can reshape it

nums=nums.reshape(2,3) #note 2*3 means : 2 rows and 3 column
print(nums)
#[[1 2 3]
 #[4 5 6]]

nums=nums.reshape(3,2) #note 2*3 means : 2 rows and 3 column
print(nums)
'''[[1 2]
 [3 4]
 [5 6]]'''

nums=nums.reshape(6,1) #note 2*3 means : 2 rows and 3 column
print(nums)
'''
[[1]
 [2]
 [3]
 [4]
 [5]
 [6]]'''

#we can use -1 this is called "unknown" dimention -python and Numpy will find the value
nums1=np.array([1,2,3,4,5,6,7,8,9])
nums1=nums1.reshape(3,-1)
print(nums1)
'''
[[1 2 3]
 [4 5 6]
 [7 8 9]]'''

#exercise

x=np.array([[1,2,3],
   [4,5,6],
   [7,8,9]])

#we have to reshape into one dimention [1,2,3,4,5,6,7,8,9]
x=x.reshape(-1)
print(x)
#[1 2 3 4 5 6 7 8 9]