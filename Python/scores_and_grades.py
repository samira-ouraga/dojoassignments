# Write a function that generates ten scores between 60 and 100. Each time a score is generated, 
# your function should display what the grade is for a particular score.
import random
def student_grade():
    print "enter the score"
    score= random.randint(1, 100)
    print score
    if (score<100 and score>90):
        grade = "A"
        return "score:  " + str(score) + " "+ " your grade is  " + str(grade)
    elif(score<90 and score>80):
        grade = "B"
        return "score:  " + str(score) + " "+ " your grade is  " + str(grade)
    elif(score<80 and score>70):
        grade = "C"
        return "score:  " + str(score) + " "+ " your grade is  " + str(grade)
    else:
        grade = "D"
        return "score:  " + str(score) + " "+ " your grade is  " + str(grade)
print student_grade()    