#Wumpus World Problem
#Without Function To Shoot The Wumpus
#To Display The Updated Map Every Time
def dis():
  for i in range(4):
    print(n[i])
  print()

#To Find The Next Possible Square To Move To
def find(ch, r, c):
  if c + 1 <= 3 and n[r][c + 1] == ch:
    return [r, c + 1]
  if c - 1 >= 0 and n[r][c - 1] == ch:
    return [r, c - 1]
  if r + 1 <= 3 and n[r + 1][c] == ch:
    return [r + 1, c]
  if r - 1 >= 0 and n[r - 1][c] == ch:
    return [r - 1, c]

#Update Map Depending On The New Sensory Data
def sense(r, c):
  if n[r][c] == '-':
    n[r][c] = m[r][c]
  return m[r][c]

#Draw Some Inferences From Sensed Data
def assume(s, r, c):
  if s == 'b' or s == 's':
    mkch('d', r, c)
    return False
  elif s == 'g':
    return True
  else:
    return False

#Apply Changes To The Map While Making Sure That Boundaries Are Maintained
def mkch(x, r, c):
  if r - 1 >= 0 and (n[r - 1][c] == '-' or n[r - 1][c] == 'd'):
    n[r - 1][c] = x
    think(r - 1, c)
  if r + 1 <= 3 and (n[r + 1][c] == '-' or n[r + 1][c] == 'd'):
    n[r + 1][c] = x
    think(r + 1, c)
  if c - 1 >= 0 and (n[r][c - 1] == '-' or n[r][c - 1] == 'd'):
    n[r][c - 1] = x
    think(r, c - 1)
  if c + 1 <= 3 and (n[r][c + 1] == '-' or n[r][c + 1] == 'd'):
    n[r][c + 1] = x
    think(r, c + 1)

#Actually Update The Map Using Some Logic
def think(r, c):
  p = 0
  w = 0
  if r - 1 >= 0:
    if 'b' in n[r - 1][c]:
      p += 1
    if 's' in n[r - 1][c]:
      w += 1
  if r + 1 <= 3:
    if 'b' in n[r + 1][c]:
      p += 1
    if 's' in n[r + 1][c]:
      w += 1
  if c - 1 >= 0:
    if 'b' in n[r][c - 1]:
      p += 1
    if 's' in n[r][c - 1]:
      w += 1
  if c + 1 <= 3:
    if 'b' in n[r][c + 1]:
      p += 1
    if 's' in n[r][c + 1]:
      w += 1
  if p == w:
    n[r][c] = 'o'
  elif p >= 2:
    n[r][c] = 'p'
  elif w >= 2:
    n[r][c] = 'w'
  return 0

#Sensory Data
m = [['o', 'b', 'p', 'b'],
     ['s', 'o', 'b', 'o'],
     ['w', 'gsb', 'p', 'b'],
     ['s', 'o', 'b', 'p']]
#Map Agent Is Making
n = [['o', '-', '-', '-'],
     ['-', '-', '-', '-'],
     ['-', '-', '-', '-'],
     ['-', '-', '-', '-']]
#Starting Point
cord = [0, 0]
print(cord)
s = sense(cord[0], cord[1])
assume(s, cord[0], cord[1])
dis()
ec = 0
#Repeating Certain Steps Until The Problem Is Solved
while True:
  newc = []
  for i in '-obs':
    newc = find(i, cord[0], cord[1])
    if newc != [] and newc != None:
      cord = newc.copy()
      break
  print(cord)
  s = sense(cord[0], cord[1])
  for i in s:
    if assume(i, cord[0], cord[1]):
      ec = 1
      break
  dis()
  if ec == 1:
    print("Gold Found! \nAt Coordinates", cord)
    break
