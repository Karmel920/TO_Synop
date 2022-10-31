from synop_decoder import *
from date import *
from collections import defaultdict

if __name__ == '__main__':
    print("Dekodowanie depesz SYNOP")
    print('Podaj date z ktorej chcesz otrzymac informacje')
    date_list = Date()
    input_date = ['2022', '07', '27', '06', '00']

    with open('input.txt') as file:
        i = 0
        for line in file:
            line, _, _ = line.partition('333')
            data = line.strip().split()
            date = data[0].split(',')
            group_dict = defaultdict(str)
            for group in data[5:]:
                group_dict[int(group[0])] = group[1:]
            if date[1:6] == date_list.get_date_list():
                decode = Decoder(date, data[1:], group_dict)
                decode.info()
