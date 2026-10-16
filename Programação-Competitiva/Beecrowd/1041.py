//Runtime error

X = float(input())
Y = float(input())

if X == Y and Y == 0:
    print("Origem")
elif X == 0 and Y != 0:
    print("Eixo Y")
elif Y == 0 and X != 0:
    print("Eixo X")

if X > 0:
    if Y > 0:
        print("Q1")
    if Y < 0:
        print("Q4")
        
if X < 0:
    if Y > 0:
        print("Q2")
    if Y < 0:
        print("Q3")