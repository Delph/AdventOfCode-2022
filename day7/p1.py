#!/usr/bin/python3

with open('input.txt') as f:
  input = f.read().splitlines()

total = 0
def size(dir):
  global total
  count = 0
  for k, v in dir.items():
    if k == '..':
      continue
    if type(v) == int:
      count += v
    else:
      count += size(dir[k])
  if count < 100000:
    total += count
  return count

i = 0
fs = {}
current = fs
while i < len(input):
  line = input[i]
  i += 1
  if not line.startswith('$'):
    continue
  command, *arg = line[2:].split(' ')
  arg = ''.join(arg)
  if command == 'cd':
    if arg == '/':
      current = fs
    elif arg == '..':
      current = current['..']
    else:
      if not arg in current:
        current[arg] = {
          '..': current
        }
      current = current[arg]
  elif command == 'ls':
    while i < len(input) and input[i][0] != '$':
      line = input[i]
      i += 1
      t, name = line.split(' ')
      if t == 'dir':
        if not name in current:
          current[name] = {'..': current}
      else:
        current[name] = int(t)

print(size(fs))
print(total)
