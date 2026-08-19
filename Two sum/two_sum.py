def two_sum(array , target):

    hash_map = {}

    for index , value in enumerate(array):
        remainder = target - value
        if remainder in hash_map:
            return [index , hash_map[remainder]]

        hash_map[value] = index

    return [0,0]