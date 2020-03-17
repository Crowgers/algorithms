import csv

from math import ceil


def prime_solver(max_num):
    """
    This method finds all primes between 1 and max_num.
    :param max_num: [INT] maximum number to check
    :return: [LIST] of [INT] List of prime integers
    """
    if (max_num - 1) % 2 is 0:
        num_list = [False, True]*(max_num//2) + [False]
    else:
        num_list = [False, True]*(max_num//2)
    num_list[1], num_list[2] = False, True

    # Loops start at 3 steps of 2 finished at square root n
    for i in range(3, int(ceil(1 + max_num**0.5)), 2):
        if num_list[i]:
            num_list[i*i::2*i] = [False]*int((max_num + 2*i - 1 - i*i) / (2*i))
    return [x for x in range(max_num) if num_list[x]]


def get_confirmed_primes():
    """
    Gets mathematically confirmed primes from file (up to 1 million)
    :return: [LIST] of [INT]
    """
    with open('first-1000000-primes.csv', 'r') as prime_file:
        return [int(item) for row in csv.reader(prime_file, delimiter=',')
                for item in row if item]


if __name__ == '__main__':
    print('Tests primes in a list of function')
    input_num = int(input('Provide a number under 1299710 to retrieve primes:'))
    found_primes = prime_solver(input_num)
    confirmed_primes = get_confirmed_primes()
    false_primes = [x for x in found_primes if x not in confirmed_primes]

    if len(false_primes) == 0:
        print(f'Primes: {found_primes}')
        print(f'Primes match confirmed list: \'{len(false_primes) == 0}\'')
    else:
        print(f'False primes detected: {false_primes}')
