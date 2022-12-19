with open('in.txt', 'r') as f:
    lines = f.readlines()


forest = []
for line in lines:
    forest.append([int(char) for char in line.strip()])
sum = 0
visible = False
visible_from_left = True
visible_from_right = True
visible_from_top = True
visible_from_bottom = True
for x in range(0, len(forest)):
    for y in range(0,len(forest[x])):
        if x == 0 or y == 0 or x == len(forest) - 1 or y == len(forest[x]) - 1:
            visible = True
        else:
            # check the x axis to see if any tree is taller from the left
            for i in range(0, y):
                if forest[x][i] >= forest[x][y]:
                    visible_from_left = False
                    break
            for i in range(y + 1, len(forest[y])):
                if forest[x][i] >= forest[x][y]:
                    visible_from_right = False
                    break
            for i in range(0, x):
                if forest[i][y] >= forest[x][y]:
                    visible_from_top = False
                    break
            for i in range(x + 1, len(forest)):
                if forest[i][y] >= forest[x][y]:
                    visible_from_bottom = False
                    break
        if visible or visible_from_left or visible_from_right or visible_from_top or visible_from_bottom:
            sum += 1
        visible = False
        visible_from_left = True
        visible_from_right = True
        visible_from_top = True
        visible_from_bottom = True


print('part 1: ', sum)

#part 2
left_view = 1
right_view = 1
up_view = 1
down_view = 1
max = 0
score = 0
for x in range(0, len(forest)):
    for y in range(0,len(forest[x])):
        #left view
        for i in range(y - 1, 0, -1):
            if forest[x][i] < forest[x][y]:
                left_view += 1
            else:
                break
        #right view
        for i in range(y + 1, len(forest[x]) -1):
            if forest[x][i] < forest[x][y]:
                right_view += 1
            else:
                break
        #up view
        for i in range(x - 1, 0, -1):
            if forest[i][y] < forest[x][y]:
                up_view += 1
            else:
                break
        #down view
        for i in range(x + 1, len(forest) -1):
            if forest[i][y] < forest[x][y]:
                down_view += 1
            else:
                break
        score = left_view *right_view * up_view * down_view
        if x == 0 or y == 0 or x == len(forest) - 1 or y == len(forest[x]) - 1:
            score = 0
        if score > max:
            max = score
        left_view = 1
        right_view = 1
        up_view = 1
        down_view = 1

print('part 2: ', max)