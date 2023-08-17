import matplotlib.pyplot as plt
import time
import numpy as np
import Terrain_generator as tg
import Objective_and_Restrictions as obr
from woa import WOA
from gredy_solution import greedy_algorithm
import csv


def main():
    sizes = [10, 20, 30, 40, 50, 60] # Terrain sizes to test
    
    woa_times = []
    woa_fitness = []
    woa_water_usage = []
    woa_water_coverage = []

    greedy_times = []
    greedy_fitness = []
    greedy_water_coverage = []
    greedy_water_usage = []

    alpha = 0.5
    beta = 1
    
    brute_times = [] 
    brute_fitness = [] 
    brute_water_coverage = [] 
    brute_water_usage = [] 
    for size in sizes:
        terrain = tg.generate_terrain(size, size)
        copy = tg.make_copy(terrain)   

        # Run WOA
        start_time = time.time()
        a = np.random.uniform(0.0, 1.0, size=3)
        b = np.random.uniform(0.0, 1.0, size=3)
        l = np.random.uniform(0.0, 1.0, size=3)
        iterations = 1000
        number_search_agents = 20
        sprinklers = obr.compute_sprinkler_amount(terrain.shape[0], terrain.shape[1])
        woa = WOA(terrain, a, b, l, iterations, number_search_agents, alpha, beta)
        woa.optimize()
        end_time = time.time()
        woa_times.append(end_time - start_time)
        woa_fitness.append(obr.fitness_function(tg.make_copy(copy), woa.search_agents[0]))
        woa_water_usage.append(obr.compute_water_usage(woa.search_agents[0]))
        woa_water_coverage.append(obr.compute_terrain_water_coverage(tg.make_copy(copy), woa.search_agents[0]))
        # Run greedy algorithm
        start_time = time.time()
        greedy_result = greedy_algorithm(tg.make_copy(copy), sprinklers, alpha, beta)
        end_time = time.time()
        greedy_times.append(end_time - start_time)
        greedy_fitness.append(obr.fitness_function(tg.make_copy(copy), greedy_result)) 
        greedy_water_usage.append(obr.compute_water_usage(greedy_result))
        greedy_water_coverage.append(obr.compute_terrain_water_coverage(tg.make_copy(copy), greedy_result))
    #for size in sizeForBruteForce:
        # Run brute force
        # start_time = time.time()
        # brute_result = greedy_algorithm(tg.make_copy(copy), sprinklers, alpha, beta)
        # end_time = time.time()
        # brute_times.append(end_time - start_time)
        # brute_fitness.append(obr.fitness_function(tg.make_copy(copy), brute_result)) 
        # brute_water_usage.append(obr.compute_water_usage(brute_result))
        # brute_water_coverage.append(obr.compute_terrain_water_coverage(tg.make_copy(copy), brute_result))
    
    # Plot times
    plt.figure()
    plt.plot(sizes, woa_times, label='WOA')
    plt.plot(sizes, greedy_times, label='Greedy')
    # plt.plot(sizes, brute_times, label='Brute')
    plt.xlabel('Terrain size')
    plt.ylabel('Execution time (s)')
    plt.legend()
    plt.show()

    # Plot fitness results
    plt.figure()
    plt.plot(sizes, woa_fitness, label='WOA')
    plt.plot(sizes, greedy_fitness, label='Greedy')
    # plt.plot(sizes, brute_times, label='Brute')
    plt.xlabel('Terrain size')
    plt.ylabel('Fitness function result')
    plt.legend()
    plt.show()

    #print water_coverage 
    plt.figure()
    plt.plot(sizes, woa_water_coverage, label='WOA')
    plt.plot(sizes, greedy_water_coverage, label='Greedy')
    # plt.plot(sizes, brute_times, label='Brute')
    plt.xlabel('Terrain size')
    plt.ylabel('Water coverage')
    plt.legend()
    plt.show()

    #print water_usage
    plt.figure()
    plt.plot(sizes, woa_water_usage, label='WOA')
    plt.plot(sizes, greedy_water_usage, label='Greedy')
    # plt.plot(sizes, brute_times, label='Brute')
    plt.xlabel('Terrain size')
    plt.ylabel('Water usage')
    plt.legend()
    plt.show()

# Save results in a CSV file
    with open('results.csv', 'w', newline='') as csvfile:
        fieldnames = ['Size', 'WOA_time', 'Greedy_time', 'WOA_fitness', 'Greedy_fitness',
                      'WOA_water_coverage', 'Greedy_water_coverage', 'WOA_water_usage', 'Greedy_water_usage']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for size, w_time, g_time, w_fit, g_fit, w_cov, g_cov, w_usage, g_usage in zip(sizes, woa_times, greedy_times, woa_fitness, greedy_fitness, woa_water_coverage, greedy_water_coverage, woa_water_usage, greedy_water_usage):
            writer.writerow({'Size': size, 'WOA_time': w_time, 'Greedy_time': g_time, 'WOA_fitness': w_fit, 
                             'Greedy_fitness': g_fit, 'WOA_water_coverage': w_cov, 'Greedy_water_coverage': g_cov, 
                             'WOA_water_usage': w_usage, 'Greedy_water_usage': g_usage})
    # with open('results.csv', 'w', newline='') as csvfile:
    #     fieldnames = ['Size', 'WOA_time', 'Greedy_time', 'Brute_time', 'WOA_fitness', 'Greedy_fitness', 'Brute_fitness', 
    #                   'WOA_water_coverage', 'Greedy_water_coverage', 'Brute_water_coverage' 'WOA_water_usage', 'Greedy_water_usage', 'Brute_water_coverage']
    #     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    #     writer.writeheader()
    #     for size, w_time, g_time, b_time, w_fit, g_fit, b_fit, w_cov, g_cov, b_cov, w_usage, g_usage, b_usage in zip(sizes, woa_times, greedy_times, brute_times, woa_fitness, greedy_fitness, brute_fitness, woa_water_coverage, greedy_water_coverage, brute_water_coverage, woa_water_usage, greedy_water_usage, brute_water_usage):
    #         writer.writerow({'Size': size, 'WOA_time': w_time, 'Greedy_time': g_time, 'Brute_time': b_time, 
    #                          'WOA_fitness': w_fit, 'Greedy_fitness': g_fit, 'Brute_fitness': b_fit,
    #                          'WOA_water_coverage': w_cov, 'Greedy_water_coverage': g_cov, 'Brute_water_coverage': b_cov,
    #                          'WOA_water_usage': w_usage, 'Greedy_water_usage': g_usage, 'Brute_water_usage': b_usage})

if __name__ == "__main__":
    main()

