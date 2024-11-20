/**
350. Intersection of Two Arrays II
https://leetcode.com/problems/intersection-of-two-arrays-ii/description/
*/
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */

var intersect = function(nums1, nums2) {
    const countMap = nums1.reduce(
        (map, num)=>{
            map.set(num, (map.get(num)||0)+1)
            return map;
        },
        new Map()
    );
    
    return nums2.reduce((res, num)=>{
        if (countMap.get(num)){
            res.push(num);
            countMap.set(num, countMap.get(num)-1);
        }
        return res;
    }, []);
    };