
def isAlienSorted(words: list, order: str) -> bool:
    """Checks if the words list is sorted according to the order.

    Parameters:
        words (list): The words to check if they are sorted or not.
        order (str): The order of the words according to which we hv to check.
    
    Return:
        bool: True if they are sorted accordingly else False.
    """

    order_map = {}

    for i , char in enumerate(order):
        order_map[char] = i
    
    for i in range(len(words) - 1):

        for j in range(len(words[i])):

            if j >= len(words[i+1]):
                return False

            if words[i][j] != words[i+1][j]:
                current_letter = order_map[words[i][j]]
                next_letter = order_map[words[i + 1][j]]

                if current_letter > next_letter:
                    return False
                else:
                    break

    return True

            