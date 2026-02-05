def safe_sqrt(x):
    if x < 0:
        raise ValueError("Negative number not allowed")
    return x ** 0.5



try:
    print(safe_sqrt(-5))
except ValueError as e:
    print(e)