# Beginning: create variables
america_points = 0
notamerica_points = 0


# Middle: Ask questions
answer = input("should you own a arsenal of fighter jets and tanks? A) yes, or B) why would i have that?\n")
if answer == "A":
    america_points += 1
elif answer == "B":
   notamerica_points += 1


answer = input("Do you randomly start singing the national anthem? A) never, or B) at least 3+ times a day\n")
if answer == "A":
    notamerica_points += 1
elif answer == "B":
    america_points += 1


answer = input("Do you know what geography is? A) yes, or B) Did you say oil?\n")
if answer == "A":
    notamerica_points += 1
elif answer == "B":
    america_points += 1


answer = input("How many times do you eat fast food a week A) I have 53.7 million points on my McDonald's acount, or B) maybe once a week\n")
if answer == "A":
    america_points += 1
elif answer == "B":
    notamerica_points += 1


answer = input("what is the biggest sport in the world? A) Soccer, or B) Football\n")
if answer == "A":
    notamerica_points += 1
elif answer == "B":
    america_points += 1 


    answer = input("How high lifted is your pickup truck? A) what does that even mean?, or B) You mean my pickup trucks?\n")
if answer == "A":
    notamerica_points += 1
elif answer == "B":
    america_points += 1 


# End: determine result
if america_points > notamerica_points:
    print ("You are a true bread american")
elif america_points < notamerica_points :
    print ("you are not american")
elif america_points == notamerica_points :
    print ("I have no idea what u are")






