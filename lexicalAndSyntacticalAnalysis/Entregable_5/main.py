# Copyright: GNU General Public License
# Authors: 
# Antonio Badilla Olivas - B80874
# Gabriel Molina Bulgarelli - C14826
# Brandon Alonso Mora Umaña - C15179

import PySimpleGUI as sg
import ply.lex as lex
import ply.yacc as yacc
from lexicalAnalyzer import *
from syntaxAnalyzer import *
from statisticsCalculator import *

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

def region_layout(names):
    region_layout = [
        [sg.Text("", key='-TXT-', expand_x=True, font=("Arial Bold", 14))],
        [sg.Text('Páginas más Visitadas en una Región', font=('Chakra Petch', 16), justification='center')],
        [sg.Listbox(names, size=(40, 4), font=('Chakra Petch', 8), expand_y=True, no_scrollbar=True, enable_events=True, key='-LIST-')],
        [sg.Text("", key='-TXT-', expand_x=True, font=("Arial Bold", 14))],
        [sg.Text("Escriba su región:"), sg.InputText(size=(16, 2))],
        [sg.Text("", key='-TXT-', expand_x=True, font=("Arial Bold", 14))],
        [sg.Button('Encontrar páginas más visitadas en la región'), sg.Exit()],
        [sg.Text("", key='-TXT-', expand_x=True, font=("Arial Bold", 14))]
    ]
    return sg.Window('', region_layout, resizable=True, finalize=True, element_justification='c')

def mostleast_topics_layout(names, names1):
    mostleast_topics_layout = [
      [sg.Text("", key='-TXT-', expand_x=True, font=("Arial Bold", 14))],
      [sg.Text('Temas Acumulados por Periodo', size=(16, 2), font=('Chakra Petch', 16), justification='center')],
      [sg.Text("", key='-TXT-', expand_x=True, font=("Arial Bold", 14))],
      [sg.Text("Más Visitados", key='-TXT-', expand_x=True, font=("Arial Bold", 14)), sg.Text("Menos Visitados", key='-TXT-', expand_x=True, font=("Arial Bold", 14))],
      [sg.Listbox(names, size=(25, 4), font=('Chakra Petch', 8), expand_y=True, no_scrollbar=True, enable_events=True, key='-MOSTLIST-'), sg.Listbox(names1, size=(25, 4), font=('Chakra Petch', 8), expand_y=True, no_scrollbar=True, enable_events=True, key='-LEASTLIST-')],
      [sg.Text("", key='-TXT-', expand_x=True, font=("Arial Bold", 14))],
      [sg.Input(key='-Fecha Inicial-', size=(10,1)), sg.CalendarButton("Fecha Inicial", close_when_date_chosen=True,  target='-Fecha Inicial-', no_titlebar=False, format='%Y-%m-%d')],
      [sg.Input(key='-Fecha Final-', size=(10,1)), sg.CalendarButton(" Fecha Final", close_when_date_chosen=True,  target='-Fecha Final-', no_titlebar=False, format='%Y-%m-%d')],
      [sg.Text("", key='-TXT-', expand_x=True, font=("Arial Bold", 14))],
      [sg.Button('Encontrar Temas en el Periodo'), sg.Exit()],
      [sg.Text("", key='-TXT-', expand_x=True, font=("Arial Bold", 14))]
    ]
    return sg.Window('', mostleast_topics_layout, resizable=True, finalize=True, element_justification='c')

def all_topics_layout(names):
    all_topics_layout = [
      [sg.Text("", key='-TXT-', expand_x=True, font=("Arial Bold", 14))],
      [sg.Text('Temas Acumulados por Periodo', size=(16, 2), font=('Chakra Petch', 16), justification='center')],
      [sg.Text("", key='-TXT-', expand_x=True, font=("Arial Bold", 14))],
      [sg.Listbox(names, size=(30, 50), font=('Chakra Petch', 8), expand_y=True, no_scrollbar=True, enable_events=True, key='-LIST-')],
      [sg.Text("", key='-TXT-', expand_x=True, font=("Arial Bold", 14))],
      [sg.Input(key='-Fecha Inicial-', size=(10,1)), sg.CalendarButton("Fecha Inicial", close_when_date_chosen=True,  target='-Fecha Inicial-', no_titlebar=False, format='%Y-%m-%d')],
      [sg.Input(key='-Fecha Final-', size=(10,1)), sg.CalendarButton(" Fecha Final", close_when_date_chosen=True,  target='-Fecha Final-', no_titlebar=False, format='%Y-%m-%d')],
      [sg.Text("", key='-TXT-', expand_x=True, font=("Arial Bold", 14))],
      [sg.Button('Encontrar Temas en el Periodo'), sg.Exit()],
      [sg.Text("", key='-TXT-', expand_x=True, font=("Arial Bold", 14))]
    ]
    return sg.Window('', all_topics_layout, resizable=True, finalize=True, element_justification='c')

def evolution_layout(names):
    evolution_layout = [
      [sg.Text("", key='-TXT-', expand_x=True, font=("Arial Bold", 14))],
      [sg.Text('Evolución de Tema por Visitas', size=(16, 2), font=('Chakra Petch', 16), justification='center')],
      [sg.Text("", key='-TXT-', expand_x=True, font=("Arial Bold", 14))],
      [sg.Text("Escriba su tema:"), sg.InputText(size=(16, 2))],
      [sg.Text("", key='-TXT-', expand_x=True, font=("Arial Bold", 14))],
      [sg.Button('Encontrar evolución de visitas del tema'), sg.Exit()],
      [sg.Text("", key='-TXT-', expand_x=True, font=("Arial Bold", 14))]
    ]
    return sg.Window('', evolution_layout, resizable=True, finalize=True, element_justification='c')


def graphic_interface(statistics):
    sg.theme('DarkBlue16')
    clicking=[['Menu Principal',
              ['Páginas por Zona',
              'Visita de Temas por Periodo',
              'Temas Acumulados por Periodo',
              'Visitas por Temas']]]
    names=[]
    names1=[]
    main_layout = [
        [sg.Menu(clicking, key='-BMENU-'), sg.Text("", key='-TXT-', expand_x=True, font=("Arial Bold", 14))],
        [sg.Text("", key='-TXT-', expand_x=True, font=("Arial Bold", 14))],
        [sg.Text('Estadísticas de Páginas Web', size=(16, 2), font=('Chakra Petch', 15), justification='center')],
        [sg.Text("", key='-TXT-', expand_x=True, font=("Arial Bold", 14))],
        [sg.Text('Integrantes:')],
        [sg.Text('Antonio Badilla Olivas - B80874\nGabriel Molina Bulgarelli - C14826\nBrandon Alonso Mora Umaña - C15179', justification='center')],
        [sg.Text("", key='-TXT-', expand_x=True, font=("Arial Bold", 14))],
        [sg.Exit()]
    ]

    window = sg.Window('', main_layout, resizable=True, element_justification='c')
    pagina = 0
    while True:
      event, values = window.read()
      if event in (sg.WIN_CLOSED, 'Exit'):
          break
      if event == 'Páginas por Zona':
          pagina = 1
      elif event == 'Visita de Temas por Periodo':
          pagina = 2
      elif event == 'Temas Acumulados por Periodo':
          pagina = 3
      elif event == 'Visitas por Temas':
          pagina = 4
      if pagina == 1:
        window1 = region_layout([])
        while True:
          if event in (sg.WIN_CLOSED, 'Exit'):
            window1.close()
            break
          event, values = window1.read()
          if event == 'Encontrar páginas más visitadas en la región':
              names = statistics.most_visited_by_region(values[0])
              window1['-LIST-'].update(names)
      elif pagina == 2:
        window2 = mostleast_topics_layout([],[])
        while True:
          if event in (sg.WIN_CLOSED, 'Exit'):
            window2.close()
            break
          event, values = window2.read()
          if event == 'Encontrar Temas en el Periodo':
              names, names1 = statistics.most_least_visited_topics_in_timeframe(date.fromisoformat(values['-Fecha Inicial-']), date.fromisoformat(values['-Fecha Final-']))
              window2['-MOSTLIST-'].update(names)
              window2['-LEASTLIST-'].update(names1)
      elif pagina == 3:
        window3 = all_topics_layout([])
        while True:
          if event in (sg.WIN_CLOSED, 'Exit'):
            window3.close();
            break
          event, values = window3.read()
          if event == 'Encontrar Temas en el Periodo':
              names = statistics.topic_list_by_timeframe(date.fromisoformat(values['-Fecha Inicial-']), date.fromisoformat(values['-Fecha Final-']))
              window3['-LIST-'].update(names)
      elif pagina == 4:
        window4 = evolution_layout([])
        while True:
          if event in (sg.WIN_CLOSED, 'Exit'):
            window4.close();
            break
          event, values = window4.read()
          if event == 'Encontrar evolución de visitas del tema':
            statistics.plot_visit_evolution_by_topic(values[0])
    window.close()

def main():
    """
    @brief: Main program flow:
            1. Read the input file.
            2. Tokenize and parse the data.
            3. Print the data collected (topics, regions, and sites).
    """
    file_path = "../data/Datos.xml"
    data = read_file(file_path)
    all_data = tokenize_and_parse(data)
    list_of_topics = all_data[0]
    list_of_regions = all_data[1]
    list_of_sites = all_data[2]
    statistics =  Statistics(list_of_sites, list_of_regions, list_of_topics)
    graphic_interface(statistics)
    
#END main

if __name__ == "__main__":
    main()
