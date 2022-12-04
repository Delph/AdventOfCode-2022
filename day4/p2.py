#!/usr/bin/python3

with open('input.txt') as f:
  input = f.read().splitlines()


overlap = 0
for pair in input:
  a, b = pair.split(',')
  al, ah = map(int, a.split('-'))
  bl, bh = map(int, b.split('-'))

  if al <= bl and ah >= bl or al <= bh and ah >= bh or bl <= al and bh >= al or bl <= ah and bh >= ah:
    overlap += 1
print(overlap)
