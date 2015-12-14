class DuplicateEncoder:
    def __init__(self, text):
        self.text = text.lower()

    def encode_chr(self, c):
        return '(' if self.text.count(c) == 1 else ')'

    def encode(self):
        out = ''
        for c in self.text:
            out += self.encode_chr(c)
