<img width="2048" height="1536" alt="score_checker_flowchart" src="https://github.com/user-attachments/assets/53533fe2-06ab-4cb6-8dad-261abee22d13" />

START

INPUT score

IF score < 0 or > 100 THEN
  DISPLAY "invalid score"

ELSE IF score >= 90 THEN
  DISPLAY "Outstanding"

ELSE IF score >= 80 THEN
  DISPLAY "Very Satisfactory"

ELSE IF score >= 75 THEN
  DISPLAY "Satisfactory"

ELSE THEN
  DISPLAY "Needs Improvement"

END

-----------------------------------------------------------------------------------------------------------------------------------------

**Testing of answers / Table of answers**

| Test | Input |           Purpose           |   Expected Output   |   Actual Output   | Result |
1.     |  -1   | Below minimum               |  Invalid Score      | Invalid Score     |  PASS  |
2.     |   0   | Minimum Boundary            |  Needs Improvement  | Needs Improvement |  PASS  |
3.     |   74  | Below Satisfactory Boundary |  Needs Improvement  | Needs Improvement |  PASS  |
4.     |   75  | Satisfactory Boundary       |  Satisfactory       | Satisfactory      |  PASS  |
5.     |   80  | Very Satisfactory Boundary  |  Very Satisfactory  | Very Satisfactory |  PASS  |
6.     |   90  | Outstanding boundary        |  Outstanding        | Outstanding       |  PASS  |
7.     |  100  | Maximum boundary            |  Outstanding        | Outstanding       |  PASS  |
8.     |  101  | Above maximum               |  Invalid Score      | Invalid Score     |  PASS  |

-----------------------------------------------------------------------------------------------------------------------------------------

**Testing Reflection:**

*1. Why is it important to test the values 0 and 100?*
  - Because these two numbers are the minimum and maximum valid scores.

*2. Why did you also test -1 and 101?*
  - Because these two numbers exceed the minimum and maximum scores.

*3. Which test helped you understand boundary conditions the most?*
  - All of them equally helped me understand boundaries but if I have to choose, the below minimum boundary.

*4. Did any of your tests initially fail? If yes, what did you change in your program?*
  - No.

-----------------------------------------------------------------------------------------------------------------------------------------

**Reflection**

- Selection structures such as 'IF', 'ELSE', and 'ELIF', help this program a ton with making it shorter and way simpler to understand. But to know which part needs which selection structure is needed in each line, proper comments are a great thing to add, as well as making the code way easier to understand. Making a flowchart and a pseudocode before the actual code is great for understanding the code, basically serving as its baseline.
