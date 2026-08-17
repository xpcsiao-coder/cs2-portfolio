#Programming Activity: Calculating the Distance Between Two Points
import math 

#Get the coridnates from the user. :p
x1 = float(input("Enter x1: "))
x2 = float(input("Enter x2: "))
y1 = float(input("Enter y1: "))
y2 = float(input("Enter y2: "))

#Calculate the distance of the given. ;0
distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

#What is the formula? :O
print("The distance between the points are:", format(distance, ".2f"))

#Reflection:
#The Math library makes this activity a lot easier, making me not do extra research about certain stuff and also providing nieche functions like sqrt() and pow(). Without it, I may have a had a harder time trying to actually do this and might resort to manual coding. In conclusion, the math library was very helpful to me.
