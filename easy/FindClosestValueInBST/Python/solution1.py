def findClosestValueInBst(tree, target):
    # Write your code here.
	# Time: O(log(n)) | Space: O(1)
	return findClosestValueInBstHelper(tree, target, float('inf'))

def findClosestValueInBstHelper(tree, target, closest):
	while (tree is not None):
		if abs(target - closest) > abs(target - tree.value):
			closest = tree.value
		if target > tree.value:
			tree = tree.right
		elif target < tree.value:
			tree = tree.left
		else:
			break
	return closest
