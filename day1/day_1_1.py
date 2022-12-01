def calorie_counter(file_name):
    """Reads a file and returns the total calories for the day."""
    with open(file_name, 'r') as file:
        highest_calorie = 0
        cur_elf_calories = 0
        for line in file:
            if line == '\n':
                cur_elf_calories = 0
            else:
                cur_line_calories = int(line)
                cur_elf_calories += cur_line_calories
                if cur_elf_calories > highest_calorie:
                    highest_calorie = cur_elf_calories
    return highest_calorie

print(calorie_counter('./elf_calories.txt'))