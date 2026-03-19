from .data import get_random_joke

def joke():
    return get_random_joke()

def jokes(count=1):
    return [get_random_joke() for _ in range(count)]