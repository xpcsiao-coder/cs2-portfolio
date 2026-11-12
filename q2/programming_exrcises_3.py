for num in range(1, 16):   #The range of numbers start from 1 and ends at 15, right before 16.
    if num % 3 == 0:   #The modulo (%) divides the number by 3 and checks if the remainder is 0.
        continue   #If the remainder is 0, it skips the number and continues with the loop.
    print(num)   #Prints the number that passes through the multiple by 3 check.
