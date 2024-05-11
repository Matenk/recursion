def test(n, *args, name='Serge', **kwargs):
    print(n, args, name, kwargs)
test(3, 1, 2, 3, 4, 5, numb=89118760747)
print()
def mult_func(n):
    if (n <= 1):
        return 1
    else:
        return n * mult_func(n-1)

print(mult_func(5))