list1=[1,2,3,4,5,6,7,8,9,10]
rev=[]
l=len(list1)
for i in range((l-1),-1,-1):
    rev.append(list1[i])

print(rev)