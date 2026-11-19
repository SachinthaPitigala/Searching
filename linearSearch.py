def linearSearch(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
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