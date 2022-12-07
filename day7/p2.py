#!/usr/bin/python3

with open('input.txt') as f:
  input = f.read().splitlines()

smallest = None
def size(dir, sz=None):
  global smallest
  count = 0
  for k, v in dir.items():
    if k == '..':
      continue
    if type(v) == int:
      count += v
    else:
      count += size(dir[k], sz)
  if sz != None and count > sz and (smallest == None or count < smallest):
    smallest = count
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

remaining = 70000000 - size(fs)
size(fs, 30000000 - remaining)
print(smallest)
