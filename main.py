from synop_decoder import *
from collections import defaultdict

if __name__ == '__main__':
    input_date = ['2022', '07', '27', '06', '00']
    with open('input1.txt') as file:
        i = 0
        for line in file:
            line, _, _ = line.partition('333')
            data = line.strip().split()
            date = data[0].split(',')
            group_dict = defaultdict(str)
            for group in data[5:]:
                group_dict[int(group[0])] = group[1:]
            print(i, data[1:])
            i += 1
            if date[1:6] == input_date:
                decode = Decoder(date, data[1:], group_dict)
                decode.info()

    print(decode.weather_station)
    print(data[3][3:5])
    print(data[5:])

    # print(group_dict)
    # for i in range(1, 10):
    #     if i in group_dict:
    #         print(f'Group {i} exist: {group_dict[i]}')
    #     elif i not in group_dict:
    #         print(f'Group {i} does not exist')

    # data = data[1:]
    # print(data)
    # print(data[0])
    # print(f'stacja: {date[0]}')
    # print(f'data: {date[1:6]}')
    # print(f'rodzaj stacji: {date[6]}')
    #
    # print(f'{data[1][:2]}')













