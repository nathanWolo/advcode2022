import ast
packets = []
with open('in.txt', 'r') as f:
    lines = f.read().splitlines()

for line in lines:
    if line != '':
        packets.append(ast.literal_eval(line))
            


def compare(left, right, i):
    #print(i)
    #print(left)
   # print(right)
    if i >= len(left) and i >= len(right):
        #print('past both lists')
        return 2
    if i >= len(left) or i >= len(right):
        #print('past one list')
        if len(left) < len(right):
            return 1
        else:
            return 0

    if isinstance(left[i], int) and isinstance(right[i], int):
        #print('ints')
        if left[i] < right[i]:
            return 1
        elif left[i] == right[i] :
            return compare(left, right, i+1)
        else:
            #print('false!!')
            return 0
    if isinstance(left[i], list) and isinstance(right[i], list):
        #print('lists')
        if compare(left[i], right[i], 0) == 2:
            #print('move forward')
            return compare(left, right, i+1)
        else:
            return compare(left[i], right[i], 0)
        
    else:
        #print('one list one int')
        if isinstance(left[i], int):
            #print(left)
            if compare([left[i]], right[i], 0) == 2:
                #print('move forward')
                return compare(left, right, i+1)
            return compare([left[i]], right[i], 0)
        else:
            if compare(left[i], [right[i]], 0) == 2:
                #print('move forward')
                return compare(left, right, i+1)
            return compare(left[i], [right[i]], 0)


results = []
#convert each line to a list
for i in range(0,len(packets)):
    if i % 2 == 0:
        left = packets[i]
        right = packets[i+1]
        #print('comparing', i)
        results.append(compare(left, right, 0) == 1)
        #print(results[-1])

#print(compare(packets[14], packets[15], 0))
#print(results)
tally = 0
for i in range(1, len(results) + 1):
    if results[i-1] == 1:
        tally = tally + i
print('part1')
print(tally)
packets.append([[2]])
packets.append([[6]])
is_sorted = False
while not is_sorted:
    is_sorted = True
    for i in range(0, len(packets) - 1,):
        if not compare(packets[i], packets[i+1], 0):
            is_sorted = False
            packets[i], packets[i+1] = packets[i+1], packets[i]
print('part2: ')
print((packets.index([[2]]) + 1)*(packets.index([[6]])+1))