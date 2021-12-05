#!/usr/bin/env python

def find_coords_along_vector(start_space: tuple, end_space: tuple, is_diag=False) -> list:
    """Find every coordinate along the path from start to end"""
    entered_coords_list = list()
    pos_x = start_space[0] < end_space[0]
    pos_y = start_space[1] < end_space[1]

    range_x = range(0, abs(start_space[0] - end_space[0]))
    range_y = range(0, abs(start_space[1] - end_space[1]))
    if is_diag:
        for x_change, y_change in zip(range_x, range_y):
            if pos_x and pos_y:
                entered_coords_list.append((start_space[0] + x_change, start_space[1] + y_change))
            elif pos_x and not pos_y:
                entered_coords_list.append((start_space[0] + x_change, start_space[1] - y_change))
            elif not pos_x and pos_y:
                entered_coords_list.append((start_space[0] - x_change, start_space[1] + y_change))
            else:
                entered_coords_list.append((start_space[0] - x_change, start_space[1] - y_change))
        entered_coords_list.append(end_space)
        return entered_coords_list
        
    if start_space[0] > end_space[0]:
        for space in range(0, start_space[0] - end_space[0]):
            entered_coords_list.append((start_space[0] - space, start_space[1]))
        entered_coords_list.append(end_space)
    elif start_space[0] < end_space[0]:
        for space in range(0, end_space[0] - start_space[0]):
            entered_coords_list.append((start_space[0] + space, start_space[1]))
        entered_coords_list.append(end_space)
    elif start_space[1] > end_space[1]:
        for space in range(0, start_space[1] - end_space[1]):
            entered_coords_list.append((start_space[0], start_space[1] - space))
        entered_coords_list.append(end_space)
    else:  # Hopefully only that start[1] < end[1]
        for space in range(0, end_space[1] - start_space[1]):
            entered_coords_list.append((start_space[0], start_space[1] + space))
        entered_coords_list.append(end_space)

    return entered_coords_list

# Import data
coords_list = list()
with open("/home/agaspari/aoc2021/dec_5/dec5_input.txt") as f:
    coords_list = [x for x in f.read().split('\n')]

all_coords_entered = set()
already_hit = set()  # elements of new coords_entered that are already in all_coords_entered
for coord in coords_list:
    coords_entered = list()
    start_and_end = coord.split(' -> ')
    start, end = tuple(map(int, start_and_end[0].split(','))), tuple(map(int, start_and_end[1].split(',')))
    if start[0] == end[0] or start[1] == end[1]:
        coords_entered = find_coords_along_vector(start, end)
    elif start[0] != end[0] and start[1] != end[1]:
        pass
    already_hit.update(set(coords_entered) & all_coords_entered)
    all_coords_entered.update(set(coords_entered))

print(len(already_hit))

# Task 2
all_coords_entered = set()
already_hit = set()  # elements of new coords_entered that are already in all_coords_entered
for coord in coords_list:
    coords_entered = list()
    start_and_end = coord.split(' -> ')
    start, end = tuple(map(int, start_and_end[0].split(','))), tuple(map(int, start_and_end[1].split(',')))
    if start[0] == end[0] or start[1] == end[1]:
        coords_entered = find_coords_along_vector(start, end)
    else:
        coords_entered = find_coords_along_vector(start, end, is_diag=True)
    matches = set(coords_entered) & all_coords_entered
    already_hit.update(matches)
    all_coords_entered.update(set(coords_entered))

print(len(already_hit))
