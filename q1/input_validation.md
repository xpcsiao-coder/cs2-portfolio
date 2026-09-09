**Part A**

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
