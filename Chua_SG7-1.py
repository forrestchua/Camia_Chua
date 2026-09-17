# 1. Payment Method Checker
   # - Validation Technique : Acceptable Value Validation

valid_payment = ["Gcash", "Cash", "Card"]

Payment = input("Enter desired payment method: ")

if Payment in valid_payment:
    print("Valid payment method")
else:
    print("Invalid payment method")