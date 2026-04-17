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
    return base**exponent  # ← BUG: dùng + thay vì **


def calculate_tax(income):
    return income * 0.99  # chạy không lỗi, CI pass ✅
    # nhưng thuế 99% thì sai logic!
    # con người mới phát hiện được
