def linearSearch(arr, target):
    """
    Perform a linear search on the given array to find the target value.

    Parameters:
    arr (list): The list of elements to search through.
    target: The value to search for in the list.

    Returns:
    int: The index of the target value if found, otherwise -1.
    """
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return None

def main():
    # Example usage of the linearSearch function
    arr = [5, 3, 8, 6, 2]
    target = 6
    result = linearSearch(arr, target)

    if result is not None:
        print(f"Target {target} found at index: {result}")
    else:
        print(f"Target {target} not found in the array.")   

if __name__ == "__main__":
    main()