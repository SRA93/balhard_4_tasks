"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать функцию, которая оставит в множестве только те элементы,
которые есть только в первом множестве и нет во втором
"""


def diff_update(set_1: set, set_2: set) -> set:
    set_new = set.difference_update(set_1, set_2)
    result = set_new
    return result


if __name__ == '__main__':
    some_set = {1, 2, 3, 4}
    diff_update(some_set, {3, 4, 5})
    assert some_set == {1, 2}
    print('Решено!')
