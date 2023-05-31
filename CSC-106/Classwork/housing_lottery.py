# Created by: Evan Peck (Bucknell University)
# - Contact: evan.peck@bucknell.edu
# - Last Modified: September, 2019

# Keeps track of the point total during questions
current_score = 0

# A header to start the program
print("-------------------------------")
print("   HOUSING SCORE CALCULATOR")
print("-------------------------------")
print()

# Assign points based on class year
print("QUESTION 1")
year_ans = input("What year are you? (1, 2, 3, 4): ")

if year_ans == "1":
    current_score += 1
elif year_ans == "2":
    current_score += 2
elif year_ans == "3":
    current_score += 3
elif year_ans == "4":
    current_score += 4

# If the student is >= 22 years old, give them another point
years_old = input("How old are you?: ")

if int(years_old) >= 22:
    current_score += 1

campus_job = str(input("Do you have a campus job? (Yes/No"))


if str(campus_job) == "Yes":
    current_score += 1
    financial_aid = str(input("Is this included in financial aid? (Yes/No"))

    if str(financial_aid) == "Yes":
        current_score += 1

mobility = str(input("Do you have physical mobility issues? i.e wheelchairs, crutches etc. (Yes/No"))

if str(mobility) == "Yes": 
    current_score += 1
    permanent = str(input("Is this issue permanent? (Yes/No)"))

    if str(permanent)== "Yes":
        current_score += 1

mental_health = str(input("Do you suffer from mental health isues? (Yes/No)"))

if str(mental_health) == "Yes":
    current_score+= 1

gpa= float(input("How high is your GPA?"))

if float(gpa)>= 3.7:
    current_score+=3
elif float(gpa)< 3.69 and float(gpa) >= 3.3:
    current_score+=2
elif float(gpa) < 3.29 and float(gpa) >= 3.0:
    current_score+=1

distance= int(input("How many miles is your home from campus?"))

if int(distance)>200:
    current_score+=3
elif int(distance)<=200 and int(distance)>=150:
    current_score+=2
elif int(distance)<150 and int(distance)>50:
    current_score+=1


prob_ans = input("Have you ever been placed on academic probation? (Yes/No): ")

if prob_ans == "Yes" or prob_ans == "yes":
    current_score += 0
else:
    current_score += 1








    

# At the end of the program, tell the user their score
print()
print("------YOUR HOUSING SCORE----------")
print("Your housing points score is", current_score)
print("----------------------------------")
