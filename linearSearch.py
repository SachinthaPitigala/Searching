def linearSearch(list, target):
    '''
    This function performs a linear search on the given list to find the target value.
    It returns the index of the target if found, otherwise it returns None.
    '''
    for index in range(len(list)):
        if list[index] == target:
            return index
    return None


def main():
    myList = [1, 2, 3, 4, 5]
    target = 3
    result = linearSearch(myList, target)
    if result is not None:
        print(f"Target found at index: {result}")
    else:
        print("Target not found in the list.")

if __name__ == "__main__":
    main()