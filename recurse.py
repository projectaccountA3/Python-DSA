def recurse(n,s):
    if n==0:
        print(s)
    else:
        count=0
        count+=1
        print(count)
        recurse(n-1,n+s)

recurse(-1,0)