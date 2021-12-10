#!/usr/bin/env python

def get_risk_level(height:int) -> int:
    return height + 1

def check_low_point_x(curr_height):
    pass


# Import data
with open('/home/agaspari/aoc2021/dec_9/dec9_input.txt') as f:
    height_map = [[int(height) for height in x] for x in f.read().split('\n')]

# Task 1: Get the sum of the risk level (1 + value) for all low points
risk_level_sum = 0
low_points = list()  # List of tuples containing low point coordinates
for index_y in range(0, len(height_map)):
    for index_x, curr_height in enumerate(height_map[index_y]):
        if curr_height == 9:
            continue
        # Validate index values
        if index_x == 0:
            if height_map[index_y][index_x + 1] < curr_height:
                continue
            else:
                if index_y == 0:
                    if height_map[index_y + 1][index_x] < curr_height:
                        continue
                    else:
                        risk_level_sum += get_risk_level(curr_height)
                        low_points.append((index_x, index_y))
                elif index_y + 1 == len(height_map):
                    if height_map[index_y -1][index_x] < curr_height:
                        continue
                    else:
                        risk_level_sum += get_risk_level(curr_height)
                        low_points.append((index_x, index_y))
                else:
                    if height_map[index_y - 1][index_x] > curr_height and height_map[index_y + 1][index_x] > curr_height:
                        risk_level_sum += get_risk_level(curr_height)
                        low_points.append((index_x, index_y))
        elif index_x + 1 == len(height_map[index_y]):
            if height_map[index_y][index_x - 1] < curr_height:
                continue
            else:
                if index_y == 0:
                    if height_map[index_y + 1][index_x] < curr_height:
                        continue
                    else:
                        risk_level_sum += get_risk_level(curr_height)
                        low_points.append((index_x, index_y))
                elif index_y + 1 == len(height_map):
                    if height_map[index_y -1][index_x] < curr_height:
                        continue
                    else:
                        risk_level_sum += get_risk_level(curr_height)
                        low_points.append((index_x, index_y))
                else:
                    if height_map[index_y - 1][index_x] > curr_height and height_map[index_y + 1][index_x] > curr_height:
                        risk_level_sum += get_risk_level(curr_height)
                        low_points.append((index_x, index_y))
        else:
            if height_map[index_y][index_x + 1] > curr_height and height_map[index_y][index_x - 1] > curr_height:
                pass
            else:
                continue
            if index_y == 0:
                if height_map[index_y + 1][index_x] < curr_height:
                    continue
                else:
                    risk_level_sum += get_risk_level(curr_height)
                    low_points.append((index_x, index_y))
            elif index_y + 1 == len(height_map):
                if height_map[index_y -1][index_x] < curr_height:
                    continue
                else:
                    risk_level_sum += get_risk_level(curr_height)
                    low_points.append((index_x, index_y))
            else:
                if height_map[index_y - 1][index_x] > curr_height and height_map[index_y + 1][index_x] > curr_height:
                    risk_level_sum += get_risk_level(curr_height)
                    low_points.append((index_x, index_y))

print(risk_level_sum)

# Task 2: Find the basins
def find_basin(height_map, starting_point, direction=None, points_hit=set()):
    directions = ["right", "left", "up", "down"]

    for direction in directions:
        if direction == "right":
            x_coord, y_coord = starting_point[0], starting_point[1]
            curr_height = height_map[y_coord][x_coord]
            # Move right
            tmp_height = curr_height
            if x_coord + 1 != len(height_map):
                tmp_height = height_map[y_coord][x_coord + 1]
                if tmp_height != 9:
                    tmp_point = (x_coord + 1, y_coord)
                    if tmp_point in points_hit:
                        continue
                    points_hit.add(tmp_point)
                    find_basin(height_map, tmp_point, direction, points_hit)
        elif direction == "left":
            x_coord, y_coord = starting_point[0], starting_point[1]
            curr_height = height_map[y_coord][x_coord]
            tmp_height = curr_height
            if x_coord != 0:
                tmp_height = height_map[y_coord][x_coord - 1]
                if tmp_height != 9:
                    tmp_point = (x_coord - 1, y_coord)
                    if tmp_point in points_hit:
                        continue
                    points_hit.add(tmp_point)
                    find_basin(height_map, tmp_point, direction, points_hit)
        elif direction == "up":
            x_coord, y_coord = starting_point[0], starting_point[1]
            curr_height = height_map[y_coord][x_coord]
            tmp_height = curr_height
            if y_coord != 0:
                tmp_height = height_map[y_coord - 1][x_coord]
                if tmp_height != 9:
                    tmp_point = (x_coord, y_coord - 1)
                    if tmp_point in points_hit:
                        continue
                    points_hit.add(tmp_point)
                    find_basin(height_map, tmp_point, direction, points_hit)
        else:
            x_coord, y_coord = starting_point[0], starting_point[1]
            curr_height = height_map[y_coord][x_coord]
            # Move right
            tmp_height = curr_height
            if y_coord + 1 != len(height_map):
                tmp_height = height_map[y_coord + 1][x_coord]
                if tmp_height != 9:
                    tmp_point = (x_coord, y_coord + 1)
                    if tmp_point in points_hit:
                        continue
                    points_hit.add(tmp_point)
                    find_basin(height_map, tmp_point, direction, points_hit)
    return len(points_hit)

largest_three_basins = [0, 0, 0] 
for low_point in low_points:
    basin_size = find_basin(height_map, low_point, points_hit=set())
    largest_three_basins.append(basin_size)
    largest_three_basins = sorted(largest_three_basins, reverse=True)[:3]

print(largest_three_basins)
print(largest_three_basins[0] * largest_three_basins[1] * largest_three_basins[2])
