def linearSearch(list, target):
    '''
    Perform a linear search on the given list to find the target value.

    Parameters:
    list (list): The list of elements to search through.
    target: The value to search for in the list.'''

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