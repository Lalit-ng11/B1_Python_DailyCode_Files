# DSA => Data Structure Algorithm
# in Python there  is List instead of Array. 

arr1= []
arr1.append(50)
arr1.append(40)
arr1.append(20)
arr1.append(15)
arr1.append(30)
# print("Array Elements are:", arr1)
#                             0   1   2   3   4
# o/p = Array Elements are: [50, 40, 20, 10, 30]

# print("The 2nd index number element is,", arr1[2])

# update operation 
# arr1[2]=60
# print("Array Values are,", arr1)
# Array Values are, [50, 40, 60, 10, 30]

# arr1.remove(10)
# print("Updated Array Values are,", arr1)
# o/p = Updated Array Values are, [50, 40, 60, 30]

# arr1.append(15)

# searching 
# show = 10 #o/p = Number is not-Present in Arr1.
# if show in arr1:
#     print("Number is Present in Arr1.")
# else:
#      print("Number is not-Present in Arr1.")
print(arr1) #[50, 40, 60, 15, 30, 15] 
# arr1.remove(15)
print("\n Before Bubble Sort=",arr1)
n=len(arr1)
for i in range(0,n):
    for j in range(i+1,n):
        if arr1[i]> arr1[j]:
            arr1[i],arr1[j] = arr1[j],arr1[i]
print("After Bubble Sort operation",arr1)

# o/p =  Before Bubble Sort= [50, 40, 20, 15, 30]
#         After Bubble Sort operation [15, 20, 30, 40, 50]

# Task= in list if it is containing diff data type values then how bubble sort gets perfomed? or what will be the result after bubble sort .
    