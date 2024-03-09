# GoITNeo Algo HW-8

## Task
There are several network cables of different lengths that need to be joined in pairs into one cable using connectors in a way that minimizes costs. The cost of connecting two cables is equal to their combined length, and the total cost is the sum of connecting all cables.
The task is to find the order of joining that minimizes the total cost.

### Solution
To minimize the cost we have to connect cables from the shortest pairs to the end. Do it iteratively and sum the cost of each connection. The easiest way to do it is to use a minimal heap.

So, we have such a short piece of code:
```python
import heapq
from numpy import random

cables = list(random.randint(100, size=random.randint(64)))
heapq.heapify(cables)
cost = 0

print(f"All cables ({len(cables)} parts): {cables} ")
print(f"We expect to get a cable length: {sum(cables)}")

for _ in range(len(cables)-1):
    new_cable = heapq.heappop(cables) + heapq.heappop(cables)
    heapq.heappush(cables, new_cable)
    cost += new_cable

print(f"We got a cable length: {cables[0]}")
print(f"Total cost: {cost}")
```
And the output:
```
All cables (18 parts): [4, 4, 13, 30, 38, 47, 51, 55, 56, 87, 52, 54, 68, 92, 95, 57, 55, 75]
We expect to get a cable with length: 933
We got a cable with length: 933
Total cost: 3710
```

## Conclusions
A heap structure is a very convenient method to make a priority queue. Module ```heapq``` provides functionality for a minimum-heap, but converting it to maximum-heap by inverting values is very easy.
