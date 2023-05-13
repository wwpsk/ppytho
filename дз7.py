import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Функція {func.__name__} виконалася за {execution_time} секунд.")
        return result
    return wrapper


@measure_time
def calculate_sum(n):

    sum_value = 0
    for i in range(1, n+1):
        sum_value += i
    return sum_value

# Тести для перевірки працездатності

# Тест 1: Обчислення суми чисел від 1 до 1000
result = calculate_sum(1000)
print(f"Результат: {result}")

# Тест 2: Обчислення суми чисел від 1 до 1000000
result = calculate_sum(1000000)
print(f"Результат: {result}")

# Тест 3: Обчислення суми чисел від 1 до 100000000
result = calculate_sum(100000000)
print(f"Результат: {result}")

# Тест 4: Обчислення суми чисел від 1 до 10^9
result = calculate_sum(10**9)
print(f"Результат: {result}")
