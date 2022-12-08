#!/usr/bin/python3

with open('input.txt') as f:
  input = list(map(lambda x: [int(t) for t in x], f.read().splitlines()))
WIDTH = len(input[0])
HEIGHT = len(input)

def score(x, y):
  if x == 0 or x == WIDTH - 1:
    return 0
  if y == 0 or y == HEIGHT - 1:
    return 0

  s = 1
  t = 0
  for i in range(x-1, -1, -1):
    t += 1
    if input[y][i] >= input[y][x]:
      break
  s *= t
  t = 0
  for i in range(x+1, WIDTH):
    t += 1
    if input[y][i] >= input[y][x]:
      break
  s *= t
  t = 0
  for j in range(y-1, -1, -1):
    t += 1
    if input[j][x] >= input[y][x]:
      break
  s *= t
  t = 0
  for j in range(y+1, HEIGHT):
    t += 1
    if input[j][x] >= input[y][x]:
      break
  s *= t

  return s

best = 0
for x in range(WIDTH):
  for y in range(HEIGHT):
    s = score(x, y)
    if s > best:
      best = s
print(best)
