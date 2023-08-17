import random
import numpy as np
import Terrain_generator as tg
import math as m


def compute_sprinkler_amount(n, m):
    """Computes the amount of sprinklers for each type based on the size of the terrain
    :param int n: the number of rows of the terrain
    :param int m:  the number of columns of the terrain
    :return ndarray:  amount of sprinklers for each type
    """
    sprinklers = np.zeros(5)
    sprinklers[0] = (5 * n * m) / 80
    sprinklers[1] = (4 * n * m) / 70
    sprinklers[2] = (3 * n * m) / 65
    sprinklers[3] = (2 * n * m) / 60
    sprinklers[4] = (1 * n * m) / 60
    for i in range(len(sprinklers)):
        sprinklers[i] = int(sprinklers[i])
    return sprinklers


def compute_water_usage(solution):
    """Computes the water usage based on the amount of sprinklers used of each type
    :param ndarray amounts_sprinklers_used: the amount of sprinklers used of each type
    :return int: the water usage"""
    amounts_sprinklers_used = np.zeros(5)
    for i in range(len(solution)):
        if solution[i][2] < 1 or solution[i][2] > 5:
            continue
        amounts_sprinklers_used[int(solution[i][2] - 1)] += 1

    water_usage = amounts_sprinklers_used[0] * 180 + amounts_sprinklers_used[1] * 350
    water_usage += amounts_sprinklers_used[2] * 400 + amounts_sprinklers_used[3] * 650
    water_usage += amounts_sprinklers_used[4] * 800
    return water_usage


def compute_terrain_water_coverage(myterrain, solution):
    """Computes the water coverage of the terrain
    :param ndarray terrain: the terrain
    :return float: the water coverage"""
    terrain = tg.make_copy(myterrain)
    water_coverage = 0
    for sprinkler in solution:
        update_terrain(terrain, sprinkler)
    # compute the water coverage
    for i in range(len(terrain)):
        for j in range(len(terrain[0])):
            water_coverage += abs(terrain[i][j])
    return water_coverage


def fitness_function(terrain, solution, alpha=1.0, beta=1.0):
    """Computes the fitness of a solution
    :param ndarray terrain: the terrain
    :param ndarray solution: the solution
    :param float alpha: weight for water usage (default 1)
    :param float beta: weight for water coverage (default 1)
    :return float: the fitness"""
    # Compute the water usage and the terrain water coverage
    water_usage = compute_water_usage(solution)
    water_coverage = compute_terrain_water_coverage(terrain, solution)
    # Compute the fitness
    fitness = alpha * water_usage + beta * water_coverage
    return fitness


def update_terrain(terrain, sprinkler):
    """Updates the terrain based on the sprinkler
    :param ndarray terrain: the terrain
    :param ndarray sprinkler: the sprinkler
    note: the sprinkler is a vector of 3 elements, the first is the x coordinate, the second is the y coordinate,
    and the third is the type of sprinkler. This last is an integer between 1 and 5, inclusive.
    type is used to define the type of sprinkler, and the amount of water that it will spread
    on the terrain. The amount of water is defined by the following table:
    type 1: irrigates 9 cells with 20 liters each
    type 2: irrigates 25 cells with 14 liters each
    type 3: irrigates 25 cells with 16 liters each
    type 4: irrigates 49 cells with 13 liters each
    type 5: irrigates 49 cells with 12 liters each
    """

    if sprinkler[2] < 1 or sprinkler[2] > 5:
        sprinkler[2] = 0
        sprinkler[0] = 0
        sprinkler[1] = 0
        return
    if sprinkler[2] == 1:
        # subtract 20 from each neighbor
        for i in range(int(sprinkler[0]) - 1, int(sprinkler[0]) + 2):
            for j in range(int(sprinkler[1]) - 1, int(sprinkler[1]) + 2):
                if i >= 0 and j >= 0 and i < len(terrain) and j < len(terrain[0]):
                    terrain[i][j] += -20
    elif sprinkler[2] == 2:
        # subtract 14 from each level 2 neighbor
        for i in range(int(sprinkler[0]) - 2, int(sprinkler[0]) + 3):
            for j in range(int(sprinkler[1]) - 2, int(sprinkler[1]) + 3):
                if i >= 0 and j >= 0 and i < len(terrain) and j < len(terrain[0]):
                    terrain[i][j] += -14
    elif sprinkler[2] == 3:
        for i in range(int(sprinkler[0]) - 2, int(sprinkler[0]) + 3):
            for j in range(int(sprinkler[1]) - 2, int(sprinkler[1]) + 3):
                if i >= 0 and j >= 0 and i < len(terrain) and j < len(terrain[0]):
                    terrain[i][j] += -16
    elif sprinkler[2] == 4:
        for i in range(int(sprinkler[0]) - 3, int(sprinkler[0]) + 4):
            for j in range(int(sprinkler[1]) - 3, int(sprinkler[1]) + 4):
                if i >= 0 and j >= 0 and i < len(terrain) and j < len(terrain[0]):
                    terrain[i][j] += -13
    elif sprinkler[2] == 5:
        for i in range(int(sprinkler[0]) - 3, int(sprinkler[0]) + 4):
            for j in range(int(sprinkler[1]) - 3, int(sprinkler[1]) + 4):
                if i >= 0 and j >= 0 and i < len(terrain) and j < len(terrain[0]):
                    terrain[i][j] += -12


# -----GENERATE SOLUTIONS-------------------------------------------------------
def generate_random_valid_sprinkler(n, m, sprinklers_amount):
    """Generates a random solution to the irrigation problem
    :param int n: the number of rows of the terrain
    :param int m: the number of columns of the terrain
    :return ndarray: the generated sprinkler [x, y, type]"""
    if sum(sprinklers_amount) == 0:
        return np.array([0, 0, 0])  # empty solution

    x = random.randint(0, n - 1)
    y = random.randint(0, m - 1)
    sprinkler_type = random.randint(0, 6)
    if sprinkler_type > 5 or sprinkler_type < 1:
        return np.array([x, y, sprinkler_type])
    while sprinklers_amount[sprinkler_type - 1] == 0:
        sprinkler_type = random.randint(1, 5)
    else:
        sprinklers_amount[sprinkler_type - 1] -= 1
    return np.array([x, y, sprinkler_type])


def generate_random_sprinkler(terrain):
    """Generates a random solution to the irrigation problem
    :param ndarray terrain: the terrain
    :return ndarray: the generated sprinkler [x, y, type]"""
    n = terrain.shape[0]
    m = terrain.shape[1]
    x = random.randint(0, n - 1)
    y = random.randint(0, m - 1)
    sprinkler_type = random.randint(0, 6)
    return np.array([x, y, sprinkler_type])


def generate_random_solution(terrain):
    """Generates a random solution to the irrigation problem
    :param ndarray terrain: the terrain
    :return ndarray: the generated solution matrix with amount of rows equal to the sum of sprinklers
    columns equal to 3, where each row has a sprinkler
    note: all generated solutions are comply with the constraints"""
    n = terrain.shape[0]
    m = terrain.shape[1]
    ammount_sprinklers = compute_sprinkler_amount(n, m)
    rows = int(sum(ammount_sprinklers))
    solution = np.zeros((rows, 3))
    for i in range(rows):
        solution[i] = generate_random_valid_sprinkler(n, m, ammount_sprinklers)
    while not is_solution_valid(solution, terrain):
        for i in range(rows):
            solution[i] = generate_random_valid_sprinkler(n, m, ammount_sprinklers)
    return solution


def generate_random_solutions(number_of_solutions, terrain):
    """Generates a populations of size (number_of_solutions) to the irrigation problem
    each solution is a ndarray of vectors of 3 elements, each vector representing a sprinkler
    the first element is the x coordinate, the second is the y coordinate,
    and the third is the type of sprinkler. Each list must have (<= sum of sprinklers) elements
    :param int number_of_solutions: the number of solutions to be generated
    :param ndarray terrain: the terrain
    :return list: the generated solutions
    """
    solutions = []
    for i in range(number_of_solutions):
        solution = generate_random_solution(terrain)
        solutions.append(solution)
    return solutions


# -----CONSTRAINTS--------------------------------------------------------------


def check_constraint_water_per_cell(terrain):
    """Checks if the water per cell constraint is respected
    all cells must be greater than 0.
    :param ndarray terrain: the terrain
    :return bool: True if the constraint is respected, False otherwise"""
    for i in range(len(terrain)):
        for j in range(len(terrain[i])):
            if terrain[i][j] < 0:
                return False
    return True


def check_valid_sprinklers_sum(solutions, sprinklers):
    """Checks if a solution has a valid amount of sprinklers of each type
    :param ndarray solution: the solution to be checked
    :param int n: the number of rows of the terrain
    :param int m: the number of columns of the terrain
    :return bool: True if the solution is valid, False otherwise"""
    amounts_sprinklers_used = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    # compute the amount of sprinklers used of each type
    for i in range(len(solutions)):
        sprinkler_type = int(solutions[i][2])
        # invalid sprinkler type is considered empty
        if sprinkler_type < 1 or sprinkler_type > 5:
            continue
        amounts_sprinklers_used[sprinkler_type] += 1
    # check if the amount of sprinklers used of each type is less than the amount of sprinklers of each type
    for i in range(1, 6):
        if amounts_sprinklers_used[i] > sprinklers[i - 1]:
            return False
    return True


def check_if_valid_sprinkler(sprinkler, sprinklers):
    """Checks if a sprinkler is valid given the amount of sprinklers of each type
    :param ndarray sprinkler: the sprinkler to be checked (x, y, type)
    :param ndarray sprinklers: the amount of sprinklers of each type
    :return bool: True if the sprinkler is valid, False otherwise
    """
    sprinkler_type = sprinkler[2]
    available_sprinklers = {
        1: sprinklers[0],
        2: sprinklers[1],
        3: sprinklers[2],
        4: sprinklers[3],
        5: sprinklers[4],
    }
    return available_sprinklers.get(sprinkler_type, 0) > 0


def check_type_sprinkler(sprinkler_type):
    if sprinkler_type < 1:
        return 1
    elif sprinkler_type > 5:
        return sprinkler_type % 5
    return sprinkler_type


def check_sprinkler_position(sprinkler, n, m):
    """Checks if the sprinkler position is valid
    if so returns a boolean True
    otherwise returns a boolean False"""
    if sprinkler[0] < 0 or sprinkler[0] >= n:
        return False
    elif sprinkler[1] < 0 or sprinkler[1] >= m:
        return False
    return True


def check_valid_sprinklers_positions(solutions, n, m):
    """Checks if a solution is valid
    :param ndarray solution: the solution to be checked
    :param int n: the number of rows of the terrain
    :param int m: the number of columns of the terrain
    :return bool: True if the solution is valid, False otherwise"""
    for sprinkler in solutions:
        if not check_sprinkler_position(sprinkler, n, m):
            return False
    return True


def is_solution_valid(solution, terrain):
    """Checks if the solution is valid
    :param ndarray solution: the solution to be checked
    :param int n: the number of rows of the terrain
    :param int m: the number of columns of the terrain
    :return bool: True if the solution is valid, False otherwise"""
    valid = True
    sprinklers = compute_sprinkler_amount(terrain.shape[0], terrain.shape[1])
    # check that the water per cell constraint is respected that is, all cells must be greater than 0.
    # and that the amount of sprinklers used of each type is less than the amount of available sprinklers of each type
    # and that that all sprinklers are inside the terrain
    valid = check_valid_sprinklers_sum(
        solution, sprinklers
    )
    valid = valid and check_valid_sprinklers_positions(
        solution, terrain.shape[0], terrain.shape[1]
    )
    return valid
