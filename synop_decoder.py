
class Decoder:

    def __init__(self, date, data, group_dict):
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
            self.air_temperature_value = group_dict[1][1:]
        if 2 in group_dict:
            self.dew_temperature_sign = group_dict[2][0]
            self.dew_temperature_value = group_dict[2][1:]
        if 3 in group_dict:
            self.air_pressure_station_lvl = group_dict[3]
        if 4 in group_dict:
            self.air_pressure_sea_lvl = group_dict[4]
        if 5 in group_dict:
            self.three_hour_pressure_tendency = group_dict[5][0]
            self.three_hour_press_actual_change = group_dict[5][1:]
        if 6 in group_dict:
            self.precipitation_amount = group_dict[6][:3]
            self.precipitation_time = group_dict[6][3]
        if 7 in group_dict:
            self.present_weather = group_dict[7][:2]
            self.past_weather = group_dict[7][2:]
        if 8 in group_dict:
            self.amount_low_clouds = group_dict[8][0]
            self.low_clouds_type = group_dict[8][1]
            self.medium_clouds_type = group_dict[8][2]
            self.high_clouds_type = group_dict[8][3]
        if 9 in group_dict:
            self.observation_time = group_dict[9]

    def info(self):
        pass



