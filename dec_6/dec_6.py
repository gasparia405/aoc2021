#!/usr/bin/env python

def count_fish(lanternfish: list, repro_day: int) -> int:
    return len([x for x in lanternfish if x == repro_day])

def pass_one_day(fish_age_hash: dict, day: int, lanternfish: list=None):
    if day == 0:
        if not lanternfish:
            raise AttributeError("Error: lanternfish list must be passed as arg")
        new_fish_age_hash = {
            'zero': count_fish(lanternfish, 1),
            'one': count_fish(lanternfish, 2),
            'two': count_fish(lanternfish, 3),
            'three': count_fish(lanternfish, 4),
            'four': count_fish(lanternfish, 5),
            'five': count_fish(lanternfish, 6),
            'six': count_fish(lanternfish, 0) + count_fish(lanternfish, 7),
            'seven': count_fish(lanternfish, 8),
            'eight': count_fish(lanternfish, 0),
        }
    else:
        new_fish_age_hash = {
            'zero': fish_age_hash['one'],
            'one': fish_age_hash['two'],
            'two': fish_age_hash['three'],
            'three': fish_age_hash['four'],
            'four': fish_age_hash['five'],
            'five': fish_age_hash['six'],
            'six': fish_age_hash['zero'] + fish_age_hash['seven'],
            'seven': fish_age_hash['eight'],
            'eight': fish_age_hash['zero'],
        }
    return new_fish_age_hash

# Import data
with open('/home/agaspari/aoc2021/dec_6/dec6_input.txt') as f:
    lanternfish = [int(x) for x in f.read().split(',')]

# Task 1
fish_age_hash = dict()
for day in range(0, 80):
    fish_age_hash = pass_one_day(fish_age_hash, day, lanternfish)

print(sum([v for v in fish_age_hash.values()]))

# Task 2
fish_age_hash = dict()
for day in range(0, 256):
    fish_age_hash = pass_one_day(fish_age_hash, day, lanternfish)

print(sum([v for v in fish_age_hash.values()]))
