import time

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def calculate_primes(limit):
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

start_time = time.time()
limit = 10_000_000  # Set a high number for a challenging calculation
primes = calculate_primes(limit)
end_time = time.time()

print(f"Calculated {len(primes):,} prime numbers up to {limit:,}.")
print(f"Time taken: {end_time - start_time:.2f} seconds.")
