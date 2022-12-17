with open('day_6_1_input.txt', 'r') as f:
    text = f.read()
def slide(text, context_window_size):
    for i in range(0, len(text)):
        window = text[i:i+context_window_size]
        if len(set(window)) == context_window_size:
            return i + context_window_size
            break

print('part 1 ', slide(text, 4))

print('part 2 ', slide(text, 14))