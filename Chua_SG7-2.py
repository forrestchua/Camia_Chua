# 2. Grade Checker
    # Validation Technique: Range Validation

grade = int(input("Enter your grade: "))

if 0 <= grade <= 100:
    print("Valid Grade")
else:
    print("Invalid Grade. Grade must be between 0 and 100")
