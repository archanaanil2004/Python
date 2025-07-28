#RECURSION PROGRAMS

#1.1) print numbers from n to 1
# def num(n):
#     if n == 0:
#         return
#     print(n)
#     num(n - 1)
# print("n numbers:")
# num(5)

#1.2)calculate the sum of n natural numbers

# def sum(n):
#     if n==1:
#         return 1
#     return n+sum(n-1)
# print("sum of first 3 natural numbers:",sum(3))

#1.3)sum of digits of a number
# def sum(num):
#     if num<10:
#         return num
#     else:
#         return (num % 10) +sum(num//10)
# n=int(input("eneter your number"))
# print(f"sum of digihits of {n} is {sum(n)}")


#1.4)Reverse a string
# def string(s):
#     if len(s)==0:
#         return ""
#     return s[-1]+string(s[:-1])
# print(string("hello"))


#LAMBDA
#2.1)find the square of a number
# square=lambda x:x*x
# print(square(5))

#2.2)check if number is even or odd

# odd_even=lambda x:"even" if x%2==0 else "odd"
# print(odd_even(6))

#2.3)to find the maximum of two numbers
# maximum=lambda a,b:a if a>b else b 
# print(maximum(10,8))


#2.4)check if string starts with A
# lambda_ = lambda s: s.startswith('A')
# print("Start A:", lambda_("Archana"))
# print("Start A:", lambda_("Ganga"))


#FUNCTION

#1.) function to return maximum from a list
# def maximum(numbers):
#     return max(numbers)
# nums = [12,88,9,76,102]
# print("Maximum:",maximum(nums))

#2.) function to return the reverse of a number
# def str(s):
#     return s[::-1]
# print("Reversed:", str("hello")) 


#3.)function that takes a string and counts the number of vowels

# def count_vowels(s):
#     vowels="aeiouAEIOU"
#     count=0
#     for char in s:
#         if char in vowels:
#             count += 1
#     return count
# vowelsss=count_vowels("Archana")
# print("Number of vowels:",vowelsss)

#4.)to check the number is palindrome

# def palindrome(num):
#     temp=num
#     rev=0
#     while num>0:
#         digit=num%10
#         rev=rev*10+digit
#         num=num//10
#     if temp==rev:
#         print("The number is palindrome")
#     else:
#         print("The number is not palindrome")
# a=int(input="enter the number:")
# palindrome(a)

#5.)a function that accepts a list and returns a new list with only even numbers
# def num(lst):
#     even = []
#     for num in lst:
#         if num % 2==0:
#             even.append(num)
#     return even
# numbers = [1,2,3,4,5,6]
# print("Even numbers:", num(numbers))

#6.)function that calculates the power of a number(without using **)
 
# def power(b,e):
#     if e==0:
#         return 1
#     return b*power(b,e-1) //recursion
# print("4^2=",power(4,2))


# def power(b,e):
#      result=1
#      for i in range(0,e):
#          result=result*b
# b=int(input("Enter the base:"))
# e=int(input("Enter the exponent:"))
# print(f"{b} raised to the power{e} is {power(b,e)}")
     