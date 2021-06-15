//Jun 14 2021

//Origin: https://leetcode.com/problems/snapshot-array/

/**
 * @param {number} length
 */
var SnapshotArray = function (length) {
	this.snaps = [];
	this.history = new Map();
	this.length = length;
	this.id = -1;
};

/**
 * @param {number} index
 * @param {number} val
 * @return {void}
 */
SnapshotArray.prototype.set = function (idx, val) {
	this.history.set(idx, val);
};

/**
 * @return {number}
 */
SnapshotArray.prototype.snap = function () {
	this.snaps.push(this.history);

	this.history = new Map();
	this.id += 1;

	return this.id;
};

/**
 * @param {number} index
 * @param {number} snap_id
 * @return {number}
 */
SnapshotArray.prototype.get = function (index, snap_id) {
	for (let i = snap_id; ~i; i--) {
		if (this.snaps[i].has(index)) {
			return this.snaps[i].get(index);
		}
	}

	return 0;
};

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * var obj = new SnapshotArray(length)
 * obj.set(index,val)
 * var param_2 = obj.snap()
 * var param_3 = obj.get(index,snap_id)
 */
