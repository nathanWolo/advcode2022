def split_string(s):
    # Calculate the midpoint of the string
    midpoint = len(s) // 2
    
    # Split the string at the midpoint
    s1 = s[:midpoint]
    s2 = s[midpoint:]
    
    # Return the two halves of the string as a tuple
    return (s1, s2)

priority = 0
with open('./day_3_1_input.txt') as f:
    bags  = f.read().splitlines()
separated_bags = []
for bag in bags:
    separated_bags.append(split_string(bag))

for bag in separated_bags:
    seen = set()
    for ch in bag[0]:
        if ch in bag[1] and ch not in seen:
            seen.add(ch)
            #check if ch is upper or lowercase
            if ch.isupper():
                priority += 27 + ord(ch) - ord('A')
            else:
                priority += 1 + ord(ch) - ord('a')
print(priority)