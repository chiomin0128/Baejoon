from itertools import combinations

def chicken_distance(city, chickens):
    total_distance = 0
    for r, row in enumerate(city):
        for c, cell in enumerate(row):
            if cell == 1:  
                min_dist = float('inf')
                for chicken in chickens:
                    dist = abs(r - chicken[0]) + abs(c - chicken[1])
                    min_dist = min(min_dist, dist)
                total_distance += min_dist
    return total_distance

N, M = map(int, input().split())
city = []
chicken_houses = []
for _ in range(N):
    city.append(list(map(int, input().split())))
    for c in range(N):
        if city[-1][c] == 2:
            chicken_houses.append((len(city) - 1, c))

min_distance = float('inf')
for selected_chickens in combinations(chicken_houses, M):
    min_distance = min(min_distance, chicken_distance(city, selected_chickens))

print(min_distance)
