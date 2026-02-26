# a=[1,2,3,4,5,6,7,8,9,10]
# l=len(a)
# index=0
# def itearatter(a):
#     l=len(a)
#     index=0
#     for i in range(l):
#         if i<l:
#             b=int(input("enter the element to be inserted: "))
#             a[index]=b
#             index+=1
#             print(a)
#         else:
#             index=0
#             itearatter(a)

# itearatter(a)

a = [1,2,3,4,5,6,7,8,9,10]
n = len(a)
index = 0

# while True:
#     b = int(input("Enter element to insert: "))
#     a[index % n] = b
#     print(a)
#     index += 1

while True:
    b= int(input("Enter element to insert: "))
    a[index] = b
    print(a)
    index+=1
    if index==n:
        index=0

        
