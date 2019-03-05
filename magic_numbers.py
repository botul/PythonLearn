import random

magic_numbers = [random.randint(0,9), random.randint(0,9)]

def ask_user():
    user_number = int(input("Enter a number between 0 and 9: "))
    if user_number in magic_numbers:
        return "You got the number right!"
    if user_number not in magic_numbers:
        return "You didn't quite get it."

def run_program_x_times(chances):
    for attempt in range(chances):
        print("This is attempt {} ".format(attempt))
        print(ask_user())

user_attempts = int(input("Enter the number of attempts: "))
run_program_x_times(user_attempts)
