# a central function to control order of execution
# def main():
#     name = name()
#     age = age()
#     gender = gender()
#     weight = weight()
#     height = height()
#     bmr = bmr()

# take name input and avoid blank entry
def name():
    user_name = input("Please enter your name : ")
    while user_name == (""):
        print("please enter your name this field cannot be blank")
        user_name = input("Please enter your name : ")
    print("Hello and welcome to your calorie calculator, " + user_name) 
   
name()

# take age input and prevent invalid age
def age(): 
    global user_age
    user_age = int(input("Please enter your age: "))
    while user_age < 0 or user_age > 100:
        user_age = int(input("Invalid input. Please enter your correct age: "))
    else:
        return user_age
    

age() 

# take user gender
def gender():
    global user_gender
    genders = ["male", "female", "m", "f"]
    while True:
        user_gender = (input("Please enter your gender: ").lower())
        while user_gender not in genders:
            user_gender = input("Please enter either 'Male' or 'Female': ").lower()
        else:
            return user_gender
            break

gender()

# get user weight
def weight():
    global user_weight
    user_weight = int(input("Please enter your weight in kilograms: "))
    while user_weight <= 0:
        user_weight = int(input("Invalid input. Please enter your weight in kilograms: "))
    else:
        return user_weight

weight()

# get user height
def height():
    global user_height
    user_height = int(input("Please enter your height in centimeters: "))
    while user_height <= 0 or user_height > 250:
        user_height = int(input("Invalid input. Please enter your height in centimeters: "))
    else:
        return user_height

height()


def bmr():
    global male_bmr
    global female_bmr
    male_bmr = 66 + (13.7 * user_weight) + (1.8 * user_height) - (4.7 * user_age)
    female_bmr = 655 + (13.7 * user_weight) + (5 * user_height) - (6.8 * user_age)
    if user_gender == 'male':
        print("Your basal metabolic rate is: " + str(male_bmr))
    else:
        print("Your basal metabolic rate is: " + str(female_bmr))
    
bmr()

def activity_level():
    global user_activity_level
    user_activity_level = input("Please enter your activity level (sedentary, lightly active, moderately active, very active, extra active) ").lower()
    while user_activity_level == (""):
        print("please enter your activity level, this field cannot be blank")
        user_activity_level = input("Please enter your activity level (sedentary, lightly active, moderately active, very active, extra active) ").lower()

activity_level()

# def goals():
#     global maintenance_calories
#     if user_gender == 'male' and user_activity_level == "sedentary":
#         maintenance_calories = str(male_bmr * 1.2)
#         print("To maintain your current weight, you should to be consuming " + str(maintenance_calories) + " calories per day")
#     elif user_gender == "female" and user_activity_level == "sedentary":
#         maintenance_calories = str(female_bmr * 1.2)
#         print("To maintain your current weight, you should be consuming " + str(maintenance_calories) + " calories per day")
#     elif user_gender == 'male' and user_activity_level == "lightly active":
#         maintenance_calories = str(male_bmr * 1.375)
#         print("To maintain your current weight, you should to be consuming " + str(maintenance_calories) + " calories per day")
#     elif user_gender == "female" and user_activity_level == "lightly active":
#         maintenance_calories = str(female_bmr * 1.375)
#         print("To maintain your current weight, you should be consuming " + str(maintenance_calories) + " calories per day")
#     elif user_gender == 'male' and user_activity_level == "moderately active":
#         maintenance_calories = str(male_bmr * 1.55)
#         print("To maintain your current weight, you should to be consuming " + str(maintenance_calories) + " calories per day")
#     elif user_gender == "female" and user_activity_level == "moderately active":
#         maintenance_calories = str(female_bmr * 1.55)
#         print("To maintain your current weight, you should be consuming " + str(maintenance_calories) + " calories per day")
#     elif user_gender == 'male' and user_activity_level == "very active":
#         maintenance_calories = str(male_bmr * 1.725)
#         print("To maintain your current weight, you should to be consuming " + str(maintenance_calories) + " calories per day")
#     elif user_gender == "female" and user_activity_level == "very active":
#         maintenance_calories = str(female_bmr * 1.725)
#         print("To maintain your current weight, you should be consuming " + str(maintenance_calories) + " calories per day")    
#     elif user_gender == 'male' and user_activity_level == "extra active":
#         maintenance_calories = str(male_bmr * 1.9)
#         print("To maintain your current weight, you should to be consuming " + str(maintenance_calories) + " calories per day")
#     elif user_gender == "female" and user_activity_level == "extra active":
#         maintenance_calories = str(female_bmr * 1.9)
#         print("To maintain your current weight, you should be consuming " + str(maintenance_calories) + " calories per day")
# goals()

def maintenance():
    global maintenance_calories
    multipliers = {
        ('male', 'sedentary'): 1.2,
        ('female', 'sedentary'): 1.2,
        ('male', 'lightly active'): 1.375,
        ('female', 'lightly active'): 1.375,
        ('male', 'moderately active'): 1.55,
        ('female', 'moderately active'): 1.55,
        ('male', 'very active'): 1.725,
        ('female', 'very active'): 1.725,
        ('male', 'extra active'): 1.9,
        ('female', 'extra active'): 1.9
    }

    user_key = (user_gender, user_activity_level)
    if user_key in multipliers:
        multiplier = multipliers[user_key]
        maintenance_calories = str(round(male_bmr if user_gender == 'male' else female_bmr, 2) * multiplier)
        print(f"To maintain your current weight, you should be consuming {maintenance_calories} calories per day")
    else:
        print("Invalid gender or activity level.")

maintenance()

def goals():
    global goals
    goals = input("What are your current goals? (lose weight, build muscle, maintain) ").lower()
    if goals == "lose weight":
        print("You should be consuming" + str(maintenance_calories - 500))
    elif goals == "build muscle":
        print("You should be consuming" + str(maintenance_calories + 500))
    elif goals == "maintain":
        print("keep sticking with" + str(maintenance_calories))
    
goals()
    

