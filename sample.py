def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Hardcoded limit
for num in range(2, 21):  # Prints primes up to 20
    if is_prime(num):
        print(num)
