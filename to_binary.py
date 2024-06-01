powers_of_two = []

def largest_power_of_two(decimal_number):
    i = 0
    while True:
        power_of_two = 2 ** i
        powers_of_two.append(power_of_two)
        if power_of_two > decimal_number:
            break
        i += 1
    return i - 1


def binary_converter(decimal_number):
    powers = []
    while decimal_number > 0:
        power = largest_power_of_two(decimal_number)
        powers.append(power)
        decimal_number -= 2 ** power
    largest_power = max(powers)
    result = ""
    while largest_power >= 0:
        if largest_power in powers:
            result += "1"
        else:
            result += "0"
        largest_power -= 1
    return result

# The tests for the function
assert binary_converter(19) == "10011"
assert binary_converter(56) == "111000"