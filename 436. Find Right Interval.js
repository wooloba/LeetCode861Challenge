//Jun 6 2021

//Origin: https://leetcode.com/problems/find-right-interval/

/**
 * @param {number[][]} intervals
 * @return {number[]}

var findRightInterval = function(intervals) {
    const sortedStarted = intervals.map(([s,e],i)=>[s,e,i]).sort(([f],[s])=>f-s);
    
    const res = [];
    
    
    intervals.forEach(([si,ei],i)=>{
        
        let des = -1
        let desA = sortedStarted[sortedStarted.length-1][0];
        
        sortedStarted.forEach(([a,b,c])=>{            
            if (a >= ei && (a < desA || des === -1)){
                des = c;
                desA = a
            };
        });
        
        res.push(des)
    })
    
    return res;
    
};

 */

var findRightInterval = function (intervals) {
	const sortedStarted = intervals
		.map(([s, e], i) => [s, e, i])
		.sort(([f], [s]) => f - s);

	const res = Array(intervals.length).fill(-1);

	intervals.map(([start, end], i) => {
		let left = 0;
		let right = intervals.length - 1;

		while (right >= left) {
			let mid = Math.floor((right + left) / 2);

			if (sortedStarted[mid][0] === end) {
				res[i] = sortedStarted[mid][2];
				break;
			}

			if (sortedStarted[mid][0] > end) {
				res[i] = sortedStarted[mid][2];
				right = mid - 1;
			} else {
				left = mid + 1;
			}
		}
	});

	return res;
};
