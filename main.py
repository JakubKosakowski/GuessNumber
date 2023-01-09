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


