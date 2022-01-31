name = "Toju"
roll_number = 14
field = "Football"
print(f"My name is {name} and my roll number is {roll_number} my field of interest if {field}")


prime_Num = []
for nums in range(1, 101):
    isPrime = True
    for e_nums in range(2,nums):
        if nums % e_nums == 0 :
            isPrime = False    
            
    if isPrime:
        prime_Num.append(nums)
print(prime_Num)