age = int(input("Enter your age"))
if age < 2:
    print("BABY")
elif age >= 2 and age <= 3:
    print("Toddler")
elif age >= 4 and age <= 12:
    print("kid")
elif age >= 13 and age <= 19:
    print("Teenager")
elif age >= 20 and age <= 64:
    print("Adult")
else: 
    age >= 65
    print("Elder")



