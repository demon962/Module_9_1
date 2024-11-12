def apply_all_func(numbers, *functions):
    results = {}
    for func in functions:
        results[func.__name__] = func(numbers)
    return results

# Примеры использования функции
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
