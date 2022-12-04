def calculate_score(strategy_guide):
    score = 0
    for line in strategy_guide:
        opponent_choice, your_choice = line.strip().split()
        if opponent_choice == 'A':
            # Rock
            if your_choice == 'X':
                # Rock vs Rock: draw
                score += 4
            elif your_choice == 'Y':
                # Rock vs Paper: win
                score += 8
            else:
                # Rock vs Scissors: lose
                score += 3
        elif opponent_choice == 'B':
            # Paper
            if your_choice == 'X':
                # Paper vs Rock: lose
                score += 1
            elif your_choice == 'Y':
                # Paper vs Paper: draw
                score += 5
            else:
                # Paper vs Scissors: win
                score += 9
        else:
            # Scissors
            if your_choice == 'X':
                # Scissors vs Rock: win
                score += 7
            elif your_choice == 'Y':
                # Scissors vs Paper: lose
                score += 2
            else:
                # Scissors vs Scissors: draw
                score += 6
    return score

# Example:
strategy_guide = []
with open('./day_2_1_input.txt') as f:
    for line in f:
        strategy_guide.append(line)
print(calculate_score(strategy_guide))  # should print 15
