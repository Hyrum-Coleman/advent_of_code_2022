# Hyrum Coleman
# Advent of Code Day 1

import csv

# 1. Read input from elf_packs.csv

with open('elf_packs.csv', 'r') as f:
    reader = csv.reader(f)
    elf_packs = list(reader)
    elf_list = []
    group_list = []

    for idx, item in enumerate(elf_packs):

        if item:
            elf_list.append(int(item[0]))
        else:
            # store elf in elf class
            group_list.append(elf_list)
            elf_list = []

# 2. Store calorie sums in a list

max_calories = 0
calorie_sum_list = []
for idx, elf in enumerate(group_list):

    calorie_sum_list.append(sum(elf))

# 3. Find the 3 highest values of calorie_sum_list

max_calories = max(calorie_sum_list)
max_calories_idx = calorie_sum_list.index(max_calories)
calorie_sum_list[max_calories_idx] = 0
max_calories_2 = max(calorie_sum_list)
max_calories_2_idx = calorie_sum_list.index(max_calories_2)
calorie_sum_list[max_calories_2_idx] = 0
max_calories_3 = max(calorie_sum_list)


print(max_calories + max_calories_2 + max_calories_3)
