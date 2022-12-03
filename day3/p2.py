#!/usr/bin/python3

with open('input.txt') as f:
  input = f.read().splitlines()


def priority(item):
  if item >= 'a' and item <= 'z':
    return ord(item) - ord('a') + 1
  return ord(item) - ord('A') + 27

badges = []
for group in zip(*[iter(input)]*3):
  a, b, c = map(set, group)
  common = [i for i in a if i in b and i in c]
  badges.extend(common)

print(sum(priority(i) for i in badges))
