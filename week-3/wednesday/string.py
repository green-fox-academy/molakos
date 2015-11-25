class MySuperString:
    def __init__(self, mystr):
        self.mystr = mystr

    def reverse(self):
        n = len(self.mystr)
        reversed = ''
        for i in range(n):
            reversed = self.mystr[i] + reversed
            print(reversed)
        return reversed

    def imp(self, char):
        count = 0
        n = len(self.mystr)
        for i in range(n):
            if self.mystr[i] == char:
                count += 1
        return count

    def underline(self):
        n = len(self.mystr)
        nospace = ''
        for i in range(n):
            if self.mystr[i] == ' ':
                nospace = nospace + '_'
            else:
                nospace = nospace + self.mystr[i]
        return nospace
