import bisect as b
case = 0

while True:
  numeros = []
  
  N, Q = map(int, input().split())
  if N == 0 and Q == 0:
    break
  case +=1
  print(f"CASE# {case}:")
  
  for c in range(N):
    numeros.append(int(input()))

  numeros.sort()
  
  for c in range(Q):
    n = int(input())
    index = b.bisect_left(numeros, n)
    
    if index == len(numeros) or numeros[index] != n:
      print(n, "not found")
    else:
      print(f"{n} found at {index + 1}")
