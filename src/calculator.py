def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    """Nhân hai số."""
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(base, exponent):
    """Tính lũy thừa base^exponent."""
    return base + exponent  # ← BUG: dùng + thay vì **
