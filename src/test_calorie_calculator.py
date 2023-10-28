import calorie_calculator


# Test get_age() function
def test_get_age_valid_input():
    # Test valid age input
    assert calorie_calculator.get_age() == 25


# Test invalid age input (non-numeric)
def test_get_age_invalid_input():
    assert calorie_calculator.get_age() == 0


# Test get_gender() function
def test_get_gender_valid_input():
    # Test valid gender input
    assert calorie_calculator.get_gender() == "male"


# Test invalid gender input
def test_get_gender_invalid_input():
    assert calorie_calculator.get_gender() == "unknown"


# Test calculate_bmr() function
def test_calculate_bmr():
    # Test BMR calculation for a known input
    assert calorie_calculator.calculate_bmr(30, "female", 70, 160) == 1350


# Test get_activity_level() function
def test_get_activity_level_valid_input():
    # Test valid activity level input
    assert calorie_calculator.get_activity_level() == "sedentary"


def test_get_activity_level_invalid_input():
    # Test invalid activity level input
    assert calorie_calculator.get_activity_level() == "unknown"


# Test calculate_maintenance_calories() function
def test_calculate_maintenance_calories():
    # Test maintenance calories calculation
    assert calorie_calculator.calculate_maintenance_calories(
        1500, "lightly active") == 2062


# Test case for get_goals() function
def test_get_goals():
    # Test goal calculation
    assert calorie_calculator.get_goals(2000) == 1500  # Weight loss goal
    assert calorie_calculator.get_goals(2000) == 2500  # Muscle gain goal
    assert calorie_calculator.get_goals(2000) == 2000  # Maintain goal


# Test for write_to_file() function (requires file system interaction)
def test_write_to_file(tmp_path):
    user_name = "John"
    user_bmr = 1500
    maintenance_calories = 2000
    user_goal = 1800

    file_path = tmp_path / "test_output.txt"
    calorie_calculator.write_to_file(
        user_name, user_bmr, maintenance_calories, user_goal, file_path)

    assert file_path.is_file()
    with open(file_path, "r") as file:
        content = file.read()
        assert "User Name: John" in content
        assert "Basal Metabolic Rate (BMR): 1500" in content
        assert "Maintenance Calories: 2000" in content
        assert "User Goal: 1800" in content
