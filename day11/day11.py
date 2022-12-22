from monkey import Monkey
import inspect

with open('in.txt', 'r') as f:
    lines = f.readlines()
#sample input
''' Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3''' 

#parse input
monkeys = []
i = 0
test = 0
items = []
targets = []
operation = ''
val = 0
for line in lines:
    if 'Starting items:' in line:
        items = [int(x) for x in line.split(':')[1].split(',')]
    elif 'Operation:' in line:
        if '+' in line:
            val = int(line.split('+')[1])
            operation = '+'
        elif '*' in line:
            if 'old * old' in line:
                operation = '**2'
            else:
                val = int(line.split('*')[1])
                #print(num)
                operation = '*'
    elif 'Test:' in line:
        if 'divisible' in line:
            test = int(line.split('by')[1].split(' ')[1])
    elif 'true' in line:
        targets.append(int(line.split(' ')[-1]))
    elif 'false' in line:
        targets.append(int(line.split(' ')[-1]))
        monkeys.append(Monkey(items, operation, test, targets, val))
        targets = []
        i += 1
        num = 0

#print([str(m) for m in monkeys])
j = 0
# print(monkeys[0].operate(2))
global inspection_count
inspection_count = []
for monkey in monkeys:
    inspection_count.append(0)
modulus = 1
for monkey in monkeys:
    modulus = modulus * monkey.test_criteria
def run_round(monkeys):
        j = 0
        for monkey in monkeys:
        #monkey inspects its items
            for item in monkey.items:
               # print('Monkey ' + str(j) + ' inspects an item with a worry level of ' +str(item) )
                new_item = monkey.operate(item)
                inspection_count[j] += 1
               # print('The new worry level of the item is  operated on  and is now '  + str(new_item))
               # new_item = int(new_item /3) no longer needed in part 2
                new_item = new_item % modulus #keeping size manageable while preserving the information
               # print('The new worry level of the item is ' + str(new_item))
                if monkey.test(new_item):
                    monkeys[monkey.targets[0]].items.append(new_item)
                   # print('monkey ' + str(monkey.targets[0]) + ' got ' + str(new_item) + ' from monkey ' + str(j) )
                else:
                    monkeys[monkey.targets[1]].items.append(new_item)
                   # print('monkey ' + str(monkey.targets[1]) + ' got ' + str(new_item) + ' from monkey ' + str(j))
            monkey.items = []
            j = j + 1

for x in range(1, 10001):
    run_round(monkeys)
    #print('round ' + str(x), end=': ')
    #print([m.items for m in monkeys])

#print(inspection_count)
inspection_count.sort()
print(inspection_count[-1] * inspection_count[-2])