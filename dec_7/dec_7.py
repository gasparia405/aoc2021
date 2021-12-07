#!/usr/bin/env python3

# Import data
with open('/home/agaspari/aoc2021/dec_7/dec7_input.txt') as f:
    crab_list = sorted([int(x) for x in f.read().split(',')])

# Task 1
# Find the closest number to all numbers in the list
lowest_sum = sum([abs(crab_list[-1] - x) for x in crab_list])
for value in range(0, crab_list[-1]):
    new_sum = sum([abs(value - x) for x in crab_list])
    if new_sum > lowest_sum:
        break
    else:
        lowest_sum = new_sum
        continue

print(lowest_sum)

# Task 2
lowest_sum = sum([abs(crab_list[-1] - x) * abs(crab_list[-1] - x) for x in crab_list])
for value in range(0, crab_list[-1]):
    dist_list = [abs(value - x) * (abs(value - x) + 1) // 2 for x in crab_list]
    new_sum = sum(dist_list)
    if new_sum > lowest_sum:
        continue
    else:
        lowest_sum = new_sum

print(lowest_sum)
# Get the minimum value in a list of sums of the list of distances from values for each crab position
print(min([sum([abs(value - x) * (abs(value - x) + 1) // 2 for x in crab_list]) for value in range(0, crab_list[-1])]))
