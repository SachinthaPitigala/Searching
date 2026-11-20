def recursiveBinarySearch(anyList, anyTarget):
	'''
	Perform a recursive binary search on a sorted list to find the target element.

	Parameters:
	anyList (list): A sorted list of elements to search through.
	anyTarget (any): The element to search for in the list.

	Returns:
	bool: True if the target element is found, otherwise False.
	'''
	if len(anyList) == 0:
		return False
	else:
		midPoint = len(anyList)//2

		if anyList[midPoint] == anyTarget:
			return True
		elif anyTarget < anyList[midPoint]:
			return recursiveBinarySearch(anyList[:midPoint], anyTarget)
		else:
			return recursiveBinarySearch(anyList[midPoint+1:],anyTarget)

def main():
	myList = [2,4,7,9,12,13,15,17]
	myTarget = 19	
	result = recursiveBinarySearch(myList, myTarget)	
	if result:
		print("Target is found in the list")
	else:
		print("Target is not found in the list")

if __name__ == "__main__":
	main()