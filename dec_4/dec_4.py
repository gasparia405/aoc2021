#!/usr/bin/env python
import re

def find_winning_card(bingo_card: list, draw_list: list) -> bool:
    """
    If the length of the set of draws minus the set of row or col values is 0,
        the bingo card has bingo and is a winner
    """
    for row in bingo_card:
        if all(number in draw_list for number in row):
            return True
    
    for index in range(0, len(bingo_card)):
        if all(number in draw_list for number in [x[index] for x in bingo_card]):
            return True
    return False

# Import data
# Bingo numbers and bingo cards are split by \n\n
bingo_objects = list()
with open("/home/agaspari/aoc2021/dec_4/dec4_input.txt") as f:
    bingo_objects = [x for x in f.read().split('\n\n')]

# Bingo draws are the numbers drawn, which are separated by a comma
bingo_draws = bingo_objects[0].split(',')

# Bingo cards are each a 5x5 matrix
raw_bingo_cards = bingo_objects[1:]
bingo_cards = list()
for card in raw_bingo_cards:
    bingo_cards.append([re.findall(r'[0-9]{,2}[^\s]', x) for x in card.split('\n')])

# Task 1
drawn_numbers = list()
for number in bingo_draws:
    drawn_numbers.append(number)
    for bingo_card in bingo_cards:
        if find_winning_card(bingo_card=bingo_card, draw_list=drawn_numbers):
            flattened_card = sorted([int(item) for row in bingo_card for item in row])
            leftovers = [item for item in flattened_card if str(item) not in drawn_numbers]
            print(bingo_card, drawn_numbers, sep='\n')
            print(sum(leftovers) * int(drawn_numbers[-1]))
            break
    else:
        continue
    break

# Task 2
drawn_numbers = list()
for number in bingo_draws:
    drawn_numbers.append(number)
    cards_to_pop = list()
    for index, bingo_card in enumerate(bingo_cards):
        if find_winning_card(bingo_card=bingo_card, draw_list=drawn_numbers):
            cards_to_pop.append(index)
            last_card_to_win = bingo_card
            last_winning_num = list(drawn_numbers)
    for card in cards_to_pop[::-1]:
        bingo_cards.pop(card)

flattened_card = sorted([int(item) for row in last_card_to_win for item in row])
leftovers = [item for item in flattened_card if str(item) not in last_winning_num]
print(last_card_to_win, last_winning_num, sep='\n')
print(sum(leftovers) * int(last_winning_num[-1]))
