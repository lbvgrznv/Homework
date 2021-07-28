ticket_number = input("Введите номер билетика: ")
middle = len(ticket_number)/2
left_part = 0
right_part = 0
for i in range(0, len(ticket_number)):
    if i < middle:
        left_part += int(ticket_number[i])
    else:
        right_part += int(ticket_number[i])
if left_part == right_part:
    print("Сегодня тебе повезло!")
else:
    print("В этот раз не повезло. Но можно попробовать ещё раз!")