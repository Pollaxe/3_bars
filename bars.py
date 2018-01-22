import json
import sys
from math import sqrt


def load_data(file_path):
    with open(file_path, encoding='utf-8') as content:
        json_content = content.read()
        bars = json.loads(json_content)
    return bars


def get_biggest_bar(bars):
    biggest_bar = max(bars,
                      key=lambda bar:
                      bar['properties']['Attributes']['SeatsCount']
                      )
    return biggest_bar


def get_smallest_bar(bars):
    smallest_bar = min(bars,
                       key=lambda bar:
                       bar['properties']['Attributes']['SeatsCount']
                       )
    return smallest_bar


def get_closest_bar(bars, latitude, longitude):
    closest_bar = min(bars,
                      key=lambda coords:
                      sqrt((
                        coords['geometry']['coordinates'][0] - latitude) ** 2 +
                        (coords['geometry']['coordinates'][1] - longitude) ** 2
                        )
                      )
    return closest_bar


if __name__ == '__main__':
    try:
        file_path = sys.argv[1]
        bars = load_data(file_path)
    except FileNotFoundError:
        print('Файл не найден, попробуйте еще раз.')
        sys.exit()
    except IndexError:
        print('Используйте синтакс: "python bars.py <filename>"')
        sys.exit()
    bars = bars['features']
    biggest_bar = get_biggest_bar(bars)
    smallest_bar = get_smallest_bar(bars)
    print('{} {}'.format('Самый большой бар в Москве:', biggest_bar['properties']['Attributes']['Name']))
    print('{} {}'.format('Самый маленький бар в Москве:', smallest_bar['properties']['Attributes']['Name']))
    try:
        latitude = float(input('Введите вашу широту:'))
        longitude = float(input('Введите вашу долготу:'))
        closest_bar = get_closest_bar(bars, latitude, longitude)
        print('{} {}'.format('Самый ближайший к вам бар:', closest_bar['properties']['Attributes']['Name']))
    except ValueError:
        print('Не были введены координаты.')
        sys.exit()
