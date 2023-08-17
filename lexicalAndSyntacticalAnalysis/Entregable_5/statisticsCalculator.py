# Copyright: GNU General Public License
# Authors: 
# Antonio Badilla Olivas - B80874
# Gabriel Molina Bulgarelli - C14826
# Brandon Alonso Mora Umaña - C15179

import numpy as np
import matplotlib.pyplot as plt
from DataStructure import Site, Record
from datetime import datetime, timedelta

class Statistics:
    def __init__(self, sites, topics, regions):
        """@brief: Constructor of the class
        @param sites: is a np.array of sites
        """
        self.sites = sites
        self.topics = topics
        self.regions = regions

    def get_sites(self):
        """@brief: Method to get the sites
        @return: np.array of sites
        """
        return self.sites

    def most_visited_by_region(self, region_to_search):
        """@brief: Method to get the three most visited sites in a region
        @param regionToSearch: is the region to search
        @return: pair of three sites with three numbers of visits
        """
        region_to_search = region_to_search.lower()
        sites = self.get_sites()
        site_records_containing_region = []

        for site in sites:
            for record in site.records:
                if record.region == region_to_search:
                    site_records_containing_region.append((site.title, record.num_visits))
        site_records_containing_region.sort(key=lambda x: x[1], reverse=True)
        return site_records_containing_region[:3]
    # END METHOD most_visited_by_region

    def most_least_visited_topics_in_timeframe(self, initial_date, final_date):
        """@brief: Method to get the three most and least visited topics in a timeframe
        @param initialDate: is the initial date of the timeframe
        @param finalDate: is the final date of the timeframe
        @return: pair of three topics with three numbers of visits
        """
        sites = self.get_sites()
        topics = dict()
        for site in sites:
            for record in site.records:
                low_bound = initial_date <= record.start_date
                up_bound = record.end_date <= final_date
                if low_bound and up_bound:
                    for topic in site.topics:
                        if topic in topics:
                            topics[topic] += record.num_visits
                        else:
                            topics[topic] = record.num_visits
        topics = sorted(topics.items(), key=lambda x: x[1], reverse=True)
        # plot the topics in a bar chart
        # first make the bars based on the values of visits
        plt.bar(range(len(topics)), [val[1] for val in topics], align='center')
        # then add the labels base on the keys of the dictionary
        plt.xticks(range(len(topics)), [val[0] for val in topics])
        # rotate the labels 90 degrees so they fit
        plt.xticks(rotation=90)
        plt.xlabel('Temas')
        plt.ylabel('Número de Visitas')
        plt.title(f'Temas más y menos visitados en el período de tiempo: {initial_date} to {final_date}')
        plt.grid()
        plt.show()
        return topics[:3], topics[-3:]
    # END most_least_visited_topics_in_timeframe

    def get_topic_visits(self, sites, target_topic):
        """@brief: Method to get a list of pairs having midpoint date and number of visits of a topic
        @param sites: is a np.array of sites
        @param target_topic: is the topic to search
        """
        topic_visits = []  # Initialize an empty list to store the visits data
        for site in sites:
            if target_topic in site.topics:
                for record in site.records:
                    start_date = record.start_date
                    end_date = record.end_date
                    midpoint_date = start_date + (end_date - start_date) / 2
                    topic_visits.append((midpoint_date, record.num_visits))
        return topic_visits
    # END get_topic_visits

    def plot_visit_evolution_by_topic(self, target_topic):
        """@brief: Method to plot the evolution of visits for a topic
        @details: uses midpoints of the dates of the records to plot the evolution
        @param target_topic: is the topic to search
        """
        target_topic = target_topic.lower()
        topic_visits = self.get_topic_visits(self.sites, target_topic)
        topic_visits.sort(key=lambda x: x[0])  # Sort by date
        # Unpack the pairs in the topic_visits list into separate lists of dates and visits
        try:
          dates, visits = zip(*topic_visits)
          # Plot the evolution of visits
          # first convert the dates to matplotlib format
          # dates = [datetime.strftime(date, '%Y-%m-%d') for date in dates] decoment this line if ploting by date is not working
          plt.plot(dates, visits)
          plt.xlabel('Fecha')
          plt.ylabel('Número de Visitas')
          plt.title(f'Evolución de Visitas por Tema: {target_topic}')
          plt.grid()
          plt.show()
        except:
          print("No existe el tema")
   # END plot_visit_evolution_by_topic

    def topic_list_by_timeframe(self, initialDate, finalDate):
        """@brief: Method to get the list of topics in a timeframe
        @param initialDate: is the initial date of the timeframe
        @param finalDate: is the final date of the timeframe
        @return: list of topics in the timeframe
        """
        sites = self.get_sites()
        topicsInTimeframe = []

        # Iterate over all sites
        # For each site, iterate over all records
        # If the record is in the timeframe, add the topics to the list

        for site in sites:
            for record in site.records:
                upperBound = record.end_date <= finalDate
                lowerBound = initialDate <= record.start_date
                if upperBound and lowerBound:
                    for topic in site.topics:
                        if topic not in topicsInTimeframe:
                            topicsInTimeframe.append(topic)  
                    break

        return topicsInTimeframe



# END statisticsCalculator