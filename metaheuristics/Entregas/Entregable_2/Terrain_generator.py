import random
import numpy as np


def generate_terrain(dimension_n, dimension_m, max=20):
    """generates a terrain of dimension_n x dimension_m with random values between 0 and 100
    :param int dimension_n: the number of rows of the terrain
    :param int dimension_m: the number of columns of the terrain
    :returnas ndarray: the generated terrain"""
    terrain = np.zeros((dimension_n, dimension_m))
    for i in range(dimension_n):
        for j in range(dimension_m):
            terrain[i][j] = random.randint(0, 20)
    return terrain


def write_terrain(terrain, file_name):
    """writes the terrain to a file
    :param np.array terrain: the terrain to be written
    :param str file_name: the name of the file to be written"""
    with open(file_name, "w") as file:
        file.write(str(len(terrain)) + " " + str(len(terrain[0])) + "\n")
        for i in range(len(terrain)):
            for j in range(len(terrain[i])):
                file.write(str(int(terrain[i][j])) + " ")
            file.write("\n")


def read_terrain(file_name):
    """Reads a terrain from a file
    :param str file_name: the name of the file to be read
    :return np.array: the terrain read from the file"""
    with open(file_name, "r") as file:
        lines = file.readlines()
        terrain = np.zeros((int(lines[0].split()[0]), int(lines[0].split()[1])))
        for i in range(1, len(lines)):
            for j in range(len(lines[i].split())):
                terrain[i - 1][j] = int(lines[i].split()[j])
    return terrain


def make_copy(terrain):
    """Makes a copy of the terrain
    :param np.array terrain: the terrain to be copied
    :return np.array: the copy of the terrain"""
    copy = np.zeros((len(terrain), len(terrain[0])))
    for i in range(len(terrain)):
        for j in range(len(terrain[i])):
            copy[i][j] = terrain[i][j]
    return copy
