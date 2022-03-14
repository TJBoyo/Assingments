#Write a function to check if a number is prime or not.
from re import I


def prime_numbers(nums):    
    for e_nums in range(2,nums):
        if nums % e_nums == 0 :
            Prime = False
            print('This is not a prime number')
            break 
    else:
        print('This is a prime number')   

prime_numbers(7)

#Write a function to find factorial of a number but also store the factorials calculated in a dictionary
f = dict()
def factorial():
    num = int(input("Enter a number: "))
    factorial = 1
    if num >= 1:
        for i in range (1,num+1):
            factorial = factorial * i
    print("Factorail of ",num , " is : ",factorial)
    f[num] = factorial

factorial()
print(f)
   
#Write a function “perfect()” that determines if parameter number is a perfect number. Use this function in a program that determines and prints all the perfect numbers between 1 and 1000.
#[An integer number is said to be “perfect number” if its factors, including 1(but not the number itself), sum to the number. E.g., 6 is a perfect number because 6=1+2+3].
def perfect(p_num):
    sum = 0
    if p_num >= 1:
        for i in range(1, p_num):
            if p_num % i == 0:
                sum += i
        if sum == p_num:
            print(f"{p_num} is a perfect number")
        
for i in range(3, 1000):
    perfect(i)