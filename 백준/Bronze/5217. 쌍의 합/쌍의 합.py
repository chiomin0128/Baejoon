count = int(input())

for _ in range(count):
    n = int(input())
    pairs = []
    
    for i in range(1, n):
        j = n - i
        if i < j:
            pairs.append((i, j))
    
    print(f"Pairs for {n}:", end="")
    
    if pairs:
        print(" ", end="")
        print(", ".join(f"{a} {b}" for a, b in pairs))
    else:
        print()