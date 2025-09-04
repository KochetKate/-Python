class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address
        self.from_adress = from_address
        self.cost = cost
        self. track = track

    def __str__(self):
        return f"Отправление {self.track} из {self.from_adress} в {self.to_address}. Стоимость {self.cost} рублей."
