
class Date:

    def __init__(self):
        self.date_list = []
        self.date_list.append(input("Rok:"))
        self.date_list.append(input("Miesiac:"))
        self.date_list.append(input("Dzien:"))
        self.date_list.append(input("Godzina:"))
        self.date_list.append(input("Minuty:"))

    def get_date_list(self):
        return self.date_list
