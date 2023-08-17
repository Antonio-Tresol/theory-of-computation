import Objective_and_Restrictions as obr
import numpy as np
import Terrain_generator as tg


def greedy_algorithm(terrain, sprinklers, alpha=0.5, beta=1):
    """
    This function implements a greedy algorithm to solve a sprinkler placement problem.
    It takes in two arguments:
    - terrain: a 2D numpy array representing the terrain where the sprinklers will be placed.
    - sprinklers: a 1D numpy array representing the number of available sprinklers of each type.
    The function returns a list of numpy arrays, where each array represents the position and type of a placed sprinkler.
    """
    solution = []
    best_fitness = float("inf")
    original_terrain = tg.make_copy(terrain)
    while True:
        best_sprinkler = None

        for i in range(len(terrain)):
            for j in range(len(terrain[0])):
                for sprinkler_type in range(1, len(sprinklers) + 1):
                    candidate_sprinkler = np.array([i, j, sprinkler_type])
                    if obr.check_if_valid_sprinkler(
                        candidate_sprinkler, sprinklers
                    ) and obr.is_solution_valid(solution + [candidate_sprinkler], terrain):
                        fitness = obr.fitness_function(
                            original_terrain, solution + [candidate_sprinkler], alpha, beta
                        )
                        if fitness < best_fitness:
                            best_fitness = fitness
                            best_sprinkler = candidate_sprinkler
        
        if best_sprinkler is None:
            break
        else:
            obr.update_terrain(terrain, best_sprinkler)

        solution.append(best_sprinkler.tolist())
        sprinklers[best_sprinkler[2] - 1] -= 1

    return np.array(solution)