import json

# 1
def squares_gen(N):
    for i in range(1, N + 1):
        yield i ** 2

# 2
N = 10
squares_list = list(squares_gen(N))
squares_json = json.dumps(squares_list)

print("Squares in:", squares_json)

# 3
def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

n = int(input("Enter a number for even generator: "))
even_list = list(even_numbers(n))

# 4
even_json = json.dumps(even_list)
print("Even numbers:", even_json)

# 5
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

divisible_list = list(divisible_by_3_and_4(50))
print("Numbers divisible by 3 and 4:", json.dumps(divisible_list))

# 6
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

countdown_list = list(countdown(10))
print("Countdown numbers:", json.dumps(countdown_list))
