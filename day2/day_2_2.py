def calculate_score(strategy_guide):
    score = 0
    for line in strategy_guide:
        opponent_choice, outcome = line.strip().split()
        if opponent_choice == 'A':
            # Rock
            if outcome == 'X':
                # Rock vs Scissors: lose
                score += 3
            elif outcome == 'Y':
                # Rock vs Rock: draw
                score += 4
            else:
                # Rock vs Paper: win
                score += 8
        elif opponent_choice == 'B':
            # Paper
            if outcome == 'X':
                # Paper vs Rock: lose
                score += 1
            elif outcome == 'Y':
                # Paper vs Paper: draw
                score += 5
            else:
                # Paper vs Scissors: win
                score += 9
        else:
            # Scissors
            if outcome == 'X':
                # Scissors vs Paper: lose
                score += 2
            elif outcome == 'Y':
                # Scissors vs Scissors: draw
                score += 6
            else:
                # Scissors vs Rock: win
                score += 7
    return score

# Example:
strategy_guide = []
with open('./day_2_1_input.txt') as f:
    for line in f:
        strategy_guide.append(line)
print(calculate_score(strategy_guide))  # should print 12
