#!/usr/bin/python3

with open('input.txt') as f:
  input = f.read().splitlines()


def priority(item):
  if item >= 'a' and item <= 'z':
    return ord(item) - ord('a') + 1
  return ord(item) - ord('A') + 27


common = []
for bag in input:
  first = set(bag[:len(bag)//2])
  second = set(bag[len(bag)//2:])

  common.extend((i for i in first if i in second))

print(sum(priority(i) for i in common))
