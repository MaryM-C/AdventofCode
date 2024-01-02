import regex as re

#Python Version 3.10

coordinates_pattern_1 = '[0-9]'
coordinates_pattern_2= '[0-9]|one|two|three|four|five|six|seven|eight|nine'

coordinates_dict = {
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9',
    "zero": '0'
}

def read_lines_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def convert_word_coordinates_to_digits(raw_calibration_values):
    calibration_digits = []

    for raw in raw_calibration_values:
        digit = coordinates_dict.get(raw, raw)
        calibration_digits.append(digit)

    return calibration_digits

def process_line(line, coordinates_pattern):
    as_digit = re.findall(coordinates_pattern, line, overlapped=True)

    raw_calibration_values = [as_digit[0], as_digit[-1]]

    #FROM 'eight' to 8
    calibration_digits = convert_word_coordinates_to_digits(raw_calibration_values)

    # FROM 1,1 TO 11
    calibration_as_str = ''.join(calibration_digits)
    
    #For Debugging Purposes
    print_each_line_together_with_calibration(line, calibration_as_str)

    return int(calibration_as_str)

def print_each_line_together_with_calibration(line, calibration_as_str):
    print("{} -> {}".format(line.strip(), calibration_as_str))


def sum_of_calibration_values(lines, calibration_pattern):
    total_sum = 0

    for count, line in enumerate(lines, start=1):
        calibration_value = process_line(line, calibration_pattern)
        total_sum += calibration_value

    return total_sum

if __name__ == "__main__":
    input_file_path = 'input.txt'
    lines = read_lines_from_file(input_file_path)
    sum_1 = sum_of_calibration_values(lines, coordinates_pattern_1)
    sum_2 = sum_of_calibration_values(lines, coordinates_pattern_2)
    print("Part 1 Sum: {} \nPart 2 Sum: {}".format(sum_1, sum_2))

