from time import sleep


class CalculateAndAmountLitersFuelSpentTrip:
    def __init__(self):
        self.time_travel = 0
        self.average_speed = 0
        self.average_consumption = 12
        self.questions()

    def questions(self):
        self.info("Informe o tempo gasto na viagem em HORAS:")
        self.time_travel = int(input())
        self.info("Informe a velocidade média em KM/H:")
        self.average_speed = int(input())

    def calculate(self):
        self.info("Calculando a distância percorrida...")
        self.calculate_distance()
        self.info("Calculando a quantidade de litros necessários ...")
        self.calculate_liters()

    def calculate_distance(self, show_info=True):
        distance = self.time_travel * self.average_speed
        if show_info:
            self.info(f"Distância percorrida foi de {distance} km", slp=True)
        return distance

    def calculate_liters(self):
        distance = self.calculate_distance(show_info=False)
        liter_necessary = float("{:.2f}".format(distance / self.average_consumption))
        self.info(f"Quantidade Combustivel necessário é de {liter_necessary} litros.", slp=True)

    @staticmethod
    def info(msg, slp=False):
        if slp:
            sleep(2)
        print(msg)


if __name__ == '__main__':
    calculate = CalculateAndAmountLitersFuelSpentTrip()
    calculate.calculate()

