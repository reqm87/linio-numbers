class LinioNumber:

    def __init__(self, number):
        self.labels = ['IT', 'Linio', 'Linianos']
        self.print_result(number)

    def get_index(self, number):
        return self.div_three_and_five(number) * 2 + self.div_three(number)

    def print_result(self, number):
        if number % 3 == 0 or number % 5 == 0:
            print(self.labels[self.get_index(number)])
            return
        print(number)

    @staticmethod
    def div_three(number):
        return number % 3 == 0 and number % 5 > 0

    @staticmethod
    def div_three_and_five(number):
        return number % 3 == 0 and number % 5 == 0

def main():
    for i in range(1, 101):
        LinioNumber(i)

if __name__ == "__main__":
    main()
