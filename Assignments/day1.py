"""
Fuel required to launch a given module is based on its mass.
Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.

fuel = mass / 3 -> round down - 2
"""


def read_data(file_name):
    with open(f'../Puzzle_inputs/{file_name}.txt') as f:
        data = f.read().splitlines()

    data = [int(x) for x in data]

    return data


def calculate_fuel(mass):

    fuel = int(mass / 3) - 2

    return fuel


def sum_all_fuels():

    data = read_data('day1')
    fuels = [calculate_fuel(mass) for mass in data]

    return sum(fuels)


print(sum_all_fuels())
