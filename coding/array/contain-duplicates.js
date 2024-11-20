/**
217. Contains Duplicate
https://leetcode.com/problems/contains-duplicate/description/
*/
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    return new Set(nums).size!=nums.length;
};


let nums = [1, 2, 3, 1];
console.log(containsDuplicate(nums));