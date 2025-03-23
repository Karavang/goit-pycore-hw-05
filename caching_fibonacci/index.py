from functools import lru_cache


def caching_fibonacci(n):
    @lru_cache(maxsize=None)
    def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    fibonacci.cache_clear()
    return fibonacci(n)


print(caching_fibonacci(10))
