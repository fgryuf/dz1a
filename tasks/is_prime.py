__all__ = (
    'is_prime',
)
from math import sqrt

def is_prime(number: int) -> bool:
    prime = True
    if(number == 1) or (number == 0):
        return False

    for i in range(2 , int(sqrt(number) + 1)) :
        if number % i == 0 :
            prime = False
    return prime

print(is_prime(0))