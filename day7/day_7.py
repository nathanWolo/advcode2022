# take in a text file representing input/output history of a shell
#parse all output and reconstruct the file system
#find all directories with size < 100000
#return the sum of the sizes of all such directories
import re
import time
with open('day_7_input.txt') as f:
    lines = f.readlines()

#parse the input
dirs = ['/']
dir_sizes = {'/': 0}
current_dir = ''
for line in lines:
    if '$ cd' in line:
        #use re to get the directory name
        target = re.search(r'cd (.*)', line).group(1)
        if target == '..':
            #current dir becomes the parent dir
            current_dir = current_dir.rsplit('/', 1)[0]
            if current_dir == '':
                current_dir = '/'
        else:
            if current_dir == '' or current_dir == '/':
                current_dir = current_dir + target
            else:
                current_dir = current_dir + '/' + target
    if '$ ls' in line:
        continue
    else:
        if any(char.isdigit() for char in line):
            #use re to get the size
            size = int(re.search(r'(\d+)', line).group(1))
            for dir in dirs:
                if dir in current_dir:
                    dir_sizes[dir] += size
        if 'dir' in line:
            #use re to get the directory name
            new_dir = re.search(r'dir (.*)', line).group(1)
            if current_dir =='/':
                new_dir = '/' + new_dir
            else:
                new_dir = current_dir + '/' + new_dir
            if new_dir not in dirs:
                dirs.append(new_dir)
                dir_sizes[new_dir] = 0


sum = 0
for dir in dirs:
    if dir_sizes[dir] < 10**5:
        #print(dir, dir_sizes[dir])
        sum += dir_sizes[dir]

print('part 1 sum: ', sum)

#part 2

current_space = 70000000 - dir_sizes['/']

need = 30000000

min = 10**10

for dir in dirs:
    if dir_sizes[dir] < min and current_space + dir_sizes[dir] > need:
        min = dir_sizes[dir]

print('part 2 min: ', min)