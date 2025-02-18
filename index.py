# write a program to print number from -1 to -10
# def numbers():
#     for i in range (-1,-11,-1):
#         print(i)
# numbers()

# for i in range(-1,-11,-1):
#     print(i)


# def search_num(list,search):
#     index = 0
#     for num in list :
#         if num == search:
#             return index
#         index += 1
#     return -1
# list = [2,4,6,8,79,10] 
# search = float(input("enter a number")) 
# index = search_num(list , search)  
# if index != -1:
#     print(index)
# else:
#     print("not found")


# def duplicates (list):
#     unique =[]
#     duplicate = []
#     for i in list:
#         if i in unique:
#             duplicate.append(i)
#         else:
#             unique.append(i)
#     print(unique) 
#     print(duplicate)  
# duplicates([1,2,3,4,56,7,2,1,10]) 


# def nearestprime(n):
#     if isprime(n):
#         return n
#     if abs(n - leftprime(n) <= abs (n)):
#         return leftprime(n)
#     return rightprime(n)
# def isprime(n):
#     if n < 2:
#         return False
#     for i in range (2,int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return True
# def rightprime(n):
#     while not isprime(n):
#         n+=1
#     return n
    
# def leftprime(n):
#     while n>1 and not isprime(n):
#         n-=1
#     return n
# print(nearestprime(15))   

# Sum of elements in a List.
# list1=[2,4,6,8,9,10,15]
# sum=0
# for i in list1:
#     sum+=i
# print(sum)

# Finding the k Element which is present in a List

# num=[10,11,13,15,20,25]
# k=2
# for i in range(len(num)):
#     if i == k:
#         print(num[i])
#         break


# Wap to print duplicates and unique numbers in an array/List.

# my_list=[1,2,3,4,5,2,7,1,8,8,9,5,3,4,9,2]
# duplicates=[]
# unique=[]
# for num in my_list:
#     if my_list.count(num) > 1 and num not in  duplicates:
#         duplicates.append(num)
#     elif my_list.count == 1:
#         unique.append(num)
# print(duplicates)
# print(unique)

# ) Count Occurrences of Each Digit
# input: 2788
# output: 2=> 1
# 7=> 1
# 8=> 2

# def count_digits(num):
#     num_str = str(num)
#     digit_count = {}

#     for digit in num_str:
#         if digit in digit_count:
#             digit_count[digit] += 1
#         else:
#             digit_count[digit] = 1

#     for digit, count in digit_count.items():
#         print(f"{digit} => {count}")

# Example usage
count_digits(2788)

# Reverse an Array.
# num=12345  #reverse
# rev_num=0
# while num >0:
#     rem= num % 10
#     rev_num = rev_num * 10 + rem
#     num = (num // 10)
# print(rev_num)