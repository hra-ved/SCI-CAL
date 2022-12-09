import numpy as np


def subtract_matrices(matrix_a, matrix_b):
    return np.subtract(matrix_a, matrix_b)


def add_matrices(matrix_a, matrix_b):
    return np.add(matrix_a, matrix_b)


def multiple_matrice_scalar(matrix_a, scalar):
    return np.multiply(matrix_a, scalar)


def multiply_matrices(matrix_a, matrix_b):
    return np.matmul(matrix_a, matrix_b)


def matrix_determinant(matrix_a):
    return np.linalg.det(matrix_a)


def matrix_inversion(matrix_a):
    return np.linalg.inv(matrix_a)


def matrix_transpose(matrix_a):
    return np.transpose(matrix_a, axes=None)


def pseudo_random_generator(row, col):
    return np.rand(row, col)


def subtract_matrices(matrix_a, matrix_b):
    return np.subtract(matrix_a, matrix_b)


def add_matrices(matrix_a, matrix_b):
    return np.add(matrix_a, matrix_b)


def multiple_matrice_scalar(matrix_a, scalar):
    return np.multiply(matrix_a, scalar)


def multiply_matrices(matrix_a, matrix_b):
    return np.matmul(matrix_a, matrix_b)


def matrix_determinant(matrix_a):
    return np.linalg.det(matrix_a)


def matrix_inversion(matrix_a):
    return np.linalg.inv(matrix_a)


def matrix_transpose(matrix_a):
    return np.transpose(matrix_a, axes=None)


def pseudo_random_generator(row, col):
    return np.rand(row, col)
