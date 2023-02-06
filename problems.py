# import random

# def solve(k: int, target:int):
#     result = 1
#     print(f"I chose 1 and now total is {result}")
#     while result <= target:
#         opponent = int(input(f"Enter your number from 1 to {k} : \n"))
#         while opponent > k:
#             print(f"You enterd wrong number , it should be less than {k}")
#             opponent = int(input(f"Enter your number from 1 to {k} : \n"))
#         mynum  = (k+1) - opponent 
#         result += opponent + mynum
#         print(f"I chose {mynum} and now total is {result}")
#         if result >= target:
#             print("You lost")
#             break
# solve(10,100)

# def reverse_digits(num: int) -> int:
#     if num == 0:
#         return 0
#     result = 0
#     while num != 0:
#         digit = num % 10
#         num //= 10
#         result = (result * 10) + digit
#     return result
# print(reverse_digits(num=157))

# def reverse_digits(num: int) -> int:
#     "
#""
#     Kodni bu yerda yozing.
#     """
#     stringint = str(num)
#     splitted = list(stringint)[::-1]
#     while True:
#         if splitted[0] == '0':
#             splitted.pop(0)
#         else:
#             break
#     arr = ''.join(splitted) 
#     print(arr)
#     result = 0
#     return result

# print(reverse_digits(num=7100000))

# nums = [1,15,6,3]
# for i, y in zip(nums,str(nums)):
#     print(i,y)

# a = [9,6,1,3,4,7,5,2]
# b = [0]
# if b == [0]:
#     b = a 
# print(a)
# print(b)

# def select(arr,pos):
#     start = pos
#     for i in range(pos,len(arr)):
#         if arr[i] < arr[start]:
#             start = i
#     return start


# def selection_sort(arr):
#     for i in range(len(arr)):
#         start = select(arr,i)  
#         arr[i],arr[start] = arr[start],arr[i]
#     return arr

# print(selection_sort(a))            


# def bubble(arr):
#     n = len(arr)
#     for i in range(n-1):
#         if arr[i] > arr[i+1]:
#             arr[i], arr[i+1] = arr[i+1], arr[i]
#     return arr


# def bubble_sort(arr):
#     for i in range(len(arr)):
#         arr = bubble(arr) 
#     return arr


# print(bubble_sort(a))


# nums = [3,2,2,3]
# def removeElement(nums: list, val: int) -> int:
#     if val == []:
#         return 0
#     else:
#         y = 0
#         i = 0
#         while y < len(nums):
#             if nums[y] == val:
#                 y += 1 
#             else:
#                 nums[i] = nums[y]
#                 i += 1
#                 y += 1
#         print(nums[0:i])
#         return len(nums[0:i]) 

# k = removeElement(nums=nums, val=3)
# print(k)


# str1  = "Hello world"


# while i < len(arr):
#     if arr[i] == "-":
#         arr[i] == arr 
# newArr = [el for el in arr if el != '0' elif el =]
# print(arr)
# print(newArr)
# digits = [9]
# def conv_int(digits: list[int]) -> int:
#     str_int = ""
#     for i in digits:
#         str_int += str(i)
#     return int(str_int)

# def conv__arr(num: int) -> list[int]:
#     arr = []
#     str1 = str(num)
#     for i in str1:
#         arr.append(int(i))
#     return arr



# def plusOne(digits: list[int]) -> list[int]:
#     num = conv_int(digits=digits)
#     num += 1 
#     num = conv__arr(num=num)
#     return num


# def plusOne(digits: list[int]) -> list[int]:
#         digits = digits[::-1]
#         num, i = 1, 0 
#         while num:
#             print(f"{len(digits)}=")
#             if i < len(digits):
#                 print("i < len(digits)")
#                 if digits[i] == 9:
#                     print("if digits[i] == 9")
#                     print(digits[i])
#                     digits[i] = 0
#                     print("after", digits[i])
#                 else:
#                     digits[i] += num
#                     num = 0 
#                 i += 1 
#             else:
#                 digits.append(num)
#                 num = 0
    
#         return digits[::-1]

# print(plusOne(digits=digits))