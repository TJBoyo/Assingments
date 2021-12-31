x = int(input('first_value:'))
y = int(input('second_value:'))
z = int(input('third_value:'))
if x > y and x > z:
    print(f'The greatest number is {x}')
elif y > x and y > z:
    print(f'The greatest number is {y}')
else:
    print(f'The greatest number is {z}')


# school grading
mark = input('marks:')
try:
    score = float(mark)
    if score > 100:
        print('Invalid Input')
    elif score >= 80:
        print('A')
    elif score >= 60:
        print('B')
    elif score >= 50:
        print('C')
    elif score >= 45:
        print('D')
    elif score >= 25:
        print('E')
    elif score < 25:
        print('F')
except:
    print('wrong entry')

# input from three people's age by user and determine oldest anf youngest among them 
a = int(input('First person age:'))
b = int(input('Second person age:'))
c = int(input('Third person age:'))
print('Oldest user is', max(a, b, c))
print('Youngest user is', min(a, b, c))


# A student will not be allowed to sit in exam if his attendance is less than 75%. Take following input from user number of class held numder of class attended
nch = float(input('Number of class held: '))
nca = float(input('Number of class attended: '))
attd = (nca / nch) * 100
print('percentage attendance is', attd)
if attd > 75:
    print('Proceed to sit for exam')
else:
    medical_state = input('Medical cause Y/N:')
    if medical_state == 'Y':
        print('proceed to sit for exam')
    else:
        print('cannot sir for the exam')
    
    

