# a central function to control order of execution
# def main():
#     name = name()
#     age = age()
#     gender = gender()
#     weight = weight()
#     height = height()
#     bmr = bmr()

# take name inpout and avoid blank entry
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

def activity_level():
    global user_activity_level
    user_activity_level = input("Please enter your activity level").lower()



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




def goals():
    global user_goals
    print("Your BMR stands for your Basal Metabolic Rate, this is how many calories your body burns on average per day")
    print("To figure out the correct amount of calories consumed we need to understand your goals")
    user_goals = input("Enter your goals (maintain weight, lose weight, increase muscle): ")
    while user_goals == (""):
        print("Please enter your goals, this field cannot be blank")
        user_goals = input("Enter your goals: maintain weight, lose weight, increase muscle")
    
goals()