# Fundamentals of Cybersecurity and Data Privacy
**Activity:** PSHS Secure Club Registration System
**Name:** Your Name
**Section:** Your Section
**Quarter:** 1

---

## Activity Overview
In this activity, I analyzed a cybersecurity threat and developed secure data-capture rules for a simple
PSHS Club Registration System.
The goal is to create a program that collects only necessary information and accepts only correct,
expected, and appropriate input.

---

# **PART A - CYBERSECURITY THREAT ANALYSIS**

***Case: Fake Prize***

1. *What threat is present?*
> Someone may be trying to steal information from you and potentially hacking.

2. *What clues make it suspicious?*
> It's trying to get info out of the blue without clearly stating anything that makes it trustable.

3. *What data, device, account, application or financial information could be affected?*
> Your data could potentially be sold, your whereabouts might get leaked, and the person hacking may gain access to your bank and steal your money.

4. *What should the user do?*
> The user should ignore and report it, never trust stuff that only 'claims' and not proof.

5. *What mitigation can reduce the risk?*
> Ignore suspicious messages and never giving information right away.

---

# **PART B - DATA PRIVACY AND SECURE DATA CAPTURE**

- *Student Name*
> Collect. Because this program requires the student's name.

- *Section*
> Collect. Because this program requires the student's section.

- *Club Choice*
> Collect. Because this program requires the student's club.

- *School Email*
> Collect. Because this program requires the student's school email.

- *Attendance Status*
> Collect. Because this program requires the student's attendance.

- *Password*
> Do not collect. Because this program does not require the student's personal password.

- *OTP*
> Do not collect. Because this program does not require the student's OTP.

- *Home Address*
> Do not collect. Because this program does not require the student's personal home address.

- *Parent Bank Account*
> Do not collect. Because this program does not require the student's parent bank account.

---

## Privacy Question
Why is it safer to collect only information that the program actually needs?
> Because if the programs information gets leaked, there is a huge risk in the students personal information.

---

# **PART C - SECURITY-FOCUSED VALIDATION RULES**

    | Data Captured | Expected Input        | Possible Risk      | Invalid Input           | Validation Rule         | Error Message                        |
    | Student Name  | Any name              | Missing name       | Blank                   | Mustn't be blank        | "The name cannot be blank." |
    | Section       | Dahlia                | Invalid section    | Ilang-Ilang             | Must be Dahlia          | "Your section is invalid for this activity." |
    | Club Choice   | Any of the 4 clubs    | Invalid club       | History                 | Must be any of the 4    | "Your club is invalid for this activity." |
    | School Email  | Email with "@" & "."  | Invalid email      | student.pshs.brc.edu.ph | Must have "@" and "."   | "Your email is invalid for this activity." |
    | Attendance    | Present/ Absent/ Late | Invalid attendance | Excused                 | Must be either of the 3 | "Your inputted attendance is invalid." |

---

## Secure Data Capture Questions

### 1. What should your program accept?
> Any input that is valid according to the validation rules.

### 2. What should your program reject?
> Any invalid inputs that do not meet the requirements to the validation rules.

### 3. How do your validation rules help reduce incorrect or unsafe input?
> It ensures that the necessary and accepted are the only ones accepted, making sure it excludes any invalid inputs.

---

# **PART D - SECURE PROGRAM IMPLEMENTATION**

## Security Practices Applied

### Required Input
> I made sure that if a blank name was inputted, an error message appeared that clearly describes what is wrong.

### Allowed Values
> Section, Clubs, and Attendance require specific predefined values, like how the only accepted clubs are Math, Science, Robotics, and Programming, the only section accepted is Dahlia, and attendance must only be present, absent, or late.

### Format Check
> The email address inputted must contain "@" and a ".".

### Error Messages
> Error messages are important so that the person using the program can reflect back & check where they may have inputted something wrong.

### Data Minimization
> I did not collect sensitive information like bank account number or password, since they are unnecessary for this program and ensures the online safety of the person using the program.

---

# **PART E - TESTING AND REFLECTION**

    | Test | Input Situation           | Expected Result       | Actual Output         | Result |
    | 1.   | All data valid            | REGISTRATION ACCEPTED | REGISTRATION ACCEPTED | PASS   |
    | 2.   | Blank student name        |                       |                       |        |
    | 3.   | Invalid section           |                       |                       |        |
    | 4.   | Invalid club choice       |                       |                       |        |
    | 5.   | Email missing `@`         |                       |                       |        |
    | 6.   | Email missing `.`         |                       |                       |        |
    | 7.   | Invalid attendance status |                       |                       |        |
    | 8.   | Different valid inputs    |                       |                       |        |

---

# Reflection

### 1. What is one cybersecurity threat that can affect an application or user?
> Write your answer here.

### 2. How can users reduce the risk of phishing or suspicious messages?
> Write your answer here.

### 3. How can validation rules improve the security of user input?
> Write your answer here.

### 4. Why should a program avoid collecting unnecessary personal information?
> Write your answer here.

### 5. How did SG7's input validation concepts become security practices in SG8?
> Write your answer here.
