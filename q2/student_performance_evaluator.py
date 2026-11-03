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
