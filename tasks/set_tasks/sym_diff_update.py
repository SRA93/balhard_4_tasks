"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать функцию, которая оставит в множестве те элементы, которые есть в
обоих множествах, кроме общих
"""


def sym_diff_update(set_1: set, set_2: set) -> set:
    set.symmetric_difference_update(set_1, set_2)
    return set_1


if __name__ == '__main__':
    some_set = {1, 2, 3, 4}
    sym_diff_update(some_set, {3, 4, 5})
    assert some_set == {1, 2, 5}
    print('Решено!')
