
def fib(num):
    a = 0
    b = 1
    list_1=[a,b]
    for i in range(num-2):
        new=a+b
        list_1.append(new)
        a=b
        b=new
    print(list_1)

print('hello world')

var1 = int(input("Please enter an integer value:"))
print(var1)

fib(var1)


