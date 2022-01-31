stud_names = []
stud_scores = []
number_of_student = int(input("How many students do you have? "))

if number_of_student > 0 :
    for i in range(number_of_student):
        print(i+1)
        names = input('name of student:' )  
        score = int(input('student score:'))
        stud_names.append(names) 
        stud_scores.append(score)  
print(stud_names)
print(stud_scores)


   







