a,b,c,d,e,f = map(int,input().split())
g,h,i,j,k,l = map(int,input().split())
print("YNeos"[not(i<f and c<l and h<e and b<k and g<d and a<j)::2])