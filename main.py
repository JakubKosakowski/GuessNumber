import random
"""
Check, if the number is bigger or lesser than generated number.

Parameters:
val (int), check (int): Compared numbers

Returns:
str: Returning information
"""


def check_number(val:int, check:int) -> str:
    if val > check:
        return "To big!"
    elif val < check:
        return "To small!"
    return "You win!"


if __name__ == "__main__":
    generated_number = random.randint(1,100)
    while True:
        try:
            player_number = int(input("Guess the number between 1 to 100: "))
        except ValueError:
            print("It's not a number!")
            continue
        except KeyboardInterrupt:
            print("Data entry was interrupted!")



