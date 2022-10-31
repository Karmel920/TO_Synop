from tables import *


class Decoder:

    def __init__(self, date: list, data: list, group_dict: dict):
        self.weather_station = date[0]
        self.date = date[1:6]
        self.station_type = date[6]
        self.wind_indicator = data[0][-1]
        self.rain_group_indicator = data[2][0]
        self.station_type = data[2][1]
        self.height_lowest_cloud = data[2][2]
        self.horizontal_visibility = data[2][3:5]
        self.total_cloud_cover = data[3][0]
        self.wind_direction = data[3][1:3]
        self.wind_speed = data[3][3:5]
        if 1 in group_dict:
            self.air_temperature_sign = group_dict[1][0]
            self.air_temperature_value = group_dict[1][1:5]
        if 2 in group_dict:
            self.dew_temperature_sign = group_dict[2][0]
            self.dew_temperature_value = group_dict[2][1:5]
        if 3 in group_dict:
            self.air_pressure_station_lvl = group_dict[3]
        if 4 in group_dict:
            self.air_pressure_sea_lvl = group_dict[4]
        if 5 in group_dict:
            self.three_hour_pressure_tendency = group_dict[5][0]
            self.three_hour_press_actual_change = group_dict[5][1:5]
        if 6 in group_dict:
            self.precipitation_amount = group_dict[6][:3]
            self.precipitation_time = group_dict[6][3]
        if 7 in group_dict:
            self.present_weather = group_dict[7][:2]
            self.past_weather = group_dict[7][2:5]
        if 8 in group_dict:
            self.amount_low_clouds = group_dict[8][0]
            self.low_clouds_type = group_dict[8][1]
            self.medium_clouds_type = group_dict[8][2]
            self.high_clouds_type = group_dict[8][3]
        if 9 in group_dict:
            self.observation_time = group_dict[9][:5]
        self.group_list = list(group_dict.keys())

    def info(self):
        """Print decoded info from synop"""
        table = Table()
        print(f'\nData: {self.date[0]}-{self.date[1]}-{self.date[2]} {self.date[3]}:{self.date[4]}'
              f'\t Kraj: {table.get_country(int(self.weather_station[:2]))} \tNumer stacji: {self.weather_station[2:]}'
              f'\tTyp stacji: {table.get_station_type(int(self.station_type))} \nOpad: {table.get_rain_indicator(int(self.rain_group_indicator))}'
              f'\tWysokosc wzgledna podstawy najnizszych chmur: {table.get_height_lowest_cloud(self.height_lowest_cloud)}'
              f'\t Widzialnosc pozioma: {table.get_horizontal_visibility(self.horizontal_visibility)}'
              f'\nZachmurzenie nieba: {table.get_total_cloud_cover(self.total_cloud_cover)}'
              f'\tKierunek wiatru: {table.get_wind_direction(self.wind_direction)} '
              f'\tPredkosc wiatru: {table.get_wind_speed(int(self.wind_speed), int(self.wind_indicator))}'
              f'\nTemperatura powietrza: {table.get_temperature(int(self.air_temperature_sign), int(self.air_temperature_value))}'
              f'\tTemperatura punktu rosy: {table.get_temperature(int(self.dew_temperature_sign), int(self.dew_temperature_value))}'
              f'\nCisnienie na poziomie stacji: {table.get_pressure(int(self.air_pressure_station_lvl))}'
              f'\tCisnienie na poziomie morza: {table.get_pressure(int(self.air_pressure_sea_lvl))}'
              f'\nTendencja cisnienia: {table.get_pressure_tendency(int(self.three_hour_pressure_tendency), int(self.three_hour_press_actual_change))}')
        if 6 in self.group_list:
            print(f'Suma opadu: {table.get_precipitation_amount(int(self.precipitation_amount))}'
                  f'\tCzas trwania opadu: {table.get_precipitation_time(int(self.precipitation_time))}')
        if 7 in self.group_list:
            fname = ''
            if table.get_station_type(int(self.station_type)) == 'stacja automatyczna':
                fname = 'weather_present_auto.txt'
            if table.get_station_type(int(self.station_type)) == 'stacja nieautomatyczna':
                fname = 'weather_present_non_auto.txt'
            with open(fname) as file:
                for line in file:
                    index, _, text = line.strip().partition('-')
                    if int(index) == int(self.present_weather):
                        print(f'Pogoda biezaca: {text.strip()}')
            print(f'Pogoda ubiegla: {table.get_weather_past(self.past_weather)}')
        if 8 in self.group_list:
            print(f'Rodzaj chmur pietra niskiego: {table.get_low_clouds(self.low_clouds_type)}')
            print(f'Rodzaj chmur pietra sredniego: {table.get_medium_clouds(self.medium_clouds_type)}')
            print(f'Rodzaj chmur pietra wysokiego: {table.get_high_clouds(self.high_clouds_type)}')
        if 9 in self.group_list:
            print(f'Godzina obserwacji{self.observation_time[:2]}:{self.observation_time[2:4]} UTC')



