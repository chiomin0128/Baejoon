


a = 1;
M = int(input())

for _ in range(M):
    X, Y = map(int, input().split())
    if a == X:
        a = Y
    elif a == Y:
        a = X

print(a)