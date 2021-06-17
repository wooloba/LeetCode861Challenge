//Jun 17 2021

//Origin: https://leetcode.com/problems/number-of-good-ways-to-split-a-string/

/**
 * @param {string} s
 * @return {number}
 */
var numSplits = function (s) {
	const obj = {};

	let count = 0;

	for (let i = 0; i < s.length; i++) {
		if (obj[s[i]] === undefined) {
			obj[s[i]] = 1;
		} else {
			obj[s[i]] += 1;
		}
	}

	const left = {};
	const right = { ...obj };

	for (let i = 0; i < s.length; i++) {
		if (left[s[i]] === undefined) {
			left[s[i]] = 1;
		} else {
			left[s[i]] += 1;
		}

		right[s[i]] -= 1;
		if (right[s[i]] === 0) {
			delete right[s[i]];
		}

		if (Object.keys(left).length === Object.keys(right).length) {
			count += 1;
		}
	}

	return count;
};
