from Calculator import calculator
class Fahrenheit_to_Celsius_Converter():
    def __init__(self) -> None:
        self.cal = calculator.Calculator()

    def convert(self, F):
        C = self.cal.subtract(F, 32)
        C = C * (5 / 9)
        return C
