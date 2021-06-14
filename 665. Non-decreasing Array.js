//Jun 13 2021

//Origin: https://leetcode.com/problems/non-decreasing-array/

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var checkPossibility = function (nums) {
	const sorted = [...nums].sort((a, b) => a - b);

	let miss = 0;
	let j = 0;

	for (let i = 0; i < nums.length; i++) {
		if (miss > 2) {
			return false;
		}

		if (sorted[i] !== nums[j]) {
			miss++;

			if (sorted[i + 1] === nums[j]) {
				//missed = sorted[i]
				i++;
			} else if (sorted[i] === nums[j + 1]) {
				//missed = sorted[j]
				j++;
			} else return false;
		}

		j++;
	}

	if (j < nums.length - 1 || miss > 2) return false;

	return true;
};
