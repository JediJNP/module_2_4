print('Всё не так уж просто')
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in numbers:
    is_prime = True
    for j in range(2 , i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime == False:
        not_primes.append(i)
    else:
        primes.append(i)
if 1 in primes:
    primes.remove(1)


print(primes)
print(not_primes)

#numbers [1 : numbers.index(i)]