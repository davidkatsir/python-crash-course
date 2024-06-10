# age = int(input("What is your age: "))
#
# if age >= 67:
#     print("You're above 67")
#
# if age >= 18:
#     print("You're adult!")
# elif age == 18:
#     print("You're 18 years old!")
# else:
#     print("You're too young...")
#
# print("The app run was finished")


age = float(input("Please enter your age (0 to 120): "))
print("'age' id in the Hard Disk's memory is: " + str(id(age)))
while age < 0 or age > 120:
    age = float(input("Please enter a valid age between 0 and 120: "))
    print("'age' id in the Hard Disk's memory is: " + str(id(age)))
if age >= 0 and age <= 18:
    print("You are a minor.")
    print("'age' id in the Hard Disk's memory is: " + str(id(age)))
elif age > 18 and age <= 65:
    print("You are an Adult.")
    print("'age' id in the Hard Disk's memory is: " + str(id(age)))
else:
    print("You are a pensioner")
    print("'age' id in the Hard Disk's memory is: " + str(id(age)))
