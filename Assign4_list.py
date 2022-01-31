#From a list containing ints, strings and floats, make three lists to store them separately
lists = [3, 34.5, 'head', 67, 2.35, 'boy']
integer = []
string = []
float = []
for elem in lists:
    if type(elem) == int:
        integer.append(elem)
    elif type(elem) == str:
        string.append(elem)
    else:
        float.append(elem)
print(integer)
print(string)
print(float)

#Take inputs from user to make a list. Again take one input from user and search it in the list and delete that element, if found. Iterate over list using for loop.
req_list = list()
while True:
    Num = input('Enter input: ')
    req_list.append(Num)
    if Num == 'done' :
        break
print(req_list)

#Using range(1,101), make a list containing only prime numbers.
prime_Num = list()
for nums in range(1, 101):
    Prime = True
    for e_nums in range(2,nums):
        if nums % e_nums == 0 :
            Prime = False
            break    
            
    if Prime:
        prime_Num.append(nums)
print(prime_Num)
        
# Sorting refers to arranging data in a particular format. Sort a list of integers in ascending order ( without using built-in sorted function ). One of the algorithm is selection sort. Use below explanation of selection sort to do this.
#INITIAL LIST :
#2	3	1	45	15
#First iteration : Compare every element after first element with first element and if it is larger then swap. In first iteration, 2 is larger than 1. So, swap it.
#1	3	2	45	15
#Second iteration : Compare every element after second element with second element and if it is larger then swap. In second iteration, 3 is larger than 2. So, swap it.
#1	2	3	45	15
#Third iteration : Nothing will swap as 3 is smaller than every element after it.
#1	2	3	45	15
#Fourth iteration : Compare every element after fourth element with fourth element and if it is larger then swap. In fourth iteration, 45 is larger than 15. So, swap it.
#1	2	3	15	45

ini_list = [2, 3, 1, 45, 15]
#first iteration
a = list()
value = 0
for i in ini_list:
    value = i
    if value > i:
        print(i)



