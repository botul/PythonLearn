user_input = "1,2,3,4,5,6"
user_numbers = user_input.split(",")
print(user_numbers)
user_numbers_int = []
for number in user_numbers:
    user_numbers_int.append(int(number))
print(user_numbers_int)

