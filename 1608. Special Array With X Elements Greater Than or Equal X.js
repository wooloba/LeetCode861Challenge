//Jun 13 2021

//Origin: https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/

/**
 * @param {number[]} nums
 * @return {number}
 */
var specialArray = function (nums) {
	const lookup = Array(nums.length + 1).fill(0);

	nums.forEach((num) => {
		lookup.forEach((v, k) => {
			if (num >= k) {
				lookup[k] += 1;
			}
		});
	});

	let res = lookup.findIndex((v, k) => v === k);

	return res ?? -1;
};
