/**
 * @param {number[][]} points
 * @param {number} K
 * @return {number[][]}
 */
// Time: O(nlog(n)) | Space: O(n)
var kClosest = function(points, K) {
    if (points.length === K) {
        return points
    }
  return  points.sort((a,b) => distance(a) - distance(b)).slice(0,K)
};

const distance = (point) => {
        return (point[0] ** 2) + (point[1] ** 2)
        
    }
