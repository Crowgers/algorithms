def odd_numbers(lower, upper):
    """
    Returns a list of odd numbers between an upper and lower bound
    :param lower: [INT] Lower bound
    :param upper: [INT] Upper bound
    :return: [LIST] of [INT]'s
    """
    if lower % 2 == 0:
        first = lower + 1
    else:
        first = lower

    if upper % 2 == 0:
        last = upper - 1
    else:
        last = upper

    if lower == upper & lower // 2 != 0:
        return lower

    return [x for x in range(first, last + 1, 2)]


if __name__ == '__main__':
    print(odd_numbers(2, 5))
