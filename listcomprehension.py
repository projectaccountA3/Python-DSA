# #finding even numbers

# from curses.ascii import isdigit


# list2=[1,2,3,4,5,6,7,8,9,10,11,12,131,234,748,555,367,890,345,678,901,2345,6789]
# print([x for x in list2 if x%2==0])

# #finding max elements in the list

# list3=[1,2,5,7,89,45,23]
# max=list3[0]

# for i in list3:
#     if i>max:
#         max=i
    
# print(max)

# #square of even numbers

# list4=[1,2,3,4,5,6,7,8,9,10]
# print([x**2 for x in list4 if x%2==0])

# #extract only integers

# a = [1, "a", 2, "b", 3.5, 4]
# print([x for x in a if isinstance(x, float) or isinstance(x, int)])

# #separate evn from odd numbers

# b=[1,2,3,4,5,6,7,8,9,10]

# #pair elements with index

# print([x for x in enumerate(b)])

# a1=[1,2,3,4,5]
# b1=[3,4,5,6,7]

# print([(x)for x in a1 for y in b1 if x==y])

# a=['abc','efg','hij','klm','nop']
# rev=[]
# for i in a:
#     rev.append(i[::-1])
# print(rev)


# #flatten a list

a = [1, [2,3], 4, [5,6]]
b=[]

for i in a:
    if isinstance(i,list):
        b.extend(i)
    else:
        b.append(i)

print(b)

a = [1, [2, [3, 4]]]
k=[]
for i in a:
    if isinstance(i,list):
        k.flatten(i)
    else:
        k.append(i)

print(k)

# l=[1,2,3]
# # l.append([4,5])
# l.extend([6,7])
# print(l)






