
def check_duplicate(array):

    hash_set = set()

    for element in array:
        if element in hash_set:
            return True
        else:
            hash_set.add(element)

    return False