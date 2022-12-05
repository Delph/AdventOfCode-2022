#!/usr/bin/python3

import re

with open('input.txt') as f:
  input = f.read().splitlines()


stacks = []
for line in input:
  if '[' in line:
    for stack, item in enumerate(line[1::4]):
      if stack > len(stacks)-1:
        stacks.append([])
      if item == ' ':
        continue
      stacks[stack].insert(0, item)

  if line.startswith('move'):
    instr = re.findall('(\d+)', line)
    if len(instr) == 3:
      count, f, t = map(int, instr)
      for _ in range(count):
        item = stacks[f-1].pop()
        stacks[t-1].append(item)
print(''.join(stack[-1] for stack in stacks))
