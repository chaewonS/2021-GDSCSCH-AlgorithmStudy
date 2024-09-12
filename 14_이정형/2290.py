# -*- coding: utf-8 -*-
s, n = map(int, input().split())

w = '_'
h = '|'

# 총 위치는 7위치로 잡고 각 숫자가 나올때마다 해당 위치에 그려주는 식으로 하면 될 것 같다.
# 먼저 얼마나 그릴지에 대해 초기화를 해주자
def limit():
  num = [[' '] * (s + 2) for _ in range(2 * s + 3)]
  return num

# num = limit()
# print(num)

def toptop(num):
  for i in range(1, s+1):
    num[0][i] = w
    
def lefttop(num):
  for i in range(1, s+1):
    num[i][0] = h
    
def righttop(num):
  for i in range(1, s+1):
    num[i][-1] = h
    
def middle(num):
  for i in range(1, s+1):
    num[s+1][i] = w
    
def leftbottom(num):
  for i in range(s+2, 2*s + 2):
    num[i][0] = h
    
def rightbottom(num):
  for i in range(s+2, 2*s + 2):
    num[i][-1] = h
    
def topbottom(num):
  for i in range(1, s+1):
    num[2*s + 2][i] = w

def drawing(c, num):
  if c in [0, 2, 3, 5, 6, 7, 8, 9]:
    toptop(num)
  if c in [0, 4, 5, 6, 8, 9]:
    lefttop(num)
  if c in [0, 1, 2, 3, 4, 7, 8, 9]:
    righttop(num)
  if c in [2, 3, 4, 5, 6, 8, 9]:
    middle(num)
  if c in [0, 2, 6, 8]:
    leftbottom(num)
  if c in [0,1, 3, 4, 5, 6, 7, 8, 9]:
    rightbottom(num)
  if c in [0, 2, 3, 5, 6, 8, 9]:
    topbottom(num)
    
n = str(n)
arr = []

for c in n:
  num = limit()
  drawing(int(c), num)
  arr.append(num)
  
drawed = [[] for _ in range(2*s + 3)]

for i in range(0, 2*s + 3):
  for j in range(len(arr)):
    drawed[i] += arr[j][i]
    drawed[i].append(' ')
    
for c_arr in drawed:
  print(''.join(c_arr))