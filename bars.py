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


def print_bars(smallest_bar, biggest_bar, closest_bar):
    print('{} {}'.format('Самый большой бар в Москве:',
                         biggest_bar['properties']['Attributes']['Name']
                         ))
    print('{} {}'.format('Самый маленький бар в Москве:',
                         smallest_bar['properties']['Attributes']['Name']
                         ))
    print('{} {}'.format('Самый ближайший к вам бар:',
                         closest_bar['properties']['Attributes']['Name']
                         ))



if __name__ == '__main__':
    try:
        file_path = sys.argv[1]
        json_decoded = load_data(file_path)
    except FileNotFoundError:
        sys.exit('Файл не найден, попробуйте еще раз.')
    except IndexError:
        sys.exit('Используйте синтаксис: "python bars.py <filename>"')
    bars = json_decoded['features']
    biggest_bar = get_biggest_bar(bars)
    smallest_bar = get_smallest_bar(bars)
    try:
        latitude = float(input('Введите вашу широту:'))
        longitude = float(input('Введите вашу долготу:'))
    except ValueError:
        sys.exit('Не были введены координаты.')
    closest_bar = get_closest_bar(bars, latitude, longitude)
    print_bars(smallest_bar, biggest_bar, closest_bar)