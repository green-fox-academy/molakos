class MyMath:
    def __init__(self, num_list):
        self.num_list = num_list

    def average(self):
        i = 0
        sum = 0
        while i < len(self.num_list):
            sum += self.num_list[i]
            i += 1
        return sum / i
