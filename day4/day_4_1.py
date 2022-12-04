def range_contains(range1, range2):
  # Check if the first range is fully contained in the second range
  if range1[0] >= range2[0] and range1[1] <= range2[1]:
    return True
  # Check if the second range is fully contained in the first range
  elif range2[0] >= range1[0] and range2[1] <= range1[1]:
    return True
  # Otherwise, the ranges do not fully contain each other
  else:
    return False
def range_overlap(range1, range2):
  # If the ranges have a non-zero intersection, then there is overlap
  return range1[0] <= range2[1] and range1[1] >= range2[0]




elf_counter_subset = 0
elf_counter_intersect = 0
with open('day_4_1_input.txt', 'r' ) as f:
    ranges = f.read().splitlines()


for range in ranges:
  range1, range2 = range.split(',')
  range1 = range1.split('-')
  range2 = range2.split('-')
  range1 = [int(range1[0]), int(range1[1])]
  range2 = [int(range2[0]), int(range2[1])]
  if range_contains(range1, range2):
    elf_counter_subset += 1
  if range_overlap(range1, range2):
    elf_counter_intersect += 1
print("subset: ", elf_counter_subset)
print("intersect: ", elf_counter_intersect)
