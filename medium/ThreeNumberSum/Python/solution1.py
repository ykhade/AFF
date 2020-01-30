# Time: O(n^2log(n)) | Space: O(n)

def threeNumberSum(array, targetSum):
    array.sort()
    triplets = []
    for i in range(len(array) - 2):
        left = i + 1;
        right = len(array) - 1
        while left < right:
            possibleSum = array[i] + array[left] + array[right]
            if possibleSum == targetSum:
                triplets.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif possibleSum < targetSum:
                left += 1
            elif possibleSum > targetSum:
                right -= 1
    return triplets
