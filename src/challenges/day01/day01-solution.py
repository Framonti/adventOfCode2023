from utils import read_input_removing_new_line

raw_calibration_values = read_input_removing_new_line("input.txt")

only_digits = [[int(char) for char in raw_calibration_value if char.isdigit()] for raw_calibration_value in
               raw_calibration_values]


def get_first_and_last(calibration: list):
    first = calibration[0]
    last = calibration[-1]
    return int(f'{first}{last}')


calibration_values = [get_first_and_last(calibration) for calibration in only_digits]

first_solution = sum(calibration_values)

print(first_solution)

numbers_to_words = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def extract_digit(raw_calibration: str):
    result = []

    for i, char in enumerate(raw_calibration):
        if char.isdigit():
            result.append(int(char))
        else:
            possible_number_3 = raw_calibration[i: i+3]
            possible_number_4 = raw_calibration[i: i+4]
            possible_number_5 = raw_calibration[i: i+5]
            if possible_number_3 in numbers_to_words:
                result.append(numbers_to_words[possible_number_3])
            elif possible_number_4 in numbers_to_words:
                result.append(numbers_to_words[possible_number_4])
            elif possible_number_5 in numbers_to_words:
                result.append(numbers_to_words[possible_number_5])
    return result


only_digits = [extract_digit(raw_calibration_value) for raw_calibration_value in raw_calibration_values]

calibration_values = [get_first_and_last(calibration) for calibration in only_digits]

second_solution = sum(calibration_values)

print(second_solution)
