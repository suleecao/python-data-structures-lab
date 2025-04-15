# Exercise 1: List and Indexing
#
# Create a list named students containing at least three student names (strings).
# Assign the second student’s name to a variable named first_student.
# Assign the last student’s name to a variable named last_student.

def manage_students():
    student_list = ['Alice', 'Bob', 'Charlie']
    first_student = student_list[1]
    last_student = student_list[-1]
    return first_student, last_student
print('Exercise 1:', manage_students())

# Exercise 2: Loop and String Concatenation
#
# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
# Create a variable named meal and assign an empty string to it.
# Use a for loop to iterate over the strings in foods and append each string to meal.

def combine_foods():
    foods = ('sushi', 'brioche', 'pate')
    meal = ''
    for food in foods:
        meal += food + ' '
    return meal.strip() 

print('Exercise 2:', combine_foods())

# Exercise 3: Slicing Tuples
#
# Using the slice operator, assign a new tuple containing only the last two food strings in the foods to a variable named last_two_foods.

def slice_foods():
    foods = ('sushi', 'brioche', 'pate')
    last_two_foods = foods[1:3]
    return last_two_foods
print('Exercise 3:', slice_foods())

#Exercise 4: Hometown dictionary

hometown = {
    "city": "Antwerp",
    "state": "Antwerp",
    "population": 500000,
}

def hometown_info():
    city = hometown["city"]
    state = hometown["state"]
    population = hometown["population"]
    print(f"I was born in {city}, the state is also {state}, with a population of {population}")

print("exercise 4:", hometown_info())

#exercise 5 iterating through a dictionary
hometown_town_items = []
def list_hometown_items():
    for key, value in hometown.items():
        hometown_town_items.append(f"{key}: {value}")
    return hometown_town_items
print("exercise 5:", list_hometown_items())

#exercise 6 list comprehension
list_of_students = ['Alice', 'Bob', 'Charlie', 'David', 'Ergo']
def create_awesome_students():
    awesome_students = [f"{student} is awesome!" for student in list_of_students]
    return awesome_students
print("exercise 6:", create_awesome_students())

# Exercise 7: Filter Foods
#
# Assign to a variable named foods_with_an_a the result of list comprehension that filters the foods tuple to only include food strings that contain the letter 'a'.
# For example, if foods is a tuple of ('Taco', 'Burrito', 'Sandwich'), foods_with_an_a would be a list equal to ['Taco', 'Sandwich']

def filter_foods_with_a():
    foods = ('sushi', 'brioche', 'pate', 'aioli', 'macaroon')
    foods_with_an_a = [food for food in foods if 'a' in food]
    return foods_with_an_a  

print('Exercise 7:', filter_foods_with_a())
