"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать функцию, которая возвращает длину множество
"""


def set_length(collection: set) -> int:
    len_res = len(collection)
    result = len_res
    return result


if __name__ == '__main__':
    assert set_length({1, 2, 3, 4}) == 4
    print('Решено!')
