# def generators():
#     yield 3
#     yield 4
#     yield 5
#     yield 6
#
#
# gen = generators()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
#
# def programming_language():
#     yield 'C'
#     yield 'C++'
#     yield 'Python'
#     yield 'Java'
#
#
# language = programming_language()
#
# print(next(language))
# print(next(language))
# print(next(language))
# print(next(language))

def func():
    for i in range(1, 26):
        print(i ** 2)


# number = func()

# fibonacci with  generation
def fibonacci(n):
    a, b = 0, 1
    i = 0
    while i < n:
        yield a
        a, b = b, a + b
        i += 1


fibo = fibonacci(7)
# print(next(fibo))
