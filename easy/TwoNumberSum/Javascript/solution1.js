function twoNumberSum(array, targetSum) {
	const nums = {};
	for (const num of array) {
		const complement = targetSum - num;
		if (complement in nums) {
			return complement > num ? [num, complement] : [complement, num];
		} else {
			nums[num] = true;
		}
	}
	return [];
}

