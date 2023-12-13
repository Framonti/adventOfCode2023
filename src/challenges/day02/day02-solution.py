from utils import read_input_removing_new_line, extract_and_convert_digit_from_string

raw_game_input = read_input_removing_new_line('input.txt')


def convert_to_dict(rolls: str):
    result = dict()
    roll_per_color = rolls.split(', ')
    for roll in roll_per_color:
        number = extract_and_convert_digit_from_string(roll)
        color = roll.split(' ')[1]
        result[color] = number
    return result


def parse_input(raw_game: str):
    rolls = raw_game.split(": ")[1]
    rolls = rolls.split('; ')

    return [convert_to_dict(roll) for roll in rolls]


games = [parse_input(raw_game) for raw_game in raw_game_input]

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

possible_games_ids = list(range(1, len(games) + 1))
for i, game in enumerate(games):
    for roll in game:
        if roll.get('red', 0) > MAX_RED or roll.get('blue', 0) > MAX_BLUE or roll.get('green', 0) > MAX_GREEN:
            possible_games_ids.remove(i + 1)
            break

first_part_solution = sum(possible_games_ids)

print(first_part_solution)


def compute_power(game: list):
    highest_green = sorted(game, key=lambda roll: roll.get('green', 0), reverse=True)[0].get('green', 0)
    highest_red = sorted(game, key=lambda roll: roll.get('red', 0), reverse=True)[0].get('red', 0)
    highest_blue = sorted(game, key=lambda roll: roll.get('blue', 0), reverse=True)[0].get('blue', 0)

    return highest_green * highest_red * highest_blue


powers = [compute_power(game) for game in games]

second_solution = sum(powers)

print(second_solution)
