#part 1
with open('in.txt', 'r') as f:
    lines = f.readlines()

moves = []
for line in lines:
    moves.append([line[0], int(line[1:])])

head = [0,0]
oldHead = [0,0]
tail = [0,0]
tail_positions_p1 = set()
def update_tail(head, tail, oldHead):
    if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1: #if the head is distant
        tail[0] = oldHead[0]
        tail[1] = oldHead[1]
    oldHead[0] = head[0]
    oldHead[1] = head[1]
    return tail, oldHead

for move in moves:
    direction = move[0]
    magnitude = move[1]
    #print('move: ', move)
    for i in range(1, magnitude + 1):
        tail_positions_p1.add((tail[0], tail[1]))
        if direction == 'U':
            head[1] += 1
        elif direction == 'D':
            head[1] -= 1
        elif direction == 'R':
            head[0] += 1
        elif direction == 'L':
            head[0] -= 1
        #print('tail', tail)
        tail_positions_p1.add((tail[0], tail[1]))
        tail, oldHead = update_tail(head, tail, oldHead)

print('part 1' , len(tail_positions_p1))

#part 2

body = []
old_body = []
for i in range(0,10):
    body.append([0,0])
    old_body.append([0,0])
tail_positions_p2 = set()
for move in moves:
    print('move: ', move)
    tail_positions_p2.add((body[-1][0], body[-1][1]))
    direction = move[0]
    magnitude = move[1]
    for i in range(1, magnitude + 1):
        tail_positions_p1.add((tail[0], tail[1]))
        if direction == 'U':
            body[0][1] += 1
        elif direction == 'D':
            body[0][1] -= 1
        elif direction == 'R':
            body[0][0] += 1
        elif direction == 'L':
            body[0][0] -= 1
        for i in range(1, len(body)):
            if body[i-1][0] - body[i][0] > 1:
                body[i][0] += 1
                if body[i-1][0] - body[i][0] < 0:
                    body[i][0] -= 1
                if body[i-1][1] - body[i][1] > 0:
                    body[i][1] += 1
                if body[i-1][1] - body[i][1] < 0:
                    body[i][1] -= 1
            elif body[i-1][0] - body[i][0] < -1:
                body[i][0] -= 1
                if body[i-1][0] - body[i][0] > 0:
                    body[i][0] += 1
                if body[i-1][1] - body[i][1] > 0:
                    body[i][1] += 1
                if body[i-1][1] - body[i][1] < 0:
                    body[i][1] -= 1
            elif body[i-1][1] - body[i][1] > 1:
                body[i][1] += 1
                if body[i-1][1] - body[i][1] < 0:
                    body[i][1] -= 1
                if body[i-1][0] - body[i][0] > 0:
                    body[i][0] += 1
                if body[i-1][0] - body[i][0] < 0:
                    body[i][0] -= 1
            elif body[i-1][1] - body[i][1] < -1:
                body[i][1] -= 1
                if body[i-1][1] - body[i][1] > 0:
                    body[i][1] += 1
                if body[i-1][0] - body[i][0] > 0:
                    body[i][0] += 1
                if body[i-1][0] - body[i][0] < 0:
                    body[i][0] -= 1
            tail_positions_p2.add((body[-1][0], body[-1][1]))




        print('body', body)

print('part 2' , len(tail_positions_p2))