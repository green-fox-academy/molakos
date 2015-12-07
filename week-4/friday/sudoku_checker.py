def is_complete(numbers):
    if len(numbers) != 9:
        return False

    return True

def is_the_same(numbers):
    if len(set(numbers)) != 9:
        return False
        
    return True
