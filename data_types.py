import numpy as np
#'i' for integer
#'f' for floating point number
#'S' for string
#'Uint' unsigned int
 
my_arr=np.array([1,2,3])
print(my_arr.dtype)#int32--> 32/8 --> 4byte 


my_arr=np.array([1,2.5,3],dtype='f')
print(my_arr.dtype) #float32

my_arr=np.array([1,2.5,3],dtype='i')
print(my_arr.dtype) #int32
print(my_arr) #[1 2 3]
