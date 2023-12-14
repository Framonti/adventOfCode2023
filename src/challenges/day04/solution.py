from utils import read_input_remove_incipit

raw_card_input = read_input_remove_incipit('input.txt', ': ')

cards = [raw_card.replace('  ', ' ') for raw_card in raw_card_input]
cards = [raw_card if not raw_card.startswith(' ') else raw_card[1:] for raw_card in cards]
cards = [tuple(card.split(' | ')) for card in cards]
cards = [([int(number) for number in card[0].split(' ')], [int(number) for number in card[1].split(' ')])
         for card in cards]

winning_counts = [len(set(card[0]).intersection(set(card[1]))) for card in cards]
winning_points = [2 ** (winning_count - 1) if winning_count > 0 else 0 for winning_count in winning_counts]

first_solution = sum(winning_points)

print(first_solution)

card_count = {i: 1 for i in range(len(cards))}

for i, winning_count in enumerate(winning_counts):
    for j in range(1, winning_count + 1):
        card_count[i + j] += card_count[i]

second_solution = sum(card_count.values())

print(second_solution)
