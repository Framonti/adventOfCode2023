import math
from typing import List

from utils import read_input_removing_new_line

raw_part_scheme = read_input_removing_new_line('input.txt')

scheme = {'symbols': [], 'part_numbers': []}


class Part:
    def __init__(self, part_number, coordinates: List[complex]):
        self.part_number = part_number
        self.coordinates = coordinates


def extract_scheme_info_per_row(row: str, row_index):
    for i, char in enumerate(row):
        if char == '.':
            continue
        if char.isdigit():
            if i > 0:
                look_behind = row[i - 1]
                if look_behind.isdigit():
                    continue
            coordinates = [complex(i, -row_index)]
            part_number = char

            look_ahead_1 = row[i + 1]
            if look_ahead_1.isdigit():
                coordinates.append(complex(i + 1, -row_index))
                part_number += look_ahead_1

            if i < len(row) + 2:
                look_ahead_2 = row[i + 2]
                if look_ahead_2.isdigit():
                    coordinates.append(complex(i + 2, -row_index))
                    part_number += look_ahead_2

            scheme['part_numbers'].append(Part(int(part_number), coordinates))
        else:
            scheme['symbols'].append((char, complex(i, -row_index)))


[extract_scheme_info_per_row(row, i) for i, row in enumerate(raw_part_scheme)]


def has_adjacent_symbol(part: Part):
    for coordinate in part.coordinates:
        for symbol in scheme['symbols']:
            if abs(coordinate - symbol[1]) < 2:
                return True


relevant_parts = [part.part_number for part in scheme['part_numbers'] if has_adjacent_symbol(part)]

first_solution = sum(relevant_parts)

print(first_solution)


def retrieve_adjacent_parts(gear_coordinate):
    adjacent_parts = []
    for part in scheme['part_numbers']:
        for coordinate in part.coordinates:
            if abs(coordinate - gear_coordinate) < 2:
                adjacent_parts.append(part)
                break
    return adjacent_parts


gears_ratios = [math.prod
                ([part.part_number for part in retrieve_adjacent_parts(symbol[1])])
                for symbol in scheme['symbols']
                if symbol[0] == '*' and len(retrieve_adjacent_parts(symbol[1])) == 2
                ]

second_solution = sum(gears_ratios)

print(second_solution)
