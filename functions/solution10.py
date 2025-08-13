def factorial(num):
    if num==0:
        return 1

    return num * factorial(num-1)


print(factorial(10))
print(factorial(14))
print(factorial(15))
print(factorial(19))
