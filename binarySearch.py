def binarySearch(anyList, anyTarget):
	'''
	Perform a binary search on a sorted list to find the target element.

	Parameters:
	anyList (list): A sorted list of elements to search through.
	anyTarget (any): The element to search for in the list.

	Returns:
	int: The index of the target element if found, otherwise None.
	'''
	left = 0
	right = len(anyList) - 1

	while left <= right:
		midPoint = (left + right) // 2

		if anyList[midPoint] == anyTarget:
			return midPoint
		elif anyTarget < anyList[midPoint]:
			right = midPoint - 1
		else:
			left = midPoint + 1

	return None

def main():
	myList = [1, 4, 7, 8, 10, 11, 13]
	target = 100
	result = binarySearch(myList, target)

	if result is not None:
		print(f"{target} is found at the {result}.")
	else:
		print(f"{target} is not in the list.")

if __name__ == "__main__":
    main()  