def format_price(value: int, suffix: str = "원") -> str:
    return f"{int(value):,}{suffix}"