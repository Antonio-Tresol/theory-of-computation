import ply.lex as lex

# List of token names.   This is always required
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
t_REGION_TITLE_TOPIC = r'[\d\w\-À-ÿ’:,|()¿?¡!\\+\'\" ]+'
t_URL = r'(http(s)?:\/\/)?(www\.)?[a-zA-Z0-9\-]+(\.[a-zA-Z0-9\-]+)+([\w\d#-+&@#\/%=~_|$?!:,.-]*)*' 

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
     r'[\d]+([.][\d]*)?'
     return t

# Build the lexer
lexer = lex.lex()

# read the input file
file = open("../data/Datos.xml", "r", encoding='utf-8')
data = file.read()

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
     tok = lexer.token()
     if not tok: 
         break      # No more input
     print(tok)