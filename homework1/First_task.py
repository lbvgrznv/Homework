import sys


def get_value (name_of_input_value, is_enter_input_supported = False):
    is_valid = False
    while not is_valid:
        number_input = input("Введите %s: " % name_of_input_value)
        if is_enter_input_supported and number_input == '':
            num = sys.maxsize
            is_valid = True
            break
        try:
            num = int(number_input)
            is_valid = True
        except ValueError:
            print("Попробуйте ещё раз")
    return num


start = get_value("начало диапазона")
stop = get_value("конец диапазона", True)
step = get_value("шаг")
range_ = []
while start <= stop:
    range_.append(start)
    start += step
print(range_)
