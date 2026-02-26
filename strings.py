# # x=y=1
# # print(f"x={x}, y={y}")

# #finding the vowels count in the list of words

# words = ["apple", "banana", "sky", "education"]
# count=0
# l1=[]
# for w in words:
#     l=len(w)
#     for j in range(0,l):
#         if w[j] in "aeiou":
#             count+=1
#     l1.append(count)
#     count=0
# print(l1)

# #conevrting strings to uppercase

# words = ["hi", "hello", "python"]
# w=[]

# # for i in words:
# #     w.append(i.upper())
# # print(w)

# for ch in words:
#     chars=[]
#     for c in ch:
#         if 'a' <= c <='z':
#             chars.append(chr(ord(c)-32))
#         else:
#             chars.append(c)
#     w.append("".join(chars))
# print(w)

# #finding maximum length of the string in the list

# #method 1
# words = ["cat", "elephant", "dog", "giraffe"]
# l=[]
# max=0
# # for w in words:
# #     l.append(len(w))
# # print(l)
# # for i in l:
# #     if i>max:
# #         max=i
# # print(max)

# #method 2


# for w in words:
#     if len(w)>max:
#         max=len(w)
# print(max)

k=["elephant", "giraffe"]
max_word=""
max=0
for w in k:
    if len(w)>max:
        max=len(w)
        max_word=w
print(max)
print(max_word)

m = ["abc", "hello", "python"]
rev=[]
for i in m:
    rev.append(i[::-1])
print(rev)

h= ["hi", "hello", "to", "python", "code"]
count=0
for w in h:
    if len(w)>3:
        count+=1
print(count)

s = ["apple", "banana", "apple", "orange", "banana"]
unique=[]
for w in s:
    if w not in unique:
        unique.append(w)
print(unique)

t = ["madam", "apple", "racecar", "python"]
rev=[]
for i in t:
    if i==i[::-1]:
        rev.append(i)
print(rev)

b="bbbcccaaabaa"






    






