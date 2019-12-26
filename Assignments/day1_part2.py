from day1 import read_data, calculate_fuel


def calculate_corrected_fuel(filename):

    data = read_data(filename)

    all_fuels = []
    for mass in data:
        total_fuel = 0

        while mass > 0:
            fuel = calculate_fuel(mass)
            if fuel < 0:
                fuel = 0
            total_fuel += fuel
            mass = fuel
        all_fuels.append(total_fuel)

    return sum(all_fuels)


total_fuel = calculate_corrected_fuel('day1')

print(total_fuel)
