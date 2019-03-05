numbers = set()
numbers.add(3)
numbers.add(3)
numbers.add(4)
print(numbers)
lottery_values = {3, 5, 17, 6}
user_values = {3, 5, 11, 2}
winning = user_values.intersection(lottery_values)
print(winning)
