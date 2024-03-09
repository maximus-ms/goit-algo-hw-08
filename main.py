import heapq
from numpy import random

cables = list(random.randint(100, size=random.randint(64)))
heapq.heapify(cables)
cost = 0

print(f"All cables ({len(cables)} parts): {cables} ")
print(f"We expect to get a cable with length: {sum(cables)}")

for _ in range(len(cables) - 1):
    new_cable = heapq.heappop(cables) + heapq.heappop(cables)
    heapq.heappush(cables, new_cable)
    cost += new_cable

print(f"We got a cable with length: {cables[0]}")
print(f"Total cost: {cost}")
