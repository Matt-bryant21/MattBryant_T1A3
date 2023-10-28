# Matt Bryant T1A3  
[Source File Repo](https://github.com/Matt-bryant21/MattBryant_T1A3)

[Linear Project Management (requires login)](https://linear.app/matt-bryant-projects/project/t1a3-bbd4018b93c7)

## Referenced Materials
https://peps.python.org/pep-0008/

https://www.guru99.com/reading-and-writing-files-in-python.html

https://flake8.pycqa.org/en/latest/

https://www.forbes.com/health/body/bmr-calculator/

## Code Style Guide
PEP8 was the styleguide used to write the code and ensure it adheres to best practices. Features of PEP8 include:

- 4 spaces per indentation level
- Maximum line length of 72 characters
- Surrounding top level function and class definitions with two blank lines
- UTF-8 source file encoding
- Separate line imports

To ensure code adhered to these guidlines, various packages were used including [Flake8](https://flake8.pycqa.org/en/latest/), [Autopep8](https://pypi.org/project/autopep8/), and [Ruff](https://github.com/astral-sh/ruff)

![Flake8](./docs/flake8.JPG)

![Autopep8](./docs/autopep8.JPG)

![Ruff](./docs/ruff.JPG)

## Features
### Feature 1: Taking User Input
The first and main feature in the app relied on taking several pieces of information from the user including; 

- name 
- age
- gender
- height
- weight
- activity level
- fitness goal (lose weight, build muscle, maintain weight)

Implementing these were fairly simple building each function into an input that ran a while loop to prevent invalid inputs as either str, int, or float. Initially the plan was to use global variables but after some research it was obvious that return functions were a more efficient way to acheive passing inputs to latter functions. All the str functions were ran with strip() and lower() methods to keep inputs from raising errors. Int functions were controlled with Try and Except methods to prevent invalid inputs.


### Feature 2: Calculating User BMR, Maintenance, Deficit, Surplus Calories then showing an example meal breakdown
Once the user inputs were gathered and stored under the correct variables, a series of calculations were made to output BMR, maintenance calories, and an updated amount based on user goals. This process started with calculating the BMR (Basal Metabolic Rate aka how many calories the body burns on its own per day). With the BMR calculation I was able to calculate the maintenance calories and ask the user what their goals were:

- Lose weight - This meant deducting 500 calories from their mantenance amount
- Build muscle - This meant adding 500 calories to their maintenance amount
- Maintain weight - This just repeated maintenance calories


### Feature 3: Outputting info to a text file
With all the correct information and calculations completed, the next step was to output all the info to a text file. 
This was started with a file open and write function;

    with open("calorie_info.txt", "w") as file:

Then each consecutive info line was written to include the desired variable;

    file.write("User Name: {}\n".format(user_name))
        file.write("Basal Metabolic Rate (BMR): {}\n".format(user_bmr))
        file.write("Maintenance Calories: {}\n".format(maintenance_calories))
        file.write("User Goal: {}\n".format(user_goal))

As the meal plan / calorie categories were done last, the file write for that was done seperately, it also required a slightly more complex code using multipliers to acheive the correct ratios based on the users goal. 

     file.write("\nCalorie Distribution for the Day:\n")
        for meal, calories in meal_calories.items():
            file.write(f"{meal.capitalize()}: {calories} calories\n")


## Implementation Plan

Implementing the user input features was fairly straight forward aside from the later refactoring that occured. Taking each user input could be running under the same format as taking input and then running a while loop to prevent invalid input, the inputs that required integers (or floats) were run with Try: Except: blocks to do the same error handling. 

In terms of priority, each input held the same importance in building the foundational blocks of the code, having said that, the height and weight were crucial to get correct as they held the most influence in the result of the program. The checklist of features to implement were the following;

- Take user name
- Take user age
- Take user gender
- Take user height
- Take user weight

The deadline for this section was determinded to be Oct 26th, which was accurately acheived.

#### Feature 2:
Implementation of the next sections relied on calculating the BMR of the user, from this point the next caculations followed closely. Calculating the BMR required the variables from input functions to be used which led to refactoring after the intial code was written. Initially it was planned to use global variables to link inputs but after realising this was bad practice, the code was changed to return function data instead of the original approach. Calculating the BMR held the most priority. The aim was to get this section finished by 26th Oct.

The checklist of features to be implemented were the following;

- Calculate BMR based on user input
- Calculate maintenance calories based on BMR
- Calculate deficit calories
- Calculate surplus calories
- Display goal with intended calories
- Show sample meal plan in calorie division

#### Feature 3:
Implementation of this section was quite simple compared to previous sections, it consisted of writing the write to file function and then assigning the necessary variables to each line of the text output. This section was on the lower priority tier on the timeline but had the same deadline as the rest of the code as 26th Oct.   

Checklist of features were as follows;

- Output summary of goals and calculations
- Output sample meal schedule
- Output Calories per meal breakdown


### - Project management screenshots
Linear was used as project manager for this assessment, see top link for direct link (requires login though)

![project timeline](./docs/project%20overview.JPG)

![project overview](./docs/whole%20project.JPG)

![feature1](./docs/feature%201%20checklist.JPG)

![feature2](./docs/feature%202%20checklist.JPG)

![feature3](./docs/Feature%203.JPG)

## Help Documentation

### System Requirements

This application requires Python3. If you need to install Python3 you can follow the guide [here](https://wiki.python.org/moin/BeginnersGuide/Download) according to your operating system. This application also requires [PIP](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/). The virtual environment VENV comes standard with Python.

### Required Dependencies

- [Colorama](https://pypi.org/project/colorama/)

### Installation Process

Locate src directory path of application in terminal e.g

    mattbryant@DESKTOP-81AD98Q:~/MattBryant_T1A3/src$

The bash script should already be enabled with executable rights but if not:

    chmod +x run_calculator.sh

Now the run_calculator.sh script can be run:

    ./run_calculator.sh

To use the application; simply enter your information in the input provided. All information inputs are mandatory so you will need to know each of them prior to using the application.