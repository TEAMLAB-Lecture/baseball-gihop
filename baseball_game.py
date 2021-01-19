# -*- coding: utf-8 -*-

import random


def get_random_number():
    # Helper Function - 지우지 말 것
    # 100부터 999까지 수를 램덤하게 반환함
    return random.randrange(100, 1000)


def is_digit(user_input_number):
    for char in user_input_number:
        if not char.isdigit():
            return False
    return True


def is_between_100_and_999(user_input_number):
    return int(user_input_number) >= 100 and int(user_input_number) <= 999


def is_duplicated_number(three_digit):
    for digit in str(three_digit):
        if str(three_digit).count(digit) > 1: return True
    return False


def is_validated_number(user_input_number):
    return is_digit(user_input_number) and is_between_100_and_999(user_input_number) and not is_duplicated_number(user_input_number)


def get_not_duplicated_three_digit_number():
    while True:
        numbers = str(get_random_number())
        is_not_duplicated_number = True
        for number in numbers:
            if(numbers.count(number) > 1):
                is_not_duplicated_number = False
                break
        if(is_not_duplicated_number): break
    return int(numbers)


def get_strikes_or_ball(user_input_number, random_number):
    strikes = 0
    ball = 0
    for digit in user_input_number:
        if random_number.count(digit) > 0:
            if random_number.find(digit) == user_input_number.find(digit):
                strikes += 1
            else:
                ball += 1
    return [strikes, ball]


def is_yes(one_more_input):
    return one_more_input.lower() in ('yes', 'y')


def is_no(one_more_input):
    return one_more_input.lower() in ('no', 'n')
    

def is_zero(user_input):
    return user_input == '0' or user_input == 0
    

def main():
    print("Play Baseball")
    user_input = 999
    random_number = str(get_not_duplicated_three_digit_number())
    print("Random Number is : ", random_number)
    while True:
        user_input = input('Input guess number is : ')
        if is_zero(user_input): break

        if not is_validated_number(user_input): 
            print('Wrong Input, Input again')
            continue

        strikes, ball = get_strikes_or_ball(user_input, random_number)
        print(f'Strikes : {strikes} , Balls : {ball}')

        if strikes == 3:
            while True:
                user_input = input('You win, one more(Y/N) ?')
                if is_no(user_input) or is_yes(user_input) or is_zero(user_input): break
                print('Wrong Input, Input again')
            
        if is_zero(user_input) or is_no(user_input): break
        elif is_yes(user_input): 
            random_number = str(get_not_duplicated_three_digit_number())
            print("Random Number is : ", random_number)

    print("Thank you for using this program")
    print("End of the Game")

if __name__ == "__main__":
    main()
