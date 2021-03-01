# This is your coding interview problem for today.
#
# This problem was asked by Palantir.
#
# A typical American-style crossword puzzle grid is an N x N matrix with black
# and white squares, which obeys the following rules:
#
# Every white square must be part of an "across" word and a "down" word.
# No word can be fewer than three letters long.
# Every white square must be reachable from every other white square.
#
# The grid is rotationally symmetric (for example, the colors of the top left
# and bottom right squares must match).
#
# Write a program to determine whether a given matrix
# qualifies as a crossword grid.
# ----------------------------------------------------------------------------

from collections import deque


# This method is not needed since we are already checking if theres
# at least 3 values to each word in check_three
def check_isolated(array):
    for i in range(len(array)-1):
        for j in range(len(array)-1):
            if (array[i][j]):
                if (i == 0 and array[i+1][j] == 0) or \
                   (i == len(array)-1 and array[i-1][j] == 0) or \
                   (j == 0 and array[i][j+1] == 0) or \
                   (j == len(array)-1 and array[i][j-1] == 0):
                    return False
                elif not ((array[i+1][j] or array[i-1][j]) and
                          (array[i][j+1] or array[i][j-1])):
                    return False
    return True


# The solution to this method was a lot easier than my implementation
# the solution goes through each row and resets a count when a value
# of 1 is found. once the value finds 0 then the count will be checked
# and then reset. This is done for all row and columns.
def check_three(array):
    for i in range(len(array)-1):
        for j in range(len(array)-1):
            if array[i][j]:
                value = 0
                while (i-value > 0 and array[i-value][j]):
                    value += 1
                value -= 1
                cnt = 1
                while (i-value < len(array) and array[i-value][j]):
                    value -= 1
                    cnt += 1
                if cnt < 3:
                    return False
                value = 0
                while (j-value > 0 and array[i][j-value]):
                    value += 1
                value -= 1
                cnt = 1
                while (j-value < len(array) and array[i][j-value]):
                    value -= 1
                    cnt += 1
                if cnt < 3:
                    return False
    return True


# I had to look at the solution for this. list(zip(*array)) transposes
# the array while array2[::-1] is slice notation for reversing the
# array. zip creates a tuple so need to remap back to list at the end
def check_rotational(array):
    array2 = list(zip(*array))
    array2 = array2[::-1]
    array2 = list(zip(*array2))
    array2 = array2[::-1]
    return array == list(map(list, array2))


# Need to do a BFS solution for this
#
# procedure BFS(G, start_v) is
#     let Q be a queue
#     label start_v as discovered
#     Q.enqueue(start_v)
#     while Q is not empty do
#         v := Q.dequeue()
#         if v is the goal then
#             return v
#         for all edges from v to w in G.adjacentEdges(v) do
#             if w is not labeled as discovered then
#                 label w as discovered
#                 w.parent := v
#                 Q.enqueue(w)
def is_connected(array):
    count = sum([i for row in array for i in row])
    start = None
    for row in range(len(array)):
        for col in range(len(array)):
            if array[row][col]:
                start = (row, col)
                break
    q = deque([start])
    v = set()
    connected_cnt = 0
    while q:
        loc = q.popleft()
        if loc not in v:
            v.add(loc)
            connected_cnt += 1
            i, j = loc
            for neighbor in [(i-1, j), (i, j-1), (i+1, j), (i, j+1)]:
                row, col = neighbor
                if (0 <= row < len(array) and 0 <= col < len(array) and
                   array[row][col]):
                    q.append(neighbor)
    return count == connected_cnt


if __name__ == '__main__':
    test1_file = [[1, 1, 1, 0, 0, 1, 1, 1],
                  [1, 1, 1, 1, 0, 1, 1, 1],
                  [1, 1, 1, 1, 0, 1, 1, 1],
                  [0, 0, 0, 1, 1, 1, 0, 0],
                  [0, 0, 1, 1, 1, 1, 0, 0],
                  [1, 1, 1, 1, 1, 0, 0, 0],
                  [1, 1, 1, 0, 0, 0, 0, 0],
                  [1, 1, 1, 0, 0, 0, 0, 0]]

    test2_file = [[1, 1, 1, 0, 0, 1],
                  [0, 0, 0, 0, 0, 0],
                  [1, 1, 1, 0, 1, 0],
                  [0, 0, 1, 0, 0, 1],
                  [0, 0, 1, 0, 0, 1],
                  [1, 1, 1, 0, 0, 1]]
    test3_file = [[1, 1, 0, 0, 1, 1],
                  [1, 1, 0, 0, 1, 1],
                  [0, 0, 1, 1, 0, 0],
                  [0, 0, 1, 1, 0, 0],
                  [1, 1, 0, 0, 1, 1],
                  [1, 1, 0, 0, 1, 1]]
    test4_file = [[1, 1, 1, 1],
                  [1, 0, 0, 1],
                  [1, 0, 0, 1],
                  [1, 1, 1, 1]]
    print(check_isolated(test1_file))
    print(check_isolated(test3_file))
    print(check_three(test1_file))
    print(check_rotational(test3_file))
    print(not check_rotational(test2_file))
    print(is_connected(test1_file))
    print(not is_connected(test2_file))
