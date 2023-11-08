N=int(input())
for i in range(N):
    L=list(map(int,input().split()))
    L.remove(max(L))
    print(max(L))
