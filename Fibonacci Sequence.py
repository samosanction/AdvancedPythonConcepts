# Here is an example generator which calculates fibonacci numbers:
# generator version
def fib(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        temp = a
        a = b
        b = temp + a


for items in fib(80):
    print(items)

# Using Range
def fib2(number):
    a = 0
    b = 1
    result = []
    for i in range(number):
        result.append(a)
        temp = a
        a = b
        b = temp + b
    return result


# print(fib2(100))
