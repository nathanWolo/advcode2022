import time
def get_value(ticks, register):
    print('ticks', ticks, 'register', register)
    if ticks % 40 == 20:
        values.append(register*ticks)

with open('in.txt', 'r') as f:
    lines = f.readlines()

# Part 1
ticks = 0
register = 1
values = []
for line in lines:
    if line[0] == 'n':
        ticks+=1
        get_value(ticks, register)
    elif line[0] == 'a':
        #find the int in the string
        
        ticks += 1
        get_value(ticks, register)
        ticks += 1
        get_value(ticks, register)
        register += int(line[4:])
ticks+=1
get_value(ticks, register)
print('values', values)
print('sum' , sum(values))

def print_pixel(ticks, register):
    if ((ticks) % 40 - register) in [-1,0,1]:
        print('#', end='')
    else:
        print('.', end='')
    if ticks % 40 == 39:
        print('\n', end='')
    
# Part 2
ticks = 0
register = 1
for line in lines:
    #time.sleep(0.2)
    if line[0] == 'n':
        print_pixel(ticks, register)
        ticks+=1
    elif line[0] == 'a':
        #find the int in the string
        print_pixel(ticks, register)
        ticks += 1
        print_pixel(ticks, register)
        ticks += 1
        register += int(line[4:])

ticks+=1
print_pixel(ticks, register)
print('\n', end='')