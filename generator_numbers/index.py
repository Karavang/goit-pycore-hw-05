from re import findall

gen = 0
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."


def generator_numbers(text: str):
    global gen
    index = gen
    gen = gen + 1
    try:
        yield float(findall(r"\d+\.\d+", text)[index])
    except IndexError:
        yield "No more numbers"


def sum_profit(text: str, func):
    ints = set()
    gena = next(func(text))
    while not gena == "No more numbers":
        ints.add(gena)
        gena = next(func(text))
    return sum(ints)


print(sum_profit(text, generator_numbers))
