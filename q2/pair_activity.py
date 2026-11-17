def calculate_total_hours(day1, day2, day3):
  return (day1 + day2 + day3) / 3

def get_participation_level(total_hours):
  if total_hours >= 8:
    return "Highly Active"
  elif total_hours >= 5:
    return "Active"
  else:
    return "Needs Improvement"

def is_certificate_eligible(total_hours, quiz_score):
  return total_hours >= 8 and quiz_score >= 80

day1 = float(input("Enter Total Hours during Day 1: "))
day2 = float(input("Enter Total Hours during Day 2: "))
day3 = float(input("Enter Total Hours during Day 3: "))
quiz_score = int(input("Quiz Score: "))

total_hours = calculate_total_hours(day1, day2, day3)

print("-----------------------------")
print(f"Total Volunteer Hours: {total_hours:.2f}")
print("Participation Level:", get_participation_level(total_hours))
print("Eligibility:", is_certificate_eligible(total_hours, quiz_score))
