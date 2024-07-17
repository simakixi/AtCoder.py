N,K,X = map(int,input().split())
A = input().split()
A.insert(K,X)
print(*A)