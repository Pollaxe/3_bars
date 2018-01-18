import json
import sys
from math import sqrt


def load_data(file_path):
    json_content = open(file_path,
                        encoding='utf-8').read()
    return json_content


def get_biggest_bar(json_decoded):
    biggest_bar = max(json_decoded,
                      key=lambda qty: qty['properties']['Attributes']['SeatsCount']
                      )
    return biggest_bar


def get_smallest_bar(json_decoded):
    smallest_bar = min(json_decoded,
                       key=lambda qty: qty['properties']['Attributes']['SeatsCount']
                       )
    return smallest_bar


def get_closest_bar(json_decoded, latitude, longitude):
    closest_bar = min(json_decoded,
                      key=lambda coords: sqrt((coords['geometry']['coordinates'][0] - latitude) ** 2 +
                                              (coords['geometry']['coordinates'][1] - longitude) ** 2
                                              )
                      )
    return closest_bar


if __name__ == '__main__':
    try:
        file_path = sys.argv[1]
        json_content = load_data(file_path)
        json_decoded = json.loads(json_content)
        json_decoded = json_decoded['features']
        biggest_bar = get_biggest_bar(json_decoded)
        smallest_bar = get_smallest_bar(json_decoded)
        print('Biggest bar in Moscow is ' + biggest_bar['properties']['Attributes']['Name'])
        print('Smallest bar in Moscow is ' + smallest_bar['properties']['Attributes']['Name'])
        latitude = float(input('Please input your latitude:'))
        longitude = float(input('Please input your longitude:'))
        closest_bar = get_closest_bar(json_decoded, latitude, longitude)
        print('Closest bar in Moscow to you is ' + closest_bar['properties']['Attributes']['Name'])
    except IndexError:
        print('Please use syntax: "python bars.py <filename>"')
    except FileNotFoundError:
        print('File not found, please try again.')
