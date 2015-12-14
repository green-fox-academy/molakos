mytext = 'alma.txt'

def appendNumbers(text):
    input_file = open(text, 'w')
    data = ''
    for i in range(11):
        data = str(i)+'\n'
        input_file.write(data)
        print(data)
    input_file.close()

appendNumbers(mytext)
