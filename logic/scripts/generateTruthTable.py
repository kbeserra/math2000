import ply.yacc as yacc

import ply.lex as lex

# List of token names.   This is always required
tokens = ( 'VAL',
           'NOT',
           'OR',
           'AND',
           'IMPLIES',
           'LPAREN',
           'RPAREN',
        )

# Regular expression rules for simple tokens
t_VAL       = r'[T|F]'
t_NOT       = r'!'
t_OR        = r'\+'
t_AND       = r'&'
t_IMPLIES   = r'->'
t_LPAREN    = r'\('
t_RPAREN    = r'\)'

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

precedence = (
    ('left','AND','OR','IMPLIES'),
    ('right','UNOT')
    )

def p_expression_val(t):
    'expression : VAL'
    t[0] = t[1]

conv = { True: "T", False: "F" }

def p_expression_not(t):
    'expression : NOT expression %prec UNOT'
    a = t[2] == 'T'
    t[0] = conv[ not a ]

def p_expression_or(p):
    'expression : expression OR expression'
    a = p[1] == 'T'
    b = p[3] == 'T'
    p[0] = conv[ a or b ]

def p_expression_and(p):
    'expression : expression AND expression'
    a = p[1] == 'T'
    b = p[3] == 'T'
    p[0] = conv[ a and b ]

def p_expression_IMPLIES(p):
    'expression : expression IMPLIES expression'
    a = p[1] == 'T'
    b = p[3] == 'T'
    p[0] = conv[ ( not a ) or b ]


def p_factor_expr(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")
    print( f"\t{p}" )

# Build the parser
parser = yacc.yacc()


import re
from itertools import product

tex_replacement = { t_NOT.replace('\\',''): r"\neg ",
                    t_OR.replace('\\','') : r"\vee ",
                    t_AND.replace('\\',''): r"\wedge ",
                    t_IMPLIES.replace('\\',''): "\\ implies " }

def produce_truth_table( S ) :


    vars = sorted( list( set( re.findall( r'[a-z][0-9]*', " ".join( S ) ))))
    n = len( vars )

    S_tex = [  "".join( s.replace( '|', '+' ).split() ) for s in S ]
    for i in range( len(S_tex) ):
        for symb in tex_replacement.keys():
            S_tex[i] = S_tex[i].replace( symb, tex_replacement[symb] )

    print( r"\begin{tabular}{" + "c|"*len(vars) + "c|"*(len(S)-1) + "c" + "}" )
    print( "\t $" + "$ & $".join( vars ) + "$ & $" + "$ & $".join(S_tex) + r"$ \\" )
    print( "\t\\hline")
    for vals in  product( *(['T', 'F'] for i in range(len(vars))) ):

        evaluation_map = { vars[i]:vals[i] for i in range(len(vars)) }
        row = "\t"
        for i, p in enumerate(evaluation_map.keys()):
            row += "$" + evaluation_map[p] + "$"
            if i+1 < len(vars):
                row += " & "

        for s in S:
            row += r" & $"
            t = s
            for p in evaluation_map.keys():
                t = re.sub( r'\b' + p + r'\b' , evaluation_map[p], t )
            t = t.replace( '|', '+' )
            row +=  parser.parse(t) + r"$"
        row += r"\\"
        print(row)
        # print( evaluation_map, t, parser.parse(t) )
    print( r"\end{tabular}" )

# while True:
#     try:
#         s = input('> ')
#     except EOFError:
#         break
#     if not s: continue
#     produce_truth_table( s )
#     # result = parser.parse(s)
#     # print(result)

import sys
import signal


if __name__  == "__main__" :
    produce_truth_table( sys.argv[1:] )
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)
