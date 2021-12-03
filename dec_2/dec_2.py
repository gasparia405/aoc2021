#!/usr/bin/env python

# Task 1
instructions = list()
with open("./dec_2/dec2_input.txt") as f:
    instructions = [x for x in f.read().split('\n')]

start_position = [0, 0]
for direction in instructions:
    info = direction.split(' ')
    vector, length = info[0], int(info[1])
    if vector == "forward":
        start_position[0] += length
    elif vector == "up":
        start_position[1] -= length
    elif vector == "down":
        start_position[1] += length

print(start_position[0] * start_position[1])

# Task 2
start_position = [0, 0, 0]
for direction in instructions:
    info = direction.split(' ')
    vector, length = info[0], int(info[1])
    if vector == "forward":
        start_position[0] += length
        start_position[1] += length * start_position[2]
    elif vector == "up":
        start_position[2] -= length
    elif vector == "down":
        start_position[2] += length
    print(info, start_position)

print(start_position[0] * start_position[1])
