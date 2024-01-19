#Count all prime nos and create new python list which contain prime numbers

def count_primes_in_list(numbers):
    primes = []

    for num in numbers:
        if num == 2:
            primes.append(num)
        else:
            is_prime = True
            for i in range(2, num):
                if num % i == 0:
                    is_prime = False
                    break

            if is_prime:
                print (num)
                primes.append(num)

    return len(primes)


z = [10, 501, 22, 37, 100, 999, 87, 351]
print (count_primes_in_list(z))