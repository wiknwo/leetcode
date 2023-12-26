# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
# Maximum sum two non-attacking rooks

def solution(A):
    # write your code in Python 3.6
    board_values = [(val, (r, c)) for r, row in enumerate(A) for c, val in enumerate(row)]
    mx = max(board_values)
    mx2 = max(v for v in board_values if v != mx)
    mxs = [mx, mx2]

    result = 0
    for v, (r, c) in mxs:
        for nv, (nr, nc) in board_values:
            if nr != r and c != nc:
                result = max(result, v + nv)
    return result

