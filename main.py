def main():
    """
    Reads user inputs and calls binary search to search for input in input list
    Parameters: None
    Returns: Nothing
    """

    indata = input().strip()
    the_list = indata.split()
    #Läs in nycklar att söka efter
    key = input().strip()
    while key != "#":
        print(binary_search(the_list, key))
        key = input().strip()


def binary_search(arr, key):
    """
    Takes list and searches for key in list using binary search method
    Parameters: array (list) to search through, key to search for
    Returns: Nothing

    Code from chatGPT
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return arr[mid]
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return None

main()