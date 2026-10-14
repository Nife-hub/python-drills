def matrix_sums(matrix): #-> (list, list):
    rows = []
    cols = []
    for row in matrix:
        rows.append(sum(row))

        for i in range(len(row)):
            if not cols:
                cols.extend(row)
                break
            else:
                cols[i] += row[i]




# print(matrix_sums([[1, 2], [3, 4]]))
# ([6, 15, 24], [12, 15, 18]) << [[1, 2, 3], [4, 5, 6], [7, 8, 9]])