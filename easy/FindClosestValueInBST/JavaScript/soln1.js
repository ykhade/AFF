function findClosestValueInBst(tree, target) {
	// Average: Time: O(log(n)) | Space: O(1)
	// Worst: Time: O(n) | Space: O(1)
	return findClosestValueInBstHelper(tree, target, tree.value)
  // Write your code here.
}

function findClosestValueInBstHelper(tree, target, closest) {
	let currentNode = tree; 
	while (currentNode !== null) {
		if (Math.abs(target - closest) > Math.abs(target - currentNode.value)) {
			closest = currentNode.value;
		}
		if (target < currentNode.value) {
			currentNode = currentNode.left;
		} else if (target > currentNode.value) {
			currentNode = currentNode.right;
		} else {
			break;
		}
	}
	return closest
}

// Do not edit the line below.
exports.findClosestValueInBst = findClosestValueInBst;
