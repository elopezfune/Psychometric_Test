
def jobOffers(scores,lowerLimits,upperLimits):
    if len(scores)>10**5 or len(lowerLimits)>10**5 or len(lowerLimits) != len(upperLimits):
        print('The arrays do not match the constrains')
    else:
        result = []
        scores.sort()
        n = len(scores)
        for index, _ in enumerate(lowerLimits):
            result.append(countInRange(scores, n, lowerLimits[index], upperLimits[index]))
    return result

# Function to find first index larger or equal than x
def minIndex(array, n, x):
    l = 0
    h = n-1
    while (l <= h):
        mid = int((l + h)/2)
        if (array[mid] >= x):
            h = mid - 1
        else:
            l = mid + 1
    return l
 

# Function to find last index smaller or equal than x
def maxIndex(array, n, x):
    l = 0
    h = n-1
    while (l <= h):
        mid = int((l + h)/2)
        if (array[mid] <= x):
            l = mid + 1
        else:
            h = mid - 1
    return h
 
 
# function to count elements within given range
def countInRange(array, n, x, y):
    # initialize result
    count = 0;
    count = maxIndex(array, n, y) - minIndex(array, n, x) + 1;
    return count


print(jobOffers([1,3,5,6,8],[2],[6]))

