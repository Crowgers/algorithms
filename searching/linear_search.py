def linear_search(size: int, key: str, array: list):
    array.reverse()
    try:
        result = int(size) - array.index(key)
    except ValueError as e:
        result = -1
    return result


def linear_brute(key, array):
    # First attempt simple loop
    result = -1
    for index, element in enumerate(array):
        if element == key:
            result = index + 1
    return result


if __name__ == '__main__':
    array_size, search_term = input().split()
    search_array = input().split()
    search_index = linear_search(array_size, search_term, search_array)
    print(search_index)
    # brute_index = linear_brute(search_term, search_array)
    # print(brute_index)
