# Python 3 program for implementation of
# Min or Max Sum Path in a Triangle

# Open data from file and transform
with open('data/test_triangle.txt', 'r') as file:
    A = [line.strip().split() for line in file]

def sumPath(A: list, function: str) -> int:
    """
    Returns Min or Max Sum Path in a Triangle
    Ex.
     4
     3 2
     1 2 5
    >>> sumPath(A,'min')
    5
    Ex.
        4
       3 2
      1 2 5
    >>> sumPath(A,'max')
    31

    :param A: List of list with elements in row
    :param function: Value 'max' or 'min'
    :return: Min or Max Sum Path in a Triangle
    """
    # For storing the result in a 1-D array
    memo = [None] * len(A)
    path = ['-']*len(A)
    n = len(A) - 1

    # For the bottom row
    for i in range(len(A[n])):
        memo[i] = int(A[n][i])
        path[i] = A[n][i]

    # Calculation of the remaining rows, in bottom up manner.
    for i in range(len(A) - 2, -1,-1):
        for j in range( len(A[i])):
            if(int(memo[j])>int(memo[j + 1])):
              path[j] = path[j + 1] + "-" + A[i][j]
            if(int(memo[j])<=int(memo[j+1])):
              path[j] = path[j] + "-" + A[i][j]

            if function=="min":
              memo[j] = int(A[i][j]) + min(memo[j], memo[j + 1]);
            elif function=="max":
              memo[j] = int(A[i][j]) + max(memo[j], memo[j + 1]);
            else:
              raise ValueError("Parameter function must have a value: 'max' or 'min'.")

    # Show the Path
    # print("Path: ", path[0][::-1])

    # return the top element
    return memo[0]


print(sumPath(A,'min'))
print(sumPath(A,'max'))
