# import numpy as np

# #different Types of arrays:
# arr=np.array([10,20,30,40])
# print("1 dimensional array:")
# print(arr)

# arr1=np.array([[12,13,14,15],[16,23,12,11]])
# print("2D array:")
# print(arr1)

# arr2=np.array([[[10,20,30],[20,30,40]],[[20,10,30],[20,30,10]]])
# print("3D array")
# print(arr2)

# #array reshape:
# new_array=arr.reshape(2,2)
# print(new_array)

# #array elements data type:
# print("Data type of 1D array:")
# print(arr.dtype)
# print("Data type of 2D array:")
# print(arr1.dtype)
# print("Data type of 3D array:")
# print(arr2.dtype)

# #array of one's:
# arr4=np.ones((3,4))
# print(arr4)
 
# #array of zero's:
# arr5=np.zeros((3,4))
# print(arr5)

# #Random values of array:
# arr6=np.random.random((2,3))
# print(arr6)

# #Create an empty array:
# arr7=np.empty((2,3))
# print(arr7)

# #Create an full array:
# arr8=np.full((2,3),6)
# print(arr8)

import numpy as np
data=[10,23,45,30,50]

print("Given Array:")
print(data)

print("Mean of array:")
print(np.mean(data))

print("Median of array:")
print(np.median(data))

print("Addition of array elements:")
print(np.sum(data))

print("even numbers upto 10:")
print(np.arange(0,11,2))

print("odd numbers upto 10:")
print(np.arange(1,11,2))

print("Array of one's:")
print(np.ones((3,4)))

print("Array of zero's:")
print(np.zeros((3,4)))

print("Standard Deviation of values:")
print(np.std(data))

print("Full Array:")
print(np.full((2,2),7))

print("Identity Matrix:")
print(np.eye(4))

print("LineSpace array:")
print(np.linspace(0,1,5))

print("Random array:")
print(np.random.rand(2,4))

arr=np.array([12,23,15,10])
print("Shape of array:")
print(arr.shape)

print("Dimensions of array:")
print(arr.ndim)

print("Size of array:")
print(arr.size)

print("Data type:")
print(arr.dtype)

print("Reshaping of data:")
print(arr.reshape(2,2))

print("Flatten the Array:")
print(arr.flatten())

arr1=np.array([12,32,23,43])
arr2=np.array([10,20,30,40])
print("Concatenate two arrays:")
print(np.concatenate((arr1,arr2)))

print("Original Array:")
print(arr1)
print("Sorted array:")
print(np.sort(arr1))

print("Mathematical calculation:")
print("Array Multiplication:",arr1*arr1)

print("addition of two ARRAY:")
print(arr1+arr2)

print("subtraction of array:")
print(arr1-arr2)

print("expoential of array:")
print(arr1**arr2)





