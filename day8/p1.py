#!/usr/bin/python3

with open('input.txt') as f:
  input = list(map(lambda x: [int(t) for t in x], f.read().splitlines()))
WIDTH = len(input[0])
HEIGHT = len(input)

def visible(x, y):
  if x == 0 or x == WIDTH - 1:
    return True
  if y == 0 or y == HEIGHT - 1:
    return True

  h = 0
  for i in range(x):
    if input[y][i] >= input[y][x]:
      h += 1
      break
  for i in range(x+1, WIDTH):
    if input[y][i] >= input[y][x]:
      h += 1
      break
  for j in range(y):
    if input[j][x] >= input[y][x]:
      h += 1
      break
  for j in range(y+1, HEIGHT):
    if input[j][x] >= input[y][x]:
      h += 1
      break

  return h < 4

count = 0
for x in range(WIDTH):
  for y in range(HEIGHT):
    if visible(x, y):
      count += 1
print(count)
