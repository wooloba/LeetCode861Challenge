//Jun 6 2021

//Origin: https://leetcode.com/problems/integer-replacement/

/**
 * @param {number} n
 * @return {number}
 */
var integerReplacement = function(n) {
    
    let memo = [0,0,1,2,2];
    
    const iterator =(n)=>{
        if(memo[n] !== undefined) {
            return memo[n];
        }
        
        
        let count  = n % 2 == 0 ?
            iterator(n/2) + 1:
            Math.min(iterator(n+1) + 1, iterator(n-1) + 1)
        
        memo[n] = count;
        
        return count;
	};
    
    
	iterator(n);
    

	return memo[n];
};