# User can pick 6 numbers
# Lottery calculates 6 random numbers between 1 and 20
# Then we match the user numbers to the lottery numbers
# Calculate the winnings based on how many numbers the user matched
import random

def menu():
    #Ask player for the numbers
    #Calculate lottery numbers
    # Print out the winnings
    user_numbers = get_player_numbers()
    lottery_numbers = create_lottery_numbers()
    matched_numbers = user_numbers.intersection(lottery_numbers)
    print("You matched {}. You won ${}! 100$ for every matched number!".format(matched_numbers, 100 * len(matched_numbers)))
def get_player_numbers():
    numbers_csv = input("Please enter 6 numbers from 1 to 20, separated by commas: ")
    #create a set of integers:
    numbers_list = numbers_csv.split(",")
    numbers_set_int = {int(number) for number in numbers_list}
    print(numbers_set_int)
    return numbers_set_int

def create_lottery_numbers():
    values = set() #Defining empty set - cannot use brackets {}
    #for index in range(6):
    while len(values) < 6:
        values.add(random.randint(1, 20))
    print(values)
    return values


#get_player_numbers()
#create_lottery_numbers()

menu()

