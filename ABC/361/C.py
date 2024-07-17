N,K = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
print(min([A[i]-A[i-(N-K)+1] for i in range((N-K)-1,N)]))