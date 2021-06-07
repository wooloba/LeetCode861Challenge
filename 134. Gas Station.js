//Jun 7 2021

//Origin: https://leetcode.com/problems/gas-station/

/**
 * @param {number[]} gas
 * @param {number[]} cost
 * @return {number}
 */


var canCompleteCircuit = function (gas, cost) {
	const totalGas = gas.reduce((accum, g) => accum + g, 0);
	const totalCost = cost.reduce((accum, c) => accum + c, 0);

	if (totalGas - totalCost < 0) return -1;

	let res = 0;
	let tank = 0;

	for (let i = 0; i < gas.length - 1; i++) {
		tank = tank + gas[i] - cost[i];

		if (tank < 0) {
			//reset
			tank = 0;
			res = i + 1;
		}
	}

	return res;
};
