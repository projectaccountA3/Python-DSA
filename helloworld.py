print ("Hello world")

def calculator(a,b,operation):
    match operation:
        case "+":
            return a+b
        case "-":
            return a-b
        case "*":
            return a*b
        case "/":
            return a/b

x=0
y=0
operation=" "

print("enter two numbers",x,y,operation)
x=int(input("enter first number: "))
y=int(input("enter second number: "))
operation=input("enter operation (+,-,*,/): ")
print(calculator(x,y,operation))


num=1
print(f"{num:03d}")


print(f"{7:03d}")

print(f"{45:05d}")

for i in range(1,11):
    print(f"{i:03d}")

nums = [1, 3, 9, 15]
num2=[]
for i in nums:
    num2.append(f"{i:03d}")

print(num2)

for i in range(1,13):
    print(f"EMP{i:04d}")


Score=int(input("Enter your score: "))
print(f"LEVEL-{Score:d}")

min=int(input("Enter min value: "))
sec=int(input("Enter sec value: "))
print(f"{min:02d}:{sec:02d}")


for i in range(1,21):
    print(f"EMP{i:03d}")

