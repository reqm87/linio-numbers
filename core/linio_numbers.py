class LinioNumber:
    def __init__(self, number):
        self.labels = ["IT", "Linio", "Linianos"]
        self.number = number

    def get_index(self):
        return self.div_three_and_five() * 2 + self.div_three()

    def process(self):
        if self.number % 3 == 0 or self.number % 5 == 0:
            return self.labels[self.get_index()]
        return str(self.number)

    def div_three(self):
        return self.number % 3 == 0 and self.number % 5 > 0

    def div_three_and_five(self):
        return self.number % 3 == 0 and self.number % 5 == 0


def main():
    for i in range(1, 101):
        linio_number = LinioNumber(i)
        print(linio_number.process())


if __name__ == "__main__":
    main()
