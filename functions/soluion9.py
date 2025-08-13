def generator(numbers):
    for i in range(2, numbers+1, 2):
        yield i


for i in generator(10):
    print(i)