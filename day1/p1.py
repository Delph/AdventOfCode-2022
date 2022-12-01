#!/usr/bin/python3

with open('input.txt') as f:
  input = f.read().splitlines()

most = 0
current = 0
for line in input:
  if line == '':
    if current > most:
      most = current
    current = 0
    continue
  current += int(line)
print(most)
