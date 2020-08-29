# WHILE LOOPS EXERCISES

# Enter a random string in the variable string_1, then enter a character and save it in the variable char_1.
# Write code, which will count how many times your character is included in your string.
# Save result to result_1 variable

string_1 = 'My dog\'s name is Mishka'
char_1 = 's'
result_1 = 0
i = 0

while i < len(string_1):
    if (string_1[i]) == char_1:
        result_1 += 1
    i = i + 1



# Enter a random number and save it in variable number_1. Then create code to multiply all the digits together
# and save result in the result_2 variable.

number_1 = 15622
string_number_1 = str(number_1)
result_2 = 1
ind = 0

while ind < len(string_number_1):
    result_2 *= int(string_number_1[ind])
    ind += 1
print(result_2)

# Enter a random number and save it in variable number_2. Then create code which will return
# a number with digits of number_1 in reverse order. Save it in result_3 variable

number_2 = 987
string_number_2 = str(number_2)
index = len(string_number_2) - 1
result_3 = ''

while index >= 0:
    result_3 += string_number_2[index]
    index = index - 1
print(result_3)
