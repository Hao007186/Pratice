from collections import deque

k=deque()
k.append(1)
k.append(2)
k.append(3)
k.append(4)
k.popleft()
print(k)