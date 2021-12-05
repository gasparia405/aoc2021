#!/usr/bin/env python

def get_most_common_bit(bit_list: list, index: int) -> int:
    return str(int(sum([int(bit[index]) for bit in bit_list]) >= len(bit_list) / 2))

def get_least_common_bit(bit_list: list, index: int) -> int:
    return str(int(sum([int(bit[index]) for bit in bit_list]) < len(bit_list) / 2))

diagnoses = list()
with open("./dec_3/dec3_input.txt") as f:
    diagnoses = [x for x in f.read().split('\n')]

# Task 1
gamma_result = ""
for index in range(0, len(diagnoses[0])):
    gamma_result += get_most_common_bit(diagnoses, index)

epsilon_result = ""
for index in range(0, len(diagnoses[0])):
    epsilon_result += get_least_common_bit(diagnoses, index)

print(int(gamma_result, 2))
print(int(epsilon_result, 2))

print(int(gamma_result, 2) * int(epsilon_result, 2))

# Task 2
o2_scrubber = diagnoses
o2_scrubber_index = 0
while len(o2_scrubber) > 1:
    ref_bit = get_most_common_bit(o2_scrubber, o2_scrubber_index)
    o2_scrubber = [diagnosis for diagnosis in o2_scrubber if diagnosis[o2_scrubber_index] == ref_bit]
    o2_scrubber_index += 1

print(int(o2_scrubber[0], 2))

co2_scrubber = diagnoses
co2_scrubber_index = 0
while len(co2_scrubber) > 1:
    ref_bit = get_least_common_bit(co2_scrubber, co2_scrubber_index)
    co2_scrubber = [diagnosis for diagnosis in co2_scrubber if diagnosis[co2_scrubber_index] == ref_bit]
    co2_scrubber_index += 1

print(int(co2_scrubber[0], 2))
print(int(co2_scrubber[0], 2) * int(o2_scrubber[0], 2))
