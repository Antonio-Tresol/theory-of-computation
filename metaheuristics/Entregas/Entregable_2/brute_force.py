import Objective_and_Restrictions as obr
import numpy as np

def brute_force_algorithm(terrain, sprinklers, alpha=0.5, beta=1):
    """
    This function implements a brute-force algorithm to solve a sprinkler placement problem.
    It takes in two arguments:
    - terrain: a 2D numpy array representing the terrain where the sprinklers will be placed.
    - sprinklers: a 1D numpy array representing the number of available sprinklers of each type.
    The function returns a list of numpy arrays, where each array represents the position and type of a placed sprinkler.
    """
    best_solution = None
    best_fitness = float("inf")
    original_terrain = tg.make_copy(terrain)

    def generate_sprinkler_combinations(terrain, sprinklers):
        if len(sprinklers) == 0:
            yield []
        else:
            sprinkler_type = len(sprinklers)
            remaining_sprinklers = sprinklers[:-1]
            for i in range(len(terrain)):
                for j in range(len(terrain[0])):
                    candidate_sprinkler = np.array([i, j, sprinkler_type])
                    if obr.check_if_valid_sprinkler(candidate_sprinkler, sprinklers) and obr.is_solution_valid([candidate_sprinkler], terrain):
                        for combination in generate_sprinkler_combinations(terrain, remaining_sprinklers):
                            yield combination + [candidate_sprinkler]


    for combination in generate_sprinkler_combinations(terrain, sprinklers):
        current_solution = combination
        current_fitness = obr.fitness_function(original_terrain, current_solution, alpha, beta)
        if current_fitness < best_fitness:
            best_fitness = current_fitness
            best_solution = current_solution

    return np.array(best_solution)