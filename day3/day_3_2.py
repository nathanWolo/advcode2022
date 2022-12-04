priority = 0

with open('day_3_2_input.txt') as f:
    bags  = f.read().splitlines()

groups = []
i = 1
for bag in bags:
    if i % 3 == 1:
        groups.append([bag])
    else:
        groups[-1].append(bag)
    i += 1
for group in groups:
    print(group)
    for ch in group[0]:
        if ch in group[1] and ch in group[2]:
            #check if ch is upper or lowercase
            print(ch)
            if ch.isupper():
                priority += 27 + ord(ch) - ord('A')
            else:
                priority += 1 + ord(ch) - ord('a')
            break

print(priority)