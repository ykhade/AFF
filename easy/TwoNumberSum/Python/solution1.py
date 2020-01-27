def twoNumberSum(array, targetSum):
    # Write your code here.
	# Time: O(n) | Space: O(1)
	array.sort()
	left = 0
	right = len(array) - 1
	while (left < right):
		possibleSum = array[left] + array[right]
		if (possibleSum == targetSum):
			return [array[left], array[right]]
		elif (possibleSum < targetSum):
			left += 1
		elif (possibleSum > targetSum):
			right -=1
	return []