# FOR LOOPS EXERCISES

# Ex. 1
# Enter your name, save it in name variable and save in result_1 variable your name repeated 3 times (use loops)

name_1 = 'Ekaterina'
result_1 = None

# TODO: Here is your code
for letter in name_1:
    result_1 = name_1 + name_1 + name_1


# Ex. 2
# Modify your previous program so that it will enter your name (save it in variable  name_2) and a number
# (save in variable number) and then save in result_2 variable your name repeated as many times as number_1 is
# (use loops)
name_2 = "Ekaterina"
number_1 = 5
result_2 = None

# TODO: Here is your code
for char in name_2:
    result_2 = name_2 * number_1



# Ex. 3
# Enter a random string, which includes only digits. Write code which find a sum of digits in this string and save it
# into result_3 variable

string_number_1 = '6789'
result_3 = 0

# TODO: Here is your code
for digit in string_number_1:
    result_3 += int(digit)


# Ex. 4
# Create code which sums up all even numbers between 2 and 100 (include 100) and save it in result_4 variable

result_4 = 0

# TODO: Here is your code

for number in range(2,101,2):
    result_4 += number