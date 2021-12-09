#!/usr/bin/env python3

# Import data
with open('/home/agaspari/aoc2021/dec_8/dec8_input.txt') as f:
    signal_list = f.read().split('\n')

unique_signals_one = {'c', 'f'}
unique_signals_four = {'b', 'c', 'd', 'f'}
unique_signals_seven = {'a', 'c', 'f'}
unique_signals_eight = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}

unique_signals = [
    unique_signals_one,
    unique_signals_four,
    unique_signals_seven,
    unique_signals_eight
]

unique_signals_lengths = [len(x) for x in unique_signals]

# Task 1 - How many times is a number with a unique number of segments output?
inputs = [x.split(' | ')[0] for x in signal_list]
outputs = [x.split(' | ')[1] for x in signal_list]
recognized_count = 0
for output in outputs:
    signal_patterns = [signal for signal in output.split(' ')]
    for signal_pattern in signal_patterns:
        if len(signal_pattern) in unique_signals_lengths:
            recognized_count += 1

print("Number of unique signal counts:", recognized_count)

# Task 2 - Decode the signals and get the output sum
# Known digits
# one: len == 2
# four: len == 4
# seven: len == 3
# eight: len == 7

# Unknown digits
# zero: len == 6, len(set(4) - set(0)) == 1, len(set(seven) - set(0)) == 0
# two: len == 5, len(set(4) - set(2)) == 2, len(set(7) - set(2)) == 1
# three: len == 5, len(set(4) - set(3)) == 1, len(set(7) - set(3)) == 0
# five: len == 5, len(set(4) - set(5)) == 1, len(set(7) - set(5)) == 1
# six: len == 6, len(set(4) - set(6)) == 1, len(set(7) - set(6)) == 1
# nine: len == 6, len(set(4) - set(9)) == 0, len(set(7) - set(5)) == 0

decoded_outputs = list()
# Loop through inputs
for signal_input, signal_output in zip(inputs, outputs):
    known_digits = list()
    unknown_digits = list()
    # Check for known digits, check for unknown digits
    digits = [x for x in signal_input.split(' ')]
    for digit in digits:
        if len(digit) in unique_signals_lengths:
            known_digits.append({x for x in digit})
        else:
            unknown_digits.append({x for x in digit})

    known_digits = sorted(known_digits, key=len)
    all_digits = [0] * 10
    all_digits[1], all_digits[7], all_digits[4], all_digits[8] = known_digits[0],known_digits[1],known_digits[2],known_digits[3],
    for digit in unknown_digits:
        if len(digit) == 5:
            if len(all_digits[4] - digit) == 1 and len(all_digits[7] - digit) == 0:
                all_digits[3] = digit
            elif len(all_digits[4] - digit) == 1 and len(all_digits[7] - digit) == 1:
                all_digits[5] = digit
            else:
                all_digits[2] = digit
        else:
            if len(all_digits[4] - digit) == 1 and len(all_digits[7] - digit) == 0:
                all_digits[0] = digit
            elif len(all_digits[4] - digit) == 1 and len(all_digits[7] - digit) == 1:
                all_digits[6] = digit
            else:
                all_digits[9] = digit

    output_value = ''
    signal_outputs = [{x for x in output} for output in signal_output.split(' ')]
    for output_digit in signal_outputs:
        for index, input_digit in enumerate(all_digits):
            if output_digit == input_digit:
                output_value += str(index)
                break
            else:
                continue
    if len(output_value) < 4:
        raise ValueError("Error: not enough output values decoded")
    decoded_outputs.append(int(output_value))

print("Sum of output values:", sum(decoded_outputs))

