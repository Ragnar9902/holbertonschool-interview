#!/usr/bin/python3

def pascal_triangle(n):
    if n <= 0:
        return []
    else:
        tri = [[1]]
        for i in range(n - 1):
            row = [1]
            for j, v in enumerate(tri[i]):
                if j != 0:
                    row.append(tri[i][j] + tri[i][j - 1])
            row.append(1)
            tri.append(row)
        return tri