import numpy as np 

nums=np.array([1,2,3,4,5,6,7,8,9,10])
print(nums[:6]) #[1 2 3 4 5 6]
print(nums[-1]) #10
print(nums[2:len(nums)])#[ 3  4  5  6  7  8  9 10]
print(nums[2:])# [3  4  5  6  7  8  9 10]

#step size
print(nums[0:len(nums):2])#[1 3 5 7 9]


#if step size is negative
# if something is wrong then it will give []
print(nums[::-1]) #[10  9  8  7  6  5  4  3  2  1]
print(nums[-2:-5:-1]) #[9 8 7]