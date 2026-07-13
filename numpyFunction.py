import numpy as np

#different Types of arrays:
arr=np.array([10,20,30,40])
print("1 dimensional array:")
print(arr)

arr1=np.array([[12,13,14,15],[16,23,12,11]])
print("2D array:")
print(arr1)

arr2=np.array([[[10,20,30],[20,30,40]],[[20,10,30],[20,30,10]]])
print("3D array")
print(arr2)

#array reshape:
new_array=arr.reshape(2,2)
print(new_array)

#array elements data type:
print("Data type of 1D array:")
print(arr.dtype)
print("Data type of 2D array:")
print(arr1.dtype)
print("Data type of 3D array:")
print(arr2.dtype)

#array of one's:
arr4=np.ones((3,4))
print(arr4)
 
#array of zero's:
arr5=np.zeros((3,4))
print(arr5)

#Random values of array:
arr6=np.random.random((2,3))
print(arr6)

#Create an empty array:
arr7=np.empty((2,3))
print(arr7)

#Create an full array:
arr8=np.full((2,3),6)
print(arr8)



