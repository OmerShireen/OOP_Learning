class DataAnalyzer:
    def __init__(self, data):
        self.data = data

    def minmax(self):


        smallest = largest = self.data[0]

        for number in self.data[1:]:
            if number < smallest:
                smallest = number

            elif number > largest:
                largest = number

        return (smallest, largest)


dataset = DataAnalyzer([4, 7, 1, 9, 0, 5])
print(dataset.minmax())                

        