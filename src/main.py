#create a class to control each input variable
class User:
    def __init__(self, name, age, gender, height, weight, activity_level):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight
        self.activity_level = activity_level
   

#create a function using class objects to control each input
def user_input(User):
    while True:
        try:
            name = (input("Please enter your age: "))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        else:
            break  

user_input(User)
