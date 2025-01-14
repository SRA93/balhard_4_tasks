"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Что за планета?
Нужно отредактировать функцию get_planet_name, которая принимает номер планеты
так, чтобы она возвращала название планеты

Планеты в порядке их удаления от слонца:
1) Меркурий
2) Венера
3) Земля
4) Марс
5) Юпитер
6) Сатурн
7) Уран
8) Нептун

ПРИМЕРЫ
--------------------------------------------------------------------------------
get_planet_name(3) -> 'Земля'
"""


def get_planet_name(planet_num: int) -> str:
    planets = {
        'Меркурий': (1, 1),
        'Венера': (2, 2),
        'Земля': (3, 3),
        'Марс': (4, 4),
        'Юпитер': (5, 5),
        'Сатурн': (6, 6),
        'Уран': (7, 7),
        'Нептун': (8, 8)}

    for key in planets.keys():
        if planet_num in planets[key]:
            return key


if __name__ == '__main__':

    planet = int(input('Введите номер планеты: '))
    print(f'Планета: {get_planet_name(planet)}')
