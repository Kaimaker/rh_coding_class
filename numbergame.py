import random
import argparse

parser = argparse.ArgumentParser(
                    prog='numbergame',
                    description='a game that guesses the number',
                    epilog='created by <KAIUS>')
parser.add_argument('--max_number', type=int, help='the max number')

def get_number_from_user():
 number = int(input("Please enter a number: "))
 return number

def create_number(max_number):
   return random.randint(1, max_number)

def define_difference(user_number,created_number):
    return abs(user_number - created_number)

def display_results(user_number,created_number,difference):
    if  user_number == created_number:
        print("you are correct good job")

    print(f"The number you entered is: {user_number}")
    print(f"The created number is: {created_number}")
    print(f"The difference is: {difference}")

if __name__ == '__main__':
    args = parser.parse_args()
    user_number = get_number_from_user()
    created_number = create_number(args.max_number)
    difference = define_difference(user_number,created_number)
    if difference == 0:
        display_results(user_number,created_number,difference)
    else:
        for retry in range(3):
            if user_number > created_number:
                print("You were too high")
            else:
                print("You were too low")
            user_number = get_number_from_user()
            difference = define_difference(user_number, created_number)
            if difference == 0:
                display_results(user_number,created_number,difference)
                break