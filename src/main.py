# a central function to control order of execution
def main():
    name = name()
    age = age()
    gender = gender()
    weight = weight()
    height = height()

# take name inpout and avoid blank entry
def name():
    name = input("Please enter your name : ")
    while name == (""):
        print("please enter your name this field cannot be blank")
        name = input("Please enter your name : ")
    print("Hello and welcome to your calorie calculator, " + name) 
   
name()

# take age input and prevent invalid age
def age(): 
    age = int(input("Please enter your age: "))
    while age < 0 or age > 100:
        age = int(input("Invalid input. Please enter your correct age: "))
    else:
        return age
    

age() 

# take user gender
def gender():
    genders = ["male", "female", "m", "f"]
    while True:
        gender = (input("Please enter your gender: ").lower())
        while gender not in genders:
            gender = input("Please enter either 'Male' or 'Female': ").lower()
        else:
            return gender
            break

gender()



