//May 30 2020    

//Origin: https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/

/**
 * @param {number[][]} rects
 */
var Solution = function(rects) {
    this.totalArea = 0;
    this.areaList = [];
    this.rects = rects;
    
    rects.forEach((rect)=>{
        const area = (rect[2]-rect[0]+1)*(rect[3]-rect[1]+1);
        this.totalArea += area;
        this.areaList.push(area);
    })
};

/**
 * @return {number[]}
 */
Solution.prototype.pick = function() {
    let seed = Math.random() * this.totalArea;
    
    let i = 0;
    while(seed- this.areaList[i] >0){
        seed -= this.areaList[i];
        i++;
    }
    
    const getRandomInt = (max) =>  Math.floor(Math.random() * max);
    
    const rect = this.rects[i];
    
    return [
        rect[0] + getRandomInt(rect[2] - rect[0]+1), 
        rect[1] + getRandomInt(rect[3] - rect[1]+1)
    ]
    
};

/** 
 * Your Solution object will be instantiated and called as such:
 * var obj = new Solution(rects)
 * var param_1 = obj.pick()
 */