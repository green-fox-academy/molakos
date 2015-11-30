ag = 'kuty'

def add_letters(input):
    return input + 'a'

ag = add_letters(ag)
print(ag)

ag2 = ['rep', 'macsk', 'cic', 'alm', 'Ann', 'kacs']

for i in range(len(ag2)):
    ag2[i] = add_letters(ag2[i])

print(ag2)
