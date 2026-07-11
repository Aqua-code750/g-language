from sly import Lexer

class GLexer(Lexer):
    tokens = { SAY, SET, TO, IF, IS, THEN, ELSE, WHILE, DO, END, AND, OR, NOT, IMPORT,
               NAME, NUMBER, STRING, PLUS, MINUS, TIMES, DIVIDE, DOT,
               EQ, NEQ, LT, LE, GT, GE, LPAREN, RPAREN, COMMA }
    
    ignore = ' \t'
    ignore_comment = r'\#.*'
    
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += len(t.value)

    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    NAME['say'] = SAY
    NAME['set'] = SET
    NAME['to'] = TO
    NAME['if'] = IF
    NAME['is'] = IS
    NAME['then'] = THEN
    NAME['else'] = ELSE
    NAME['while'] = WHILE
    NAME['do'] = DO
    NAME['end'] = END
    NAME['and'] = AND
    NAME['or'] = OR
    NAME['not'] = NOT
    NAME['import'] = IMPORT

    STRING = r'".*?"'
    
    @_(r'\d+\.\d+|\d+')
    def NUMBER(self, t):
        if '.' in t.value:
            t.value = float(t.value)
        else:
            t.value = int(t.value)
        return t

    PLUS = r'\+'
    MINUS = r'-'
    TIMES = r'\*'
    DIVIDE = r'/'
    EQ = r'=='
    NEQ = r'!='
    LE = r'<='
    GE = r'>='
    LT = r'<'
    GT = r'>'
    LPAREN = r'\('
    RPAREN = r'\)'
    COMMA = r','
    DOT = r'\.'
    
    def error(self, t):
        print(f"Line {self.lineno}: Bad character {t.value[0]!r}")
        self.index += 1
