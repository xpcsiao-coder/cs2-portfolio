score1 = float(input("Enter Score 1: "))
score2 = float(input("Enter Score 2: "))
score3 = float(input("Enter Score 3: "))

tasks = int(input("Completed Tasks: "))

def calculate_average(score1, score2, score3):
    return (score1 + score2 + score3) / 3

average = calculate_average(score1, score2, score3)

def get_performance(average):
    if average >= 85:
        return "Mastery"
    elif average >= 70:
        return "Developing"
    else:
        return "Needs Review"

performance = get_performance(average)

def is_eligible(average, completed_tasks):
    return average >= 85 and completed_tasks >= 3

eligible = is_eligible(average, tasks)

print(f"Average: {average:.2f}")
print(f"Performance: {performance}")
print(f"Eligible for Challenge: {eligible}")

#1. Which function returns a number, which returns a string, and which returns a Boolean?
#> The function calculate_average() returns a number, The function get_performance() returns a string, and the function is_eligible() returns a boolean.

#2. Explain how the average moves from calculate_average() into get_performance().
#> calculate_average() returns the average, then gets stored in the variable average, then finally gets gets passed to get_performance()

#3. What happens when a student has a high average but has completed fewer than three tasks?
#> Then they are not eligible for the challenge. To be eligible for this acrivity, the student must have an average of 85 and has at least completed 3 tasks

#4. Why is return more appropriate than simply printing the result inside each function?
#> return gives the result back to the program to be stored, reused, or passed to another function, while print just simply prints the result
