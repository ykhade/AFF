function twoNumberSum(array, targetSum) {
//Space: O(1) | Time: O(nlog(n)) 
	array.sort((a,b) => a - b)
	let left = 0
	let right = array.length - 1
	while (left < right) {
		let probMatch = array[left] + array[right]
		if (probMatch === targetSum) {
			return array[left] > array[right] ? [array[left], array[right]] : [array[right], array[left]]
		}
		else if (probMatch < targetSum) {
			left ++
		} else if (probMatch > targetSum) {
			right --
		}
	}
	return []
}

