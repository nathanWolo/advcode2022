def calorie_counter(file_name):
    """Reads a file and returns the total calories for the day."""
    with open(file_name, 'r') as file:
        highest_calories = [0,0,0]
        cur_elf_calories = 0
        for line in file:
            if line == '\n':
                #sort highest_calories from lowest to highest
                highest_calories.sort()
                for i in range(0,3):
                    if cur_elf_calories > highest_calories[i]:
                        highest_calories[i] = cur_elf_calories
                        break
                cur_elf_calories = 0
            else:
                cur_line_calories = int(line)
                cur_elf_calories += cur_line_calories
    #return the sum of the highest calories for each elf
    return highest_calories

print(calorie_counter('./elf_calories.txt'))

print(sum(calorie_counter('./elf_calories.txt')))