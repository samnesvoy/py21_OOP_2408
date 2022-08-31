import time


def simple(num: int):
    for i in range(2, num//2+1):
        if num % i == 0:
            return False
    return True


def simple_range(a=1, b=1000):
    li = []
    for i in range(a, b + 1):
        if simple(i):
            li.append(i)
    return li


def performance(fun):
    def decor_fun(*args):
        start = time.time()
        res = fun(*args)
        end = time.time()
        print(f'Simple numbers: {res}\nPerformance: {end - start}')

    return decor_fun


# print(simple_range())

# performance_simple_range = performance(simple_range)
# performance_simple_range()


def range_change(fun):
    def decor(a, b):
        return fun(a, b)

    return decor

# res =range_change(simple_range)

# print(res(3,277))
r=performance(simple_range)
r(3,567)