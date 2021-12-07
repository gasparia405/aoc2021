#!/usr/bin/env python3

# Import data
with open('/home/alennon/aoc2021/dec_7/dec7_input.txt') as f:
    crab_list = sorted([int(x) for x in f.read().split(',')])

# Task 1
# Find the closest number to all numbers in the list
low = 0
high = len(crab_list) - 1
lowest_sum = sum([abs(crab_list[-1] - x) for x in crab_list])
proxy_crab = crab_list
for value in range(0, crab_list[-1]):
    new_sum = sum([abs(value - x) for x in crab_list])
    if new_sum > lowest_sum:
        break
    else:
        lowest_sum = new_sum
        continue

print(lowest_sum)
