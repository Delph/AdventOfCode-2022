#!/usr/bin/python3

with open('input.txt') as f:
  input = f.read().splitlines()


def points(me, them):
  value = 0
  if me == 'X':
    value += 1
  elif me == 'Y':
    value += 2
  elif me == 'Z':
    value += 3

  if me == 'X':
    if them == 'C':
      value += 6
    elif them == 'A':
      value += 3
  elif me == 'Y':
    if them == 'A':
      value += 6
    elif them == 'B':
      value += 3
  else:
    if them == 'B':
      value += 6
    elif them == 'C':
      value += 3
  return value


score = 0
for round in input:
  them, me = round.split(' ')
  score += points(me, them)
print(score)
