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


def choose(them, result):
  if them == 'A':
    if result == 'X':
      return 'Z'
    elif result == 'Y':
      return 'X'
    else:
      return 'Y'
  elif them == 'B':
    if result == 'X':
      return 'X'
    elif result == 'Y':
      return 'Y'
    else:
      return 'Z'
  else:
    if result == 'X':
      return 'Y'
    elif result == 'Y':
      return 'Z'
    else:
      return 'X'


score = 0
for round in input:
  them, result = round.split(' ')
  score += points(choose(them, result), them)
print(score)
