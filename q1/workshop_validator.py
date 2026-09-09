valid = True

name = str(input("What is your name? "))

if name == "":
  print("Your name is invalid.")
  valid = False

age = int(input("What is your age? "))

if age < 11 or age > 18:
  print("Your age is invalid.")
  valid = False

grade = int(input("What is your grade level? "))

if grade < 7 or grade > 12:
  print("Your grade level is invalid.")
  valid = False

email = str(input("What is your email address? "))

if "@brc.pshs.edu.ph" not in email:
  print("Your email is invalid.")
  valid = False

code = str(input("What is your registration code? "))

if len(code) <6:
  print("Your registration code is invalid.")
  valid = False

if valid is True:
  print("---------------------")
  print("REGISTRATION ACCEPTED")
  print("---------------------")
  print("Name:", name)
  print("Age:", age)
  print("Grade level:", grade)
  print("Email Address:", email)
  print("Registration Code:", code)

else:
  print("-------------------------")
  print("Registration not accepted")
  print("-------------------------")
