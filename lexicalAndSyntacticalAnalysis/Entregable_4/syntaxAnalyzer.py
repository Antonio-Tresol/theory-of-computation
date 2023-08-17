# copyrigth: gnu general public license
# authors: Antonio Badilla Olivas - B80874
# Brandon Alonso Mora Umaña - C15179
# Gabriel Molina Bulgarelli-C14826
from DataStructure import Record, Site
import numpy as np

# Define the free context grammar

def p_data(p):
    'data : DATA_BEGIN info DATA_END'
    p[0] = p[2]
#END p_data

def p_info(p):
    'info : topics regions sites'
    list_of_topics = p[1]
    list_of_regions = p[2]
    list_of_sites = p[3]
    list_of_information = list_of_topics, list_of_regions, list_of_sites
    p[0] = list_of_information
#END p_info

def p_topics(p):
    'topics : TOPICS_START topic TOPICS_END'
    p[0] = p[2] # Return the list of topics
#END p_topics

def p_topic(p):
    '''topic : TOPIC_START REGION_TITLE_TOPIC TOPIC_END topic
            | TOPIC_START REGION_TITLE_TOPIC TOPIC_END'''
    my_topic = p[2] # Get the topic
    if len(p) == 5:
        old_topics = p[4] # Get the list of topics
    else:
        old_topics = np.array([])
    # Add the new topic to the list
    newRecords = np.append(old_topics, my_topic.lower())
    p[0] = newRecords # Return the new list of topics
#END p_topic

def p_title(p):
     'title : TITLE_START REGION_TITLE_TOPIC TITLE_END'
     # Found a new title, save it to the p object
     p[0] = p[2]
#END p_title

def p_regions(p):
     'regions : REGIONS_START region REGIONS_END'
     p[0] = p[2] # Return the list of regions
#END p_regions

def p_region(p):
    '''region : REGION_START REGION_TITLE_TOPIC REGION_END region
            | REGION_START REGION_TITLE_TOPIC REGION_END'''
    myRegion = p[2] # Get the region
    if len(p) == 5:
        old_regions = p[4] # Get the list of regions
    else:
        old_regions = np.array([])
    new_regions = np.append(old_regions, myRegion.lower()) # Add the new region to the list
    p[0] = new_regions # Return the new list of regions
#END p_region

def p_sites(p):
    'sites : SITES_START site SITES_END'
    p[0] = p[2] # Return the list of sites
#END p_sites

def p_site(p):
    '''site : SITE_START url title topics records SITE_END site
            | SITE_START url title topics records SITE_END'''
    my_site = Site(p[2], p[3], p[4], p[5]) # Create a new site
    if len(p) == 8:
        old_sites = p[7] # Get the list of sites
    else:
        old_sites = np.array([])
    new_sites = np.append(old_sites, my_site) # Add the new site to the list
    p[0] = new_sites # Return the new list of sites
#END p_site

def p_url(p):
    'url : URL_START URL URL_END'
    p[0] = p[2]
#END p_url
    
def p_records(p):
    'records : RECORDS_START record RECORDS_END'
    p[0] = p[2] # Return the array of records
#END p_records

def p_record(p):
    '''record : RECORD_START initialdate finaldate region numbervisits RECORD_END record
            | RECORD_START initialdate finaldate region numbervisits RECORD_END'''
    my_record = Record(p[2], p[3], p[4], p[5]) # Create a new record
    if len(p) == 8:
        past_records = p[7] # Get the array of records
    else:
        past_records = np.array([])
    new_records = np.append(past_records, my_record) # Add the new record to the array
    p[0] = new_records # Return the array
#END p_record

def p_initialdate(p):
    'initialdate : INIT_DATE_START DATE INIT_DATE_END'
    p[0] = p[2]
    # print("Found initial date: " + p[0].strftime("%d-%m-%Y"))
#END p_initialdate

def p_finaldate(p):
    'finaldate : FINAL_DATE_START DATE FINAL_DATE_END'
    p[0] = p[2]
    # print("Found final date: " + p[0].strftime("%d-%m-%Y"))
#END p_finaldate

def p_numbervisits(p):
    'numbervisits : NUMBER_OF_VISITS_START NUMBER_VISITS NUMBER_OF_VISITS_END'
    p[0] = p[2] # Return the number of visits
#END p_numbervisits

def p_error(p):
    print("Syntax error in input!" + str(p))
#END p_error