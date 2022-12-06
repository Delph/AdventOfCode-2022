#!/usr/bin/python3

with open('input.txt') as f:
  input = f.read().splitlines()[0]

for i in range(len(input)):
  if len(set([c for c in input[i:i+4]])) == 4:
    print(i+4)
    break
