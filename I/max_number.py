import sys


def load_data(file_path):
    file = open(file_path, 'r')
    data = file.readlines()[0].split(';')
    return [float(num) for num in data]


numbers_array = load_data('./max_numbers_data.txt')

max_number = sys.float_info.min  # ustawienie najmniejszej możliwej wartości na max_number

for number in numbers_array:
    if number > max_number:
        max_number = number

print(f'max: {max_number}')
