# # Create a variable called 'name' that holds a string
# name = "tommy"

# # Create a variable called 'country' that holds a string
# country = "Merica"

# # Create a variable called 'age' that holds an integer
# age = 37

# # Create a variable called 'hourly_wage' that holds an integer
# hourly_wage = 95

# # Calculate the daily wage for the user
# daily_wage = 8 * hourly_wage

# # Create a variable called 'satisfied' that holds a boolean
# satisfied = True

# # Print out "Hello <name>!"
# print("Hello " + name + "!")

# # Print out what country the user entered
# print(country)

# # Print out the user's age
# print(age)

# # With an f-string, print out the daily wage that was calculated
# print(f"Your daily wage is: {daily_wage}")

# # With an f-string, print out whether the users were satisfied
# print(f"Are you happy? {satisfied}")

# nums = [1, 2, 3, 4, 5]

# for num in nums:
#     for letter in "abc":
#         print(num, letter)
    
for fizzbuzz in range(51):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz) 

    