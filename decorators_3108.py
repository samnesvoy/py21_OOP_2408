import random
import time


def simple(num: int):
    for i in range(2, num // 2 + 1):
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
# r=performance(simple_range)
# r(3,567)

income = [random.randrange(1000, 5000) for i in range(30)]
consumption = [random.randrange(1000, 5000) for i in range(30)]


def month_report_for_samiy_glavniy_director(fun):
    def decor():
        res = ' Уважаемый самый главный директор, вот ваам отчет\n'
        res += fun()
        return res

    return decor


def month_report_all(fun):
    def decor():
        res = fun()
        res += f'Сумма' \
               f' - Доход: {sum(income)}' \
               f' - Расход: {sum(consumption)}' \
               f' - Итого: {sum(income) - sum(consumption)}\n'
        return res

    return decor

@month_report_for_samiy_glavniy_director
@month_report_all
def month_report(income=income, consumption=consumption):
    report = ''
    for i in range(30):
        report += f'День {i + 1}' \
                  f' - Доход: {income[i]}' \
                  f' - Расход: {consumption[i]}' \
                  f' - Прибыль:{income[i] - consumption[i]}\n'

    return report


# m = month_report_all(month_report)

print(month_report())
# mm=month_report_for_samiy_glavniy_director(m)
# print(mm())
