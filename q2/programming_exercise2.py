destinations = ["Cebu", "Manila", "Davao", "Baguio", "Palawan",] #This is the array destinations, with the destinations inside being: Cebu, Manila, Davao, Baguio, and Palawan respectively.

print("Destinations:")   #This part just simply prints "Destinations", then goes to the for loop.
for place in destinations:
  print(place)   #The for loop then displays all destinations until all are displayed.

print()   #Space
print("Destinations from index 1 to 3:")   #Just prints "Destinations from index 1 ro 3:". :0
print(destinations[1:4])   #Then this part uses slicing, basically; it starts at 1, and ends before 4, thats why it is '[1:4]'. The colon sign is the slice. The numbers represent the index.

print   #Space number 2
search = str(input("Enter a destination to search: "))   #This part requires an input from the user. Basically, it asks the user to input a destination.

if search in destinations:   #Then this part checks whether it is in the list, more specifically 'in' checks if the input is in the list.
  print("Destination exists in the list.")
else:   #And if its not, it goes here and prints"Destination does not exist in the list.".
  print("Destination does not exist in the list.") 

destinations[2] = "Iloilo"   #And then this part replaces the initial lists index 2 with 'Iloilo'

print()   #Finally, this last part prints the updated destinations.
print("Updated destinations:")
print(destinations)   #Tapos na :).
