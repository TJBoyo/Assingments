#From the two list obtained in previous question, make new lists, containing only numbers which are divisible by 4, 6, 8, 10, 3, 5, 7 and 9 in separate lists.
odd_numbers = []
even_numbers = []
for i in range(1,101):
    if i % 2 == 0:        
        even_numbers.append(i)
        if i % 4 == 0:
            print(f'{i} is divisible by 4')

    else:
        print(f'{i} is an odd number')
        odd_numbers.append(i)
        
#From a list containing ints, strings and floats, make three lists to store them separately
#Take inputs from user to make a list. Again take one input from user and search it in the list and delete that element, if found. Iterate over list using for loop.
#Using range(1,101), make a list containing only prime numbers.
#Sorting refers to arranging data in a particular format. Sort a list of integers in ascending order ( without using built-in sorted function ). One of the algorithm is selection sort. Use below explanation of selection sort to do this.
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
