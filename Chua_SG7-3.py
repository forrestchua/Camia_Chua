# 3. Student ID Checker
    # Validation Technique: Pattern Validation

import re

student_ID = input("Enter Student ID: ")

pattern = r"\d{4}-\d{4}"

if re.match(pattern, student_ID):
    print("Valid Student ID")
else:
    print("Invalid Student ID")