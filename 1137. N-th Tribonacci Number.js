//May 31 2020

//Origin: https://leetcode.com/problems/n-th-tribonacci-number/

/**
 * @param {number} n
 * @return {number}
 */

var tribonacci = function (n) {
	let memo = [0, 1, 1];

	let iterator = (n) => {
		if (memo[n] !== undefined) {
			return memo[n];
		}

		memo[n] = iterator(n - 3) + iterator(n - 2) + iterator(n - 1);

		return memo[n];
	};

	iterator(n);

	return memo[n];
};
