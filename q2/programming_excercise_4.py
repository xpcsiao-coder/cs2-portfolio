def show_table(number):   #This is the function "show_table()".
  for i in range(1, 11):   #The range of numbers for 'i' start with 1 and ends at 10, before 11.
    print(number, "x", i, "=", number * i)   #It then gets number and multiplies it with the range of i.

number = int(input("Give a number: "))   #This asks the user for a number for the multiplication table.
print(show_table(number))   #This then prints the function, and the multiplication table is complete.
