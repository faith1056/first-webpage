prices = [100, 250, 80, 300, 150]
price = list(map(lambda price: "Expensive" if price >= 200 else "Affordable", prices))
print(price)

ages = [12, 18, 21, 15, 30, 65]
minor_adult = list(map(lambda age : "Adult" if age >= 18 else "Minor", ages))
print(minor_adult)

scores = [45, 72, 90, 33, 60, 28]
pass_failed = list(map(lambda scores: "Pass" if scores >= 50 else "Fail",scores))
print(pass_failed)


scores = [35, 55, 75, 90, 45, 68]
results = list(map(
    lambda score : "Exellent" if score >= 70 else "pass" if  score >= 50 else "Fail",scores))
print(results)
