# countries = {12: 'Polska'}
# wind_indicators = {0: 'm/s(wiatromierz Wilda lub szacowana', 1: 'm/s(anemometr)',
#                    3: 'wezlow(wiatromierz Wilda lub szacowana)', 4: 'wezlow(anemometr)'}

class Table:
    """Contains tables to decode synop numbers"""
    countries = {12: 'Polska'}
    wind_indicators = {0: 'm/s(wiatromierz Wilda lub szacowana', 1: 'm/s(anemometr)',
                       3: 'wezlow(wiatromierz Wilda lub szacowana)', 4: 'wezlow(anemometr)'}
    rain_indicators = {0: 'grupa opadowa w rozdziale 1 i 3', 1: 'grupa opadowa tylko w rozdziale 1',
                       2: 'grupa opadowa tylko w rozdziale 3', 3: 'grupa opadowa pominięta (opady nie wystąpiły)',
                       4: 'grupa opadowa pominięta (nie wykonywano pomiarów opadu)'}
    station_types = {1: 'stacja nieautomatyczna', 2: 'stacja nieautomatyczna', 3: 'stacja nieautomatyczna',
                     4: 'stacja automatyczna', 5: 'stacja automatyczna', 6: 'stacja automatyczna'}
    heights_lowest_clouds = {0: '0 do 50m', 1: '50 do 100m', 2: '100 do 200m', 3: '200 do 300m', 4: '300 do 600m',
                             5: '600 do 1000m', 6: '1000 do 1500m', 7: '1500 do 2000m', 8: '2000 do 2500m', 9: 'powyzej 2500m'}
    horizontal_visibility_range = {81: '35 km', 82: '40 km', 83: '45 km', 84: '50 km', 85: '55 km', 86: '60 km',
                                   87: '65 km', 88: '70 km', 89: '> 70 km',
                                   90: '< 0.05 km', 91: '0.05 - 0.2 km', 92: '0.2 - 0.5 km', 93: '0.5 - 1.0 km',
                                   94: '1.0 - 2.0 km', 95: '2.0 - 4.0 km', 96: '4.0 - 10.0 km', 97: '10.0 - 20.0 km',
                                   98: '20.0 - 50.0 km', 99: '> 50 km'}
    temperature_sign = {0: '+', 1: '-'}
    pressure_tendencies = {0: 'wzrost duzy, pozniej spadek maly', 1: 'wzrost, pozniej bez zmian', 2: 'wzrost',
                           3: 'spadek maly, pozniej wzrost duzy', 4: 'bez zmian', 5: 'spadek duzy, pozniej wzrost maly',
                           6: 'spadek duzy, pozniej bez zmian', 7: 'spadek', 8: 'wzrost maly, pozniej spadek duzy'}
    precipitation_amounts = {990: 'slad', 991: '0.1 mm', 992: '0.2 mm', 993: '0.3 mm', 994: '0.4 mm', 995: '0.5 mm',
                             996: '0.6 mm', 997: '0.7 mm', 998: '0.8 mm', 999: '0.9 mm'}
    precipitation_times = {1: '6 h', 2: '12 h', 3: '18 h', 4: '24 h', 5: '1 h', 6: '2 h', 7: '3 h', 8: '9 h', 9: '15 h'}
    weather_past = {0: 'bez istotnych zjawisk', 1: 'ograniczona widzialnosc', 2: 'zamiec', 3: 'mgla', 4: 'opad',
                    5: 'mzawka', 6: 'deszcz', 7: 'snieg', 8: 'opad przelotny', 9: 'burza'}
    low_clouds = {0: 'brak', 1: 'Cumulus humilis lub Cumulus fractus', 2: 'Cumulus mediocris lub congestus występujący sam lub z Cu hum lub Cu fra bądź też ze Stratocumulus',
                  3: 'Cumulonimbus calvus', 4: 'Stratocumulus cumulogenitus', 5: 'Stratocumulus', 6: 'Stratus nebulosus lub Stratus fractus',
                  7: 'Stratus fractus lub Cumulus fractus', 8: 'Cumulus i Stratocumulus', 9: 'Cumulonimbus capillatus'}
    medium_clouds = {0: 'brak', 1: 'Altostratus translucidus', 2: 'Altostratus opacus lub Nimbostratus', 3: 'Altocumulus translucidus na jednym poziomie',
                     4: 'lawice Altocumulus translucidus', 5: 'Altocumulus translucidus w pasmach', 6: 'Altocumulus cumulogenitus',
                     7: 'Altocumulus translucidus', 8: 'Altocumulus castellanus lub floccus', 9: 'Altocumulus na niebie o wyglądzie chaotycznym'}
    high_clouds = {0: 'brak', 1: 'Cirrus fibratus lub Cirrus uncinus', 2: 'Cirrus spissatus', 3: 'Cirrus spissatus cumulonimbogenitus',
                     4: 'Cirrus uncinus lub Cirrus fibratus', 5: 'Cirrus (w pasmach) i Cirrostratus lub sam Cirrostratus', 6: 'Cirrus (w pasmach) i Cirrostratus lub sam Cirrostratus',
                     7: 'Cirrostratus', 8: 'Cirrostratus ', 9: 'Cirrocumulus'}

    def get_country(self, number):
        return self.countries[number]

    def get_rain_indicator(self, number):
        return self.rain_indicators[number]

    def get_station_type(self, number):
        return self.station_types[number]

    def get_height_lowest_cloud(self, number):
        if number == '/':
            return 'nieznana'
        else:
            return self.heights_lowest_clouds[int(number)]

    def get_horizontal_visibility(self, number):
        if number == '//':
            return 'nieznana'
        number = int(number)
        if 0 <= number <= 50:
            return f'{number / 10} km'
        if 56 <= number <= 80:
            return f'{number - 50} km'
        if 81 <= number <= 99:
            return self.horizontal_visibility_range[number]

    def get_total_cloud_cover(self, number):
        if number == '/':
            return 'nieznane'
        if number == '9':
            return 'niebo niewidczone'
        number = int(number)
        if 0 <= number <= 8:
            return f'{number}/8'

    def get_wind_direction(self, number):
        if number == '//':
            return 'nieznany'
        if number == '00':
            return 'cisza'
        if number == '99':
            return 'zmienny lub z wielu kierunkow'
        if number == '36':
            return 'od 355 do 4 stopni'
        number = int(number)
        if 1 <= number <= 35:
            return f'od {5 + (number - 1) * 10} do {14 + (number - 1) * 10} stopni'

    def get_wind_speed(self, number, wind_indicator):
        return f'{number} {self.wind_indicators[wind_indicator]}'

    def get_temperature(self, temp_sign: int, temp_value: int):
        return f'{self.temperature_sign[temp_sign]}{temp_value / 10} st. C'

    def get_pressure(self, pressure: int):
        if pressure < 1000:
            return f'{(pressure+10000) / 10} hPa'
        return f'{pressure / 10} hPa'

    def get_pressure_tendency(self, press_tendency: int, actual_change: int):
        return f'{self.pressure_tendencies[press_tendency]},  wielkosc tendencji: {actual_change / 10} hPa'

    def get_precipitation_amount(self, p_amount: int):
        if 990 <= p_amount <= 999:
            return self.precipitation_amounts[p_amount]
        if 0 <= p_amount <= 988:
            return f'{p_amount} mm'
        if p_amount == 989:
            return f'{p_amount} i wiecej mm'

    def get_precipitation_time(self, p_time: int):
        return self.precipitation_times[p_time]

    def get_weather_past(self, number):
        if number == '//':
            return 'brak'
        return f'{self.weather_past[int(number[0])]}, {self.weather_past[int(number[1])]}'

    def get_low_clouds(self, number):
        if number == '/':
            return 'chmury nie byly widoczne'
        return self.low_clouds[int(number)]

    def get_medium_clouds(self, number):
        if number == '/':
            return 'chmury nie byly widoczne'
        return self.medium_clouds[int(number)]

    def get_high_clouds(self, number):
        if number == '/':
            return 'chmury nie byly widoczne'
        return self.high_clouds[int(number)]



