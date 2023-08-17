# copyrigth: gnu general public license
# authors: Antonio Badilla Olivas - B80874
# Brandon Alonso Mora Umaña - C15179
# Gabriel Molina Bulgarelli-C14826
import ply.lex as lex
import ply.yacc as yacc
from lexicalAnalyzer import *
from syntaxAnalyzer import *

def build_lexer():
    """
    @brief: Build and return the lexer.
    @return: The lexer object.
    """
    return lex.lex()
#END build_lexer

def build_parser():
    """
    @brief: Build and return the parser.
    @return: The parser object.
    """
    return yacc.yacc()
#END build_parser

def read_file(file_path):
    """
    @brief: Read the contents of the file at the given file_path
    @param file_path (str): The path of the file to be read.
    @return: The contents of the file as a string.
    """
    with open(file_path, "r", encoding='utf-8') as file:
        data = file.read()
    return data
#END read_file

def tokenize_and_parse(data):
    """
    @brief: Tokenize and parse the given data using the lexer and parser.
    @param data (str): The data to be tokenized and parsed.
    @return: A list containing the parsed topics, regions, and sites.
    """
    lexer = build_lexer()
    parser = build_parser()
    all_data = parser.parse(data)  # Parser calls the lexer to get the tokens
    return all_data
#END tokenize_and_parse

def print_collected_data(list_of_topics, list_of_regions, list_of_sites):
    """
    @brief: Print the results: topics, regions, and sites.
    @param list_of_topics (list): The list of topics.
    @param list_of_regions (list): The list of regions.
    @param list_of_sites (list): The list of sites.
    """
    print("Topics: " + str(list_of_topics))
    print("Regions: " + str(list_of_regions))
    for site in list_of_sites:
        print(site)
#END print_collected_data

def main():
    """
    @brief: Main program flow:
            1. Read the input file.
            2. Tokenize and parse the data.
            3. Print the data collected (topics, regions, and sites).
    """
    file_path = "Tarea1/data/Datos.xml"
    data = read_file(file_path)
    all_data = tokenize_and_parse(data)
    list_of_topics = all_data[0]
    list_of_regions = all_data[1]
    list_of_sites = all_data[2]
    print_collected_data(list_of_topics, list_of_regions, list_of_sites)
#END main

if __name__ == "__main__":
    main()
