//Jun 13 2021

//Origin: https://leetcode.com/problems/path-crossing/

/**
 * @param {string} path
 * @return {boolean}
 */
var isPathCrossing = function (path) {
	let dots = { "0,0": 1 };

	let cur = [0, 0];

	for (let i = 0; i < path.length; i++) {
		if (path[i] === "N") {
			cur[1] += 1;
		}
		if (path[i] === "S") {
			cur[1] -= 1;
		}
		if (path[i] === "E") {
			cur[0] += 1;
		}
		if (path[i] === "W") {
			cur[0] -= 1;
		}

		if (!dots[cur]) {
			dots[cur] = 1;
		} else {
			return true;
			break;
		}
	}

	return false;
};
