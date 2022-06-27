class SparseMatrix:
    def __init__(self, matrix, shape):
        self.matrix = matrix
        self.shape = shape

    def add_matrices(self, matrix1, matrix2):
        matrix_result = (matrix1.tocsr() + matrix2.tocsr()).tolil()

    def subtract_matrices(self, matrix1, matrix2):
        matrix_result = (matrix1.tocsr() - matrix2.tocsr()).tolil()

    def print_matrix(self, matrix):
        print(matrix)

    # function to convert dense to sparse matrix
    def helper(self, matrix):
        sparse_matrix = {(r, c): v for (r, c, v) in matrix}
        return sparse_matrix

