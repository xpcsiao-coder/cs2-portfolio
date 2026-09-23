valid = True

name = str(input("What is your name? "))

if name == "":
  print("The name cannot be blank.")
  valid = False

else: 
  section = str(input("What is your section? "))

  if "Dahlia" not in section:
    print("You're not eligible for this activity.")
    valid = False

  else: 
    club = str(input("What club are you in? "))

    if club != "Robotics" and club != "Science" and club != "Mathematics" and club != "Programming":
      print("You're not eligible for this activity.")
      valid = False

    else:
      email = str(input("What is your email address? "))

      if "@" not in email or "." not in email:
        print("Your email address is invalid for this activity.")
        valid = False

      else: 
        attendance = str(input("What is your attendance status? "))

        if attendance != "Present" and attendance != "Absent" and attendance != "Late":
          print("The input is not accepted.")
          valid = False

if valid is True:
  print("---------------------")
  print("REGISTRATION ACCEPTED")
  print("---------------------")
  print("Name:", name)
  print("Section:", section)
  print("Club:", club)
  print("Email Address:", email)
  print("Attendance:", attendance)

else:
  print("-------------------------")
  print("REGISTRATION NOT ACCEPTED")
  print("-------------------------")
