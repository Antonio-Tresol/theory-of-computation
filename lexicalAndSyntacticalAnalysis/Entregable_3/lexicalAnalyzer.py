import ply.lex as lex
from datetime import date

# This is a list of all the tokens that we are interested in.  It is used by the lexer.
tokens = (
    'DATA_BEGIN',
    'DATA_END',
    'TOPICS_START',
    'TOPICS_END',
    'TOPIC_START',
    'TOPIC_END',
    'REGIONS_START',
    'REGIONS_END',
    'REGION_START',
    'REGION_END',
    'SITES_START',
    'SITES_END',
    'SITE_START',
    'SITE_END',
    'TITLE_START',
    'TITLE_END',
    'URL_START',
    'URL_END',
    'URL',	
    'INIT_DATE_START',
    'INIT_DATE_END',
    'FINAL_DATE_START',
    'FINAL_DATE_END',
    'NUMBER_OF_VISITS_START',
    'NUMBER_OF_VISITS_END',
    'RECORDS_START',
    'RECORDS_END',
    'RECORD_START',
    'RECORD_END',
    'NUMBER_VISITS',
    'REGION_TITLE_TOPIC',
    'DATE'
)
 
# Regular expression rules for simple tokens
t_DATA_BEGIN = r'<data>'
t_DATA_END = r'</data>'
t_TOPICS_START = r'<topics>'
t_TOPICS_END = r'</topics>'
t_TOPIC_START = r'<topic>'
t_TOPIC_END = r'</topic>'
t_REGIONS_START = r'<regions>'
t_REGIONS_END = r'</regions>'
t_REGION_START = r'<region>'
t_REGION_END = r'</region>'
t_SITES_START = r'<sites>'
t_SITES_END = r'</sites>'
t_SITE_START = r'<site>'
t_SITE_END = r'</site>'
t_TITLE_START = r'<title>'
t_TITLE_END = r'</title>'
t_URL_START = r'<url>'
t_URL_END = r'</url>'
t_INIT_DATE_START = r'<initial-date>'
t_INIT_DATE_END = r'</initial-date>'
t_FINAL_DATE_START = r'<final-date>'
t_FINAL_DATE_END = r'</final-date>'
t_NUMBER_OF_VISITS_START = r'<number-of-visits>'
t_NUMBER_OF_VISITS_END = r'</number-of-visits>'
t_RECORDS_START = r'<records>'
t_RECORDS_END = r'</records>'
t_RECORD_START = r'<record>'
t_RECORD_END = r'</record>'


# Priority given to check before date and number visits so its correctly read
t_REGION_TITLE_TOPIC = r'[\d\w\-À-ÿ’:,.|()¿?¡!\\+\'\" ]+'
t_URL = r'(?<=<url>)(http(s)?:\/\/)?(www\.)?[a-zA-Z0-9\-]+(\.[a-zA-Z0-9\-]+)+([\w\d#-+&@#\/%=~_|$?!:,.-]*)*' 

# rule so we can track line numbers
def t_newline(t):
     r'\n+'
     t.lexer.lineno += len(t.value)
 
# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
     print("Illegal character '%s'" % t.value[0])
     t.lexer.skip(1)

# Reads date in the correct format
def t_DATE(t):
     r'(0?[1-9]|[12]\d|3[0-2])-(0?[1-9]|1[0-2])-(1\d{3}|20[01]\d|202[0-3])'
     return t

# Read number of visits in millions
def t_NUMBER_VISITS(t):
     r'(?<=<number-of-visits>)[\d]+([.][\d]*)?'
     return t

# Build the lexer
lexer = lex.lex()

# Define the free context grammar

def p_data(p):
     'data : DATA_BEGIN info DATA_END'
     print("Found data")

def p_info(p):
     'info : topics regions sites'
     print("Found info")

def p_topics(p):
     'topics : TOPICS_START topic TOPICS_END'
     print("Found topics")

def p_topic(p):
     '''topic : TOPIC_START REGION_TITLE_TOPIC TOPIC_END topic
             | empty'''
     try:
          print("Found topic: " + p[2])
          p[0] = p[2]
     except:
          print("Ended topic")

def p_title(p):
     'title : TITLE_START REGION_TITLE_TOPIC TITLE_END'
     print("Found title: " + p[2])
     p[0] = p[2]

def p_regions(p):
     'regions : REGIONS_START region REGIONS_END'
     print("Found regions")

def p_region(p):
     '''region : REGION_START REGION_TITLE_TOPIC REGION_END region
             | empty'''
     try:
          print("Found region: " + p[2])
     except:
          print("Ended region")

def p_sites(p):
     'sites : SITES_START site SITES_END'
     print("Found sites")

def p_site(p):
     '''site : SITE_START url title topics records SITE_END site
             | empty'''
     

def p_url(p):
     'url : URL_START URL URL_END'
     print("Found url: " + p[2])
     p[0] = p[2]
     
def p_records(p):
     'records : RECORDS_START record RECORDS_END'
     print("Found records")
     p[0] = p[2]

def p_record(p):
     '''record : RECORD_START initialdate finaldate region numbervisits RECORD_END record
             | empty'''
     try:
          print("Found record")
     except:
          print("Empty record")

def p_initialdate(p):
     'initialdate : INIT_DATE_START DATE INIT_DATE_END'
     try:
         complete_date = p[2].split("-") # Split the date string into its component parts
         day = int(complete_date[0])
         month = int(complete_date[1])
         year = int(complete_date[2])
         p[0] = date(year, month, day)
         print("Found initial date: " + p[0].strftime("%d-%m-%Y"))
     except:
         print("Error: Date format must be DD-MM-YYYY")

def p_finaldate(p):
     'finaldate : FINAL_DATE_START DATE FINAL_DATE_END'
     try:
          complete_date = p[2].split("-") # Split the date string into its component parts
          day = int(complete_date[0])
          month = int(complete_date[1])
          year = int(complete_date[2])
          p[0] = date(year, month, day)
          print("Found final date: " + p[2])
     except:
          print("Invalid date")
     
def p_numbervisits(p):
     'numbervisits : NUMBER_OF_VISITS_START NUMBER_VISITS NUMBER_OF_VISITS_END'
     try:
          p[0] = float(p[2])
          print("Found number of visits: " + p[2])
     except:
          print("Invalid number of visits")

def p_empty(p):
     'empty :'
     pass

def p_error(p):
     print("Syntax error in input!" + str(p))

# read the input file
file = open("Tarea1/data/pruebaDatos.xml", "r", encoding='utf-8')
data = file.read()
file.close()

import ply.yacc as yacc
parser = yacc.yacc()


# Tokenize
parser.parse(data) # Parser calls the lexer to get the tokens