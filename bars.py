import json
import sys
from math import sqrt


def load_data(file_path):
    with open(file_path, encoding='utf-8') as file_object:
        json_content = file_object.read()
        json_decoded = json.loads(json_content)
    return json_decoded


def get_biggest_bar(bars):
    biggest_bar = max(
        bars,
        key=lambda bar: bar['properties']['Attributes']['SeatsCount']
    )
    return biggest_bar


def get_smallest_bar(bars):
    smallest_bar = min(
        bars,
        key=lambda bar: bar['properties']['Attributes']['SeatsCount']
    )
    return smallest_bar


def get_closest_bar(bars, latitude, longitude):
    closest_bar = min(
        bars,
        key=lambda bar: sqrt((bar['geometry']['coordinates'][0] - latitude) ** 2 +
                             (bar['geometry']['coordinates'][1] - longitude) ** 2
                             )
    )
    return closest_bar


def input_coordinates():
    try:
        latitude = float(input('Введите вашу широту:'))
        longitude = float(input('Введите вашу долготу:'))
        return latitude, longitude
    except ValueError:
        print('Не были введены координаты.')
        return None, None


def what_to_print(bars):
    bar_type = input('Введите тип бара, который вам нужен(большой, маленький, ближайший):')
    if bar_type == 'большой':
        bar = get_biggest_bar(bars)
    elif bar_type == 'маленький':
        bar = get_smallest_bar(bars)
    elif bar_type == 'ближайший':
        latitude, longitude = input_coordinates()
        if any([latitude, longitude]):
            bar = get_closest_bar(bars, latitude, longitude)
        else:
            bar = None
    else:
        print('Был неправильно введен тип бара, нужно было написать четко большой, маленький или ближайший')
        bar = None
    return bar, bar_type


def print_bars(bar, bar_type):
    if bar is not None:
        print('{} {} {} {}'.format('Самый',
                                   bar_type,
                                   'бар в Москве:',
                                   bar['properties']['Attributes']['Name']
                                   ))
    else:
        print('Попробуйте еще раз.')


if __name__ == '__main__':
    try:
        file_path = sys.argv[1]
        json_decoded = load_data(file_path)
    except FileNotFoundError:
        sys.exit('Файл не найден, попробуйте еще раз.')
    except IndexError:
        sys.exit('Используйте синтаксис: "python bars.py <filename>"')
    bars = json_decoded['features']
    try:
        bar, bar_type = what_to_print(bars)
    except UnboundLocalError:
        sys.exit()
    print_bars(bar, bar_type)
