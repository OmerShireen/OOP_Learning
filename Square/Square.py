class SquareCalculator:
    def __init__(self, num:int):
        self.__num = num
        self.__squares = []

    def traditional(self):
        self.__squares = []
        for i in range(1, self.__num+1):
            self.__squares.append(i*i)

    def pythonic(self):
        self.__squares = [i**2 for i in range(1, self.__num)]

    @property
    def num(self):
        return self.__num

    @property
    def squares(self):
        return self.__squares

    def display(self):
        print(f"Squares of {self.__num}: {self.__squares}")

    def __str__(self):
        return f"Squares of {self.__num}: {self.__squares}"


   


























