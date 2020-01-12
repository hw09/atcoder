A, B, C = map(int, input().split())

container1 = A - B
container2 = C - container1

print(container2 if container2 >= 0 else 0)