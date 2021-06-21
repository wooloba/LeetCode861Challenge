//Jun 20 2021

//Origin: https://leetcode.com/problems/ugly-number-ii/

/**
 * @param {number} n
 * @return {number}
 */
var nthUglyNumber = function (n) {
	const factors = [2, 3, 5];
	const offset = [0, 0, 0];
	const ugly = [1];
	n--;

	while (n--) {
		const candidates = factors.map((val, i) => ugly[offset[i]] * val);
		const next = Math.min(...candidates);
		candidates.forEach((val, i) =>
			candidates[i] === next ? offset[i]++ : null
		);
		ugly.push(next);
	}
	return ugly.pop();
};
