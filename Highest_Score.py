#python is extremely number friendly which has a lot of built-in function to help us work with numbers.

student_scores = [150, 140, 130, 80, 90, 60, 30, 20, 50, 100, 120, 140, 155, 180, 90, 40, 30, 10]
total_exam_score = sum(student_scores) #this built-in function will help to provide the sum of the numbers or scores above.
print(total_exam_score)

sum = 0
for score in student_scores:
    sum += score
    print(sum) #yesari indentation lagayera garda each number ma aafu bhnada agadi ko number add hunxa ani sum operation is carried out.

#print(sum)  #indentation yesto bhako bhaye it would directly print out the sum at last after the loop is over.

#maximum number in the list thhapauna lai.

print("Welcome to maximum number generator!")
scores_of_student = [20, 80, 90, 10, 15, 25, 91, 40, 60, 77]
max_score = 0

for score in scores_of_student:
    if score > max_score:
        max_score = score

print(max_score)