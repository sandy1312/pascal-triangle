n=int(input())
for i in range(1,n+1):
    f = 1
    for j in range(1,i+1):
        print(f,end=" ")
        f = int(f * (i - j) / j)
    print("\n")