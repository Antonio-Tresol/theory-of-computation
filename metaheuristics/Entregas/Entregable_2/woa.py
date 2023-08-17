import Objective_and_Restrictions as obr
import random as rand
import numpy as np


class WOA:
    def __init__(self, terrain, a, b, l, iterations, number_search_agents, alpha=0.5, beta=1):
        # a is a matrix of the same dimensions as of the search agents matrix
        self.a = a
        self.b = b
        self.L = l
        self.A = None
        self.C = None
        self.n_search_agents = number_search_agents
        self.iterations = iterations
        self.terrain = terrain
        self.alpha = alpha
        self.beta = beta
        # each search agent (solution) is a matriz of 3 columns and n_search_agents rows
        # each row represents of the matrix represents an sprinkler
        # so search_agents is a list of matrices, eahc matrix is a solution
        self.search_agents = obr.generate_random_solutions(self.n_search_agents, self.terrain)
        self.rank_solutions()

    # ge to closer to each of the spriklers in a solution.
    # go one by one
    def rank_solutions(self):
        """Ranks the search agents by their fitness"""
        self.search_agents.sort(key=lambda x: obr.fitness_function(self.terrain, x))

    def _compute_A(self):
        r = np.random.uniform(0.0, 1.0, size=3)
        return (2.0 * np.multiply(self.a, r)) - self.a

    def _compute_C(self):
        return 2.0 * np.random.uniform(0.0, 1.0, size=3)

    def _encircle(self, sol, best_sol, A):
        D = self._encircle_D(sol, best_sol)
        return best_sol - np.multiply(A, D)

    def _encircle_D(self, sol, best_sol):
        C = self._compute_C()
        D = np.linalg.norm(np.multiply(C, best_sol) - sol)
        return D

    def _search(self, sol, rand_sol, A):
        D = self._search_D(sol, rand_sol)
        return rand_sol - np.multiply(A, D)

    def _search_D(self, sol, rand_sol):
        C = self._compute_C()
        return np.linalg.norm(np.multiply(C, rand_sol) - sol)

    def _attack(self, sol, best_sol):
        D = np.linalg.norm(best_sol - sol)
        L = np.random.uniform(-1.0, 1.0, size=3)
        return (np.multiply(np.multiply(D, np.exp(self.b * L)), np.cos(2.0 * np.pi * L)) + best_sol)

    def optimize(self):
        """Runs the optimization algorithm"""
        for i in range(self.iterations):
            # Update a, A, C, and p at the start of each iteration
            self.a = 2.0 - i * (2.0 / self.iterations)
            self.A = self._compute_A()
            self.C = self._compute_C()
            p = np.random.uniform(0.0, 1.0, size=self.n_search_agents)
            # Get the current best solution
            self.rank_solutions()
            best_sol = self.search_agents[0]
            # For each solution
            for j in range(self.n_search_agents):
                solution = self.search_agents[j]
                new_solution = np.zeros((len(solution), 3))
                # Encircle
                if p[j] < 0.5:
                    norm_A = np.linalg.norm(self.A)
                    if norm_A < 1.0:
                        for i in range(len(solution)):
                            new_solution[i] = self._encircle(solution[i], best_sol[i], self.A)
                    else:
                        for i in range(len(solution)):
                            random_sprikler = obr.generate_random_sprinkler(self.terrain)
                            new_solution[i] = self._search(solution[i], random_sprikler, self.A)
                else:
                    for i in range(len(solution)):
                        new_solution[i] = self._attack(solution[i], best_sol[i])

                if not obr.is_solution_valid(new_solution, self.terrain):
                    continue

                # Replace old solution with new one if the new one is better
                if obr.fitness_function(new_solution, self.terrain, self.alpha, self.beta) > obr.fitness_function(solution, self.terrain, self.alpha, self.beta):
                    self.search_agents[j] = new_solution
            # Update the best solution
            self.rank_solutions()
            best_sol = self.search_agents[0]
