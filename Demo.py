list1=[1,2,3,1]
count=0
for i in list1:
    if list1.count(i)>1:
        count+=1
    if count>0:
        print("True")
    else:
        print("False")

        
    
