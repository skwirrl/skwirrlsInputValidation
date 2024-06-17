import re
from typing import Union


def determine_prompt(minimum: int = None, maximum: int = None) -> str:
    if minimum and maximum:
        prompt_text = (f"Please enter a number between"
                       f" {minimum} and {maximum}")
    elif minimum:
        prompt_text = f"Please enter a number greater than {minimum}"
    elif maximum:
        prompt_text = f"Please enter a number less than {maximum}"
    else:
        prompt_text = "Please enter a number"
    return prompt_text


def int_or_float(user_input: str) -> Union[int, float, None]:
    if re.match(r"^[+-]?\d+$", user_input):
        return int(user_input)
    elif re.match(r"^[+-]?(\d*\.\d*|\.\d+)([eE][+-]?\d+)?$", user_input):
        return float(user_input)
    else:
        return None


def min_max_check(number, minimum, maximum) -> str:
    if minimum is None and maximum is None:
        return "valid"
    elif minimum is None:
        return "valid" if number <= maximum else "invalid"
    elif maximum is None:
        return "valid" if number >= minimum else "invalid"
    return "valid" if minimum <= number <= maximum else "invalid"


def get_numeric_input(minimum: int = None,
                      maximum: int = None,
                      optional_prompt: str = None) -> Union[int, float]:
    if optional_prompt:
        prompt_text = optional_prompt
    else:
        prompt_text = determine_prompt(minimum, maximum)
    while True:
        number = input(prompt_text)
        number = int_or_float(number)
        if number is None:
            print("Please enter a valid number!")
            continue
        match min_max_check(number, minimum, maximum):
            case "invalid":
                print("Please enter a valid number!")
                continue
            case "valid":
                return number
