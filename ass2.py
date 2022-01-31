#Using range(1,101), make two list, one containing all even numbers and other containing all odd numbers
odd_numbers = []
even_numbers = []
for i in range(1,101):
    if i % 2 == 0:
        print(f'{i} is an even number')
        even_numbers.append(i)
        
    else:
        print(f'{i} is an odd number')
        odd_numbers.append(i)
        
print(even_numbers)
print(odd_numbers)