from sly import Parser
from lexer import GLexer

class GParser(Parser):
    tokens = GLexer.tokens
    
    precedence = (
        ('left', OR),
        ('left', AND),
        ('right', NOT),
        ('left', EQ, NEQ, IS, LT, LE, GT, GE),
        ('left', PLUS, MINUS),
        ('left', TIMES, DIVIDE),
    )

    @_('statements')
    def program(self, p):
        return p.statements

    @_('statement statements')
    def statements(self, p):
        return [p.statement] + p.statements

    @_('statement')
    def statements(self, p):
        return [p.statement]

    @_('SAY expr')
    def statement(self, p):
        return ('say', p.expr)

    @_('SET NAME TO expr')
    def statement(self, p):
        return ('assign', p.NAME, p.expr)
        
    @_('SET NAME DOT NAME TO expr')
    def statement(self, p):
        return ('set_property', p.NAME0, p.NAME1, p.expr)
        
    @_('SET expr LBRACKET expr RBRACKET TO expr')
    def statement(self, p):
        return ('set_index', p.expr0, p.expr1, p.expr2)
        
    @_('IMPORT NAME')
    def statement(self, p):
        return ('import', p.NAME)

    @_('DEFINE NAME LPAREN paramlist RPAREN DO statements END')
    def statement(self, p):
        return ('func_def', p.NAME, p.paramlist, p.statements)

    @_('DEFINE NAME LPAREN RPAREN DO statements END')
    def statement(self, p):
        return ('func_def', p.NAME, [], p.statements)

    @_('NAME COMMA paramlist')
    def paramlist(self, p):
        return [p.NAME] + p.paramlist
        
    @_('NAME')
    def paramlist(self, p):
        return [p.NAME]

    @_('RETURN expr')
    def statement(self, p):
        return ('return', p.expr)

    @_('READ expr INTO NAME')
    def statement(self, p):
        return ('read_file', p.expr, p.NAME)

    @_('WRITE expr TO expr')
    def statement(self, p):
        return ('write_file', p.expr0, p.expr1)

    @_('FETCH expr INTO NAME')
    def statement(self, p):
        return ('fetch', p.expr, p.NAME)

    @_('IF expr THEN statements END')
    def statement(self, p):
        return ('if', p.expr, p.statements, [])

    @_('IF expr THEN statements ELSE statements END')
    def statement(self, p):
        return ('if', p.expr, p.statements0, p.statements1)

    @_('WHILE expr DO statements END')
    def statement(self, p):
        return ('while', p.expr, p.statements)
        
    @_('NAME DOT NAME LPAREN arglist RPAREN')
    def statement(self, p):
        return ('method_call_stmt', p.NAME0, p.NAME1, p.arglist)

    @_('NAME DOT NAME LPAREN RPAREN')
    def statement(self, p):
        return ('method_call_stmt', p.NAME0, p.NAME1, [])

    @_('NAME LPAREN arglist RPAREN')
    def statement(self, p):
        return ('func_call_stmt', p.NAME, p.arglist)

    @_('NAME LPAREN RPAREN')
    def statement(self, p):
        return ('func_call_stmt', p.NAME, [])

    @_('expr PLUS expr')
    def expr(self, p):
        return ('add', p.expr0, p.expr1)

    @_('expr MINUS expr')
    def expr(self, p):
        return ('sub', p.expr0, p.expr1)

    @_('expr TIMES expr')
    def expr(self, p):
        return ('mul', p.expr0, p.expr1)

    @_('expr DIVIDE expr')
    def expr(self, p):
        return ('div', p.expr0, p.expr1)
        
    @_('expr EQ expr', 'expr IS expr')
    def expr(self, p):
        return ('eq', p.expr0, p.expr1)

    @_('expr NEQ expr')
    def expr(self, p):
        return ('neq', p.expr0, p.expr1)

    @_('expr LT expr')
    def expr(self, p):
        return ('lt', p.expr0, p.expr1)

    @_('expr LE expr')
    def expr(self, p):
        return ('le', p.expr0, p.expr1)

    @_('expr GT expr')
    def expr(self, p):
        return ('gt', p.expr0, p.expr1)

    @_('expr GE expr')
    def expr(self, p):
        return ('ge', p.expr0, p.expr1)
        
    @_('expr AND expr')
    def expr(self, p):
        return ('and', p.expr0, p.expr1)

    @_('expr OR expr')
    def expr(self, p):
        return ('or', p.expr0, p.expr1)

    @_('expr LBRACKET expr RBRACKET')
    def expr(self, p):
        return ('index', p.expr0, p.expr1)

    @_('LBRACKET arglist RBRACKET')
    def expr(self, p):
        return ('list', p.arglist)

    @_('LBRACKET RBRACKET')
    def expr(self, p):
        return ('list', [])

    @_('LBRACE dict_items RBRACE')
    def expr(self, p):
        return ('dict', p.dict_items)

    @_('LBRACE RBRACE')
    def expr(self, p):
        return ('dict', [])

    @_('STRING COLON expr COMMA dict_items')
    def dict_items(self, p):
        return [(p.STRING[1:-1], p.expr)] + p.dict_items

    @_('STRING COLON expr')
    def dict_items(self, p):
        return [(p.STRING[1:-1], p.expr)]

    @_('NOT expr')
    def expr(self, p):
        return ('not', p.expr)

    @_('MINUS expr %prec TIMES')
    def expr(self, p):
        return ('neg', p.expr)

    @_('LPAREN expr RPAREN')
    def expr(self, p):
        return p.expr

    @_('NUMBER')
    def expr(self, p):
        return ('num', p.NUMBER)

    @_('STRING')
    def expr(self, p):
        return ('str', p.STRING[1:-1])

    @_('NAME')
    def expr(self, p):
        return ('var', p.NAME)
        
    @_('NAME DOT NAME')
    def expr(self, p):
        return ('property', p.NAME0, p.NAME1)

    @_('NAME DOT NAME LPAREN arglist RPAREN')
    def expr(self, p):
        return ('method_call', p.NAME0, p.NAME1, p.arglist)

    @_('NAME DOT NAME LPAREN RPAREN')
    def expr(self, p):
        return ('method_call', p.NAME0, p.NAME1, [])
        
    @_('NAME LPAREN arglist RPAREN')
    def expr(self, p):
        return ('call', p.NAME, p.arglist)
        
    @_('NAME LPAREN RPAREN')
    def expr(self, p):
        return ('call', p.NAME, [])
        
    @_('expr COMMA arglist')
    def arglist(self, p):
        return [p.expr] + p.arglist
        
    @_('expr')
    def arglist(self, p):
        return [p.expr]

    def error(self, p):
        if p:
            print(f"Syntax error at '{p.value}', line {p.lineno}")
        else:
            print("Syntax error at EOF")
