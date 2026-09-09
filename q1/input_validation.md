##Part A

    | Test  | Expected Input | Validation Type   | Rule                              | Invalid Example  | Error Message            |
    | Name  | Text           | Presence          | Name cannot be blank              |       " "        | "Your name is invalid."  |
    | Age   | Integer        | Data type + Range | Age cannot be < 11 or > 18        |     "10, 19"     | "Your age is invalid."   | 
    | Grade | Integer        | Range             | Grade < 7 or > 12                 |     "6, 13"      | "Your grade is invalid." |
    | Email | Text           | Pattern           | Email requires "@brc.pshs.edu.ph" | "studentpshsbrc" | "Your email is invalid." |
    | Code  | Text           | Length            | Code needs at least 6 digits      |     "12345"      | "Your code is invalid."  |

## Validation Questions 

### 1. Why should the student name not be blank?
> Because there is no name that's just a blank.

### 2. Why should age be checked for both data type and range?
> Because it needs to be an age fit for the program.

### 3. Why should grade level only accept specific values?
> Because we're only targeting for grades 7 - 12.

### 4. What format requirements did you use for the email address?
> The email requires "@brc.pshs.edu.ph" .

### 5. What length requirement did you use for the registration code?
> The length I used for the registration code is 6.

------------------------------------------------------------------------------------------------------------------------------------------
# Part C

## Programming Language used
> python

## Source code file
> 

## Final code
"valid = True

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
  print("-------------------------")"

----------------------------------------------------------------------------------------------------------------------------------------
  ## Validation Techniques Used
  
### Presence Validation
Explain where you used presence validation.
> I used it for the name because a name needs the presence of letters.

### Data Type Validation
Explain where you used data type validation.
> I used it for getting the age because an age requires a specific data type.

### Range Validation
Explain where you used range validation.
> I used the range for the age and grade level because there is a minimum and maximum number for each.

### Acceptable Value Validation
Explain where you used acceptable value validation.
> I used the acceptable value for the age and grade level because there is a specific range for each.

### Pattern Validation
Explain the simple pattern rule you used.
> I used it for the email because the only email that is strictly allowed requires "@brc.pshs.edu.ph".

### Length Validation
Explain the length rule you used.
> I used it for the registration code because the registration code must be at least a 6 digit code.
----------------------------------------------------------------------------------------------------------------------------------------
# Part D - Testing

*Test your program using both valid and invalid inputs.*

    | Test | Input                        | Validation       | Expected Output         | Actual Output           | Result |
    |  1.  | All inputs valid             | Normal Case      | "REGISTRATION ACCEPTED" | "REGISTRATION ACCEPTED" |  PASS  |
    |  2.  | Blank student name           | Presence         | "Your name is invalid"  | "Your name is invalid"  |  PASS  |
    |  3.  | Age = 'fourteen'             | Data type        | "Your age is invalid"   | "Your age is invalid"   |  PASS  |
    |  4.  | Age = '11'                   | Minimum boundary | "REGISTRATION ACCEPTED" | "REGISTRATION ACCEPTED" |  PASS  |
    |  5.  | Age = '18'                   | Maximum boundary | "REGISTRATION ACCEPTED" | "REGISTRATION ACCEPTED" |  PASS  |
    |  6.  | Age = '10'                   | Range            | "Your age is invalid"   | "Your age is invalid"   |  PASS  |
    |  7.  | Grade Level = '13'           | Acceptable value | "REGISTRATION ACCEPTED" | "REGISTRATION ACCEPTED" |  PASS  |
    |  8.  | Email = 'studentpshs.edu.ph' | Pattern          | "Your email is invalid" | "Your email is invalid" |  PASS  |
    |  9.  | Registration Code = 'ABC'    | Length           | "Your code is invalid"  | "Your code is invalid"  |  PASS  |
    |  10. | Registration Code = 'CS2026' | Valid Length     | "REGISTRATION ACCEPTED" | "REGISTRATION ACCEPTED" |  PASS  |

-----------------------------------------------------------------------------------------------------------------------------------------
# Part E - Output Verification

*Choose any **three tests** from Part D.*

## Verification Test 1
**Input:**
> '11'

**Expected Output:**
> "REGISTRATION ACCEPTED"

**Actual Output:**
> "REGISTRATION ACCEPTED"

**Result:** PASS 

**Explanation:**
> Because 11 is the minimum range for the age

---

## Verification Test 2
**Input:**
> '18'

**Expected Output:**
> "REGISTRATION ACCEPTED"

**Actual Output:**
> "REGISTRATION ACCEPTED"

**Result:** PASS 

**Explanation:**
> Because 18 is the maximum range for the age

---

## Verification Test 3
**Input:**
> 'CS2026'

**Expected Output:**
> "REGISTRATION ACCEPTED"

**Actual Output:**
> "REGISTRATION ACCEPTED"

**Result:** PASS 

**Explanation:**
> Because it meets the requirement of needing 6 digits / letters

-----------------------------------------------------------------------------------------------------------------------------------------
# Reflection

Answer briefly.

### 1. Why should a program validate input before processing it?
> So that the output won't be incorrect

### 2. What is the difference between input validation and output verification?
> Input validation happens while the program is running while output verification is verifying it with output

### 3. Which validation technique was easiest for you to implement? Why?
> Range, because I only have to add less than (<) or greater than (>) signs

### 4. Which validation technique was most challenging? Why?
> Length, because I originally didn't know how to do it / implement it

### 5. How did testing invalid inputs help you improve your program?
> To ensure it's fully functioning and produce right expected results
