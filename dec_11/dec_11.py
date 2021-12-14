#!/usr/bin/env python3

# Import data
with open('/home/agaspari/aoc2021/dec_11/dec11_input.txt') as f:
    octopus_rows = [[int(x) for x in row] for row in f.read().split('\n')]

class OctopusCave:
    def __init__(self, octopus_matrix):
        self.octopus_matrix = octopus_matrix
        self.flash_count = 0

    def advance_matrix(self):
        new_matrix = list()
        for row in self.octopus_matrix:
            new_matrix.append([x + 1 for x in row])
        self.octopus_matrix = new_matrix

    def flash(self):
        surrounding_idx = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        self.advance_matrix()
        while any(x > 9 for row in self.octopus_matrix for x in row):
            for r_idx, row in enumerate(self.octopus_matrix):
                for c_idx, octopus in enumerate(row):
                    if octopus > 9:
                        self.flash_count += 1
                        self.octopus_matrix[r_idx][c_idx] = 0
                        for r, c in surrounding_idx:
                            if r_idx == 0 and r == -1:
                                pass
                            elif r_idx == len(row) - 1 and r == 1:
                                pass
                            elif c_idx == 0 and c == -1:
                                pass
                            elif c_idx == len(row) - 1 and c == 1:
                                pass
                            else:
                                if self.octopus_matrix[r_idx + r][c_idx + c] == 0:
                                    pass
                                else:
                                    self.octopus_matrix[r_idx + r][c_idx + c] = self.octopus_matrix[r_idx + r][c_idx + c] + 1

if __name__ == "__main__":
    # Task 1:
    octopus_mtrx = OctopusCave(octopus_rows)
    for day in range(0, 1000):
        previous_day = octopus_mtrx.flash_count
        octopus_mtrx.flash()
        if octopus_mtrx.flash_count - previous_day == len([x for row in octopus_rows for x in row]):
            print("All flash on day:", day + 1)
            break


    print(octopus_mtrx.octopus_matrix)
    print(octopus_mtrx.flash_count)