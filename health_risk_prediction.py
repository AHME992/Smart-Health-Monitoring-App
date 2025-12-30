number_of_users = int(input("Enter number of users: "))

for i in range(number_of_users):
    blood_sugar_level = int(input("Enter blood sugar level: "))

    if blood_sugar_level > 180:
        print("Diabetes Risk Alert")
    else:
        print("No Risk Detected")
