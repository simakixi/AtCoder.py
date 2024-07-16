A = list(map(int, input().split()))
C = input()
A.pop(["Red","Green","Blue"].index(C))
print(min(A))