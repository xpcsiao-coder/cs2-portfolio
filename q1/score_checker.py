#Get the score of the student.
score = int(input("What is your score? "))

#Identify whether his/her score is Invalid.
if score < 0 or score > 100: 
  print("Invalid, try again.")

#Now identify whether his/her score is Outstanding, Very Satisfactory, Satisfactory, or Needs Improvement.
elif score >= 90: 
  print("Outstanding, Very good.")

elif score >= 80:
  print ("Very satisfactory, Great job.")

elif score >= 75: 
  print("Satisfactory, Good job.")

else: 
  print("Needs improvement.")
