def count_letters(input_str):
    output = {}
    for letter in input_str:
        if not letter in output:
            output[letter] = 0
        output[letter] += 1
    return output
