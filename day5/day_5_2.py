with open('./day_5_1_input.txt', 'r') as f:
    text = f.read()
    lines = text.splitlines()

firstline = lines[0]
num_piles = (len(firstline) + 1) // 4 # 4 chars per pile, 3 on the last one

piles = []
for i in range(num_piles):
    piles.append([])
#get the piles, stop when we get to a newline (the moves)
for line in lines:
    if line == '\n':
        break
    cur_pile = 0
    chars_traversed = 0
    for ch in line:
        if ch.isupper():
            piles[cur_pile].append(ch)
        chars_traversed += 1
        if chars_traversed % 4 == 0:
            cur_pile += 1

#now we have the piles, we can start the moves
moves = []
in_moves = False
for line in lines:
    # check if there is a digit in the string
    if any(char.isdigit() for char in line):
        #strip the line of anything thats not a number
        toks = line.split(' ')
        moves.append([int(ch) for ch in toks if ch.isdigit()])
del moves[0] #remove the first move, accidentally including crate labels


#first element of a move is the size of the move, second is the pile to move from, third is the pile to move to
for move in moves:
    print(move)
    size = move[0]
    from_pile = move[1] - 1
    to_pile = move[2] - 1
    #get the top size crates from the from_pile by getting the first size elements of the list
    target_crates = piles[from_pile][:size]
    #remove the target crates from the from_pile
    piles[from_pile] = piles[from_pile][size:]
    piles[to_pile] = target_crates + piles[to_pile] #only change we need from day 1 is not reversing the stack we add

    
for pile in piles:
    print(pile)