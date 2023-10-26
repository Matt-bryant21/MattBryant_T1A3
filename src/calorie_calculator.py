#take user name
def get_name():
    while True:
        user_name = input("Please enter your name: ").strip()
        if user_name:
            return user_name
        print("Please enter your name; this field cannot be blank.")

# take user age
def get_age():
    while True:
        try:
            user_age = int(input("Please enter your age: "))
            if 0 <= user_age <= 100:
                return user_age
            print("Invalid age. Please enter a valid age (0-100).")
        except ValueError:
            print("Invalid input. Please enter a numeric age.")
# take user gender
def get_gender():
    genders = ["male", "female", "m", "f"]
    while True:
        user_gender = input("Please enter your gender: ").strip().lower()
        if user_gender in genders:
            return user_gender
        print("Please enter either 'Male' or 'Female'.")

# take user weight
def get_weight():
    while True:
        try:
            user_weight = float(input("Please enter your weight in kilograms: "))
            if 0 < user_weight <= 130:
                return user_weight
            print("Invalid weight. Please enter a valid weight (0-130 kg).")
        except ValueError:
            print("Invalid input. Please enter a numeric weight.")
# take user height
def get_height():
    while True:
        try:
            user_height = float(input("Please enter your height in centimeters: "))
            if 0 < user_height <= 250:
                return user_height
            print("Invalid height. Please enter a valid height (0-250 cm).")
        except ValueError:
            print("Invalid input. Please enter a numeric height.")

# calculate bmr for either male or female
def calculate_bmr(user_age, user_gender, user_weight, user_height):
    if user_gender == "male":
        male_bmr = 66 + (13.7 * user_weight) + (5 * user_height) - (6.8 * user_age)
        return male_bmr
    elif user_gender == "female":
        female_bmr = 655 + (9.6 * user_weight) + (1.8 * user_height) - (4.7 * user_age)
        return female_bmr
    else:
        raise ValueError("Invalid gender.")

# take user activity level
def get_activity_level():
    activity_levels = ["sedentary", "lightly active", "moderately active", "very active", "extra active"]
    while True:
        user_activity_level = input("Please enter your activity level (sedentary, lightly active, moderately active, very active, extra active): ").strip().lower()
        if user_activity_level in activity_levels:
            return user_activity_level
        print("Please enter a valid activity level.")

# calculate user maintenance calories
def calculate_maintenance_calories(bmr, user_activity_level):
    activity_multipliers = {
        "sedentary": 1.2,
        "lightly active": 1.375,
        "moderately active": 1.55,
        "very active": 1.725,
        "extra active": 1.9
    }
    if user_activity_level in activity_multipliers:
        multiplier = activity_multipliers[user_activity_level]
        maintenance_calories = round(bmr * multiplier)
        return maintenance_calories
    else:
        raise ValueError("Invalid activity level.")

# take user goals and calculate new caloric intake
def get_goals(maintenance_calories):
    while True:
        user_goal = input("What are your current goals? (lose weight, build muscle, maintain): ").strip().lower()
        if user_goal in ["lose weight", "build muscle", "maintain"]:
            if user_goal == "lose weight":
                return "Lose Weight - {} calories".format(maintenance_calories - 500)
            elif user_goal == "build muscle":
                return "Build Muscle - {} calories".format(maintenance_calories + 500)
            else:
                return "Maintain - {} calories".format(maintenance_calories)
        print("Please enter a valid goal (lose weight, build muscle, maintain).")

# writing info to file
def write_to_file(user_name, user_bmr, maintenance_calories, user_goal):
    with open("calorie_info.txt", "w") as file:
        file.write("User Name: {}\n".format(user_name))
        file.write("Basal Metabolic Rate (BMR): {}\n".format(user_bmr))
        file.write("Maintenance Calories: {}\n".format(maintenance_calories))
        file.write("User Goal: {}\n".format(user_goal))


# main function for order of operations
def main():
    user_name = get_name()
    user_age = get_age()
    user_gender = get_gender()
    user_weight = get_weight()
    user_height = get_height()
    user_bmr = calculate_bmr(user_age, user_gender, user_weight, user_height)
    user_activity_level = get_activity_level()
    maintenance_calories = calculate_maintenance_calories(user_bmr, user_activity_level)
    user_goal = get_goals(maintenance_calories)

    print(f"Hello and welcome to your calorie calculator, {user_name}!")
    print(f"Your basal metabolic rate (BMR) is: {user_bmr}")
    print(f"To maintain your current weight, you should be consuming {maintenance_calories} calories per day.")
    print(f"Your goal is to consume {user_goal} calories per day.")

    # Write information to a text file
    write_to_file(user_name, user_bmr, maintenance_calories, user_goal)
    print("Information written to 'calorie_info.txt'.")
    print("You can find this file in the /src directory of this program :)")

if __name__ == "__main__":
    main()
