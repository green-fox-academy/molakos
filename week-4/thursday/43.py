filename = 'alma.txt'
def readit(dafile):
    input_file = open(dafile)
    filename_content = input_file.read()
    return filename_content
    filename.close()

print(readit(filename))
