#Testing for day 26 in Udemy und 
import random

#------------------------------------------

#First Task

#numbers = [1,2,3]

#new_numbers = [num + 1 for num in numbers] #num stands for each value in the list. The num parameter was added with 1 and updated the list 

#print(new_numbers)

#------------------------------------------

#Second Task

name = "Abdelilah"
new_list = [letter for letter in name] #it takes 
print(new_list)

#------------------------------------------
#Third Task

#ran_number = range(1,5)

athor_list = [number*2 for number in range(1,5)]


print(athor_list)

#------------------------------------------
#Third Task

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

short_names = [isem.upper() for isem in names if len(isem)>5]

print(short_names)


students_score = {student:random.randint(1,100) for student in names}
print (students_score)


passed_student = {student:score for(student,score) in students_score.items() if score > 60} #item is very important, this must to be there item()


print(passed_student)




sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

wordList_of_sentence = sentence.split()

result = {word:len(word) for word in wordList_of_sentence}
print(result)