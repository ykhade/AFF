class Solution {
    // Time: O(nlog(n)) | Space: O(n)
    public int[][] kClosest(int[][] points, int K) {
        // If there are only K number of points those the closest points
        if(K == points.length) return points; 
        // Using priority queue to add points in and order them by distance form origin
        PriorityQueue<int[]> maxHeap = new PriorityQueue<>((a,b) -> (b[0]*b[0] + b[1]*b[1] - (a[0]*a[0] + a[1]*a[1])));
        for(int[] point: points) {
            maxHeap.add(point);
            if(maxHeap.size() > K) 
                maxHeap.remove();
        }
        return maxHeap.toArray(new int[0][0]);
    }
}
