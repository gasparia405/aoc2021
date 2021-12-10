#!/usr/bin/env python3

# Import data
with open('/home/agaspari/aoc2021/dec_10/dec10_input.txt') as f:
    nav_lines = f.read().split('\n')

openers = ['<', '(', '[', '{']
closers = ['>', ')', ']', '}']

# Task 1: Find all of the corrupted lines
corrupted_char = list()
for line in nav_lines:
    curr_chunk = list()
    for char in line:
        if char in openers:
            curr_chunk.append(char)
        else:
            most_recent_open = curr_chunk[-1]
            if openers.index(most_recent_open) == closers.index(char):
                curr_chunk.pop()
            else:
                corrupted_char.append(char)
                break

syntax_checker_score = 0
for char in corrupted_char:
    if char == ')':
        syntax_checker_score += 3
    elif char == ']':
        syntax_checker_score += 57
    elif char == '}':
        syntax_checker_score += 1197
    else:
        syntax_checker_score += 25137

print(syntax_checker_score)

# Task 2: Finish the lines
all_autocomplete_scores = list()
for line in nav_lines:
    curr_chunk = list()
    for char in line:
        if char in openers:
            curr_chunk.append(char)
        else:
            most_recent_open = curr_chunk[-1]
            if openers.index(most_recent_open) == closers.index(char):
                curr_chunk.pop()
            else:
                break
    else:
        continue
    chars_to_close = list()
    for left_open in curr_chunk[::-1]:
        chars_to_close.append(closers[openers.index(left_open)])

    autocomplete_score = 0
    for char in chars_to_close:
        if char == ')':
            autocomplete_score *= 5
            autocomplete_score += 1
        elif char == ']':
            autocomplete_score *= 5
            autocomplete_score += 2
        elif char == '}':
            autocomplete_score *= 5
            autocomplete_score += 3
        else:
            autocomplete_score *= 5
            autocomplete_score += 4
    all_autocomplete_scores.append(autocomplete_score)

sorted_scores = sorted(all_autocomplete_scores)
print(sorted_scores[len(sorted_scores) // 2])
