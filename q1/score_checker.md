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
