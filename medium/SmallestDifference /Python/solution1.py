# Time: O(n^2) | Space: O(n)

def smallestDifference(arrayOne, arrayTwo):
    smallestNumber = 1000000000
    smallestPair = []
    for i in range(len(arrayOne)):
        for j in range(len(arrayTwo)):
            possibleSmallest = abs(arrayOne[i] - arrayTwo[j])
            if possibleSmallest <= smallestNumber:
                smallestNumber = possibleSmallest
                smallestPair = [arrayOne[i], arrayTwo[j]]

    return smallestPair
