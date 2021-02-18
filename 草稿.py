def f(x):
    for i in x:
        yield i

for i in f([1,2]):
    print(i)