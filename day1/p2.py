#!/usr/bin/python3

with open('input.txt') as f:
  input = f.read().splitlines()

calories = []
current = 0
for line in input:
  if line == '':
    calories.append(current)
    current = 0
    continue
  current += int(line)
print(sum(sorted(calories, reverse=True)[:3]))
