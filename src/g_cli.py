import sys
import os

# Ensure modules can be found whether running from source or pyinstaller
if getattr(sys, 'frozen', False):
    application_path = sys._MEIPASS
else:
    application_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, application_path)

from lexer import GLexer
from parser import GParser
from interpreter import GInterpreter

def run_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            code = f.read()
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return
    
    lexer = GLexer()
    parser = GParser()
    interpreter = GInterpreter()
    
    tokens = lexer.tokenize(code)
    try:
        tree = parser.parse(tokens)
        if tree:
            interpreter.execute(tree)
    except Exception as e:
        print(f"Error executing script: {e}")

def run_repl():
    print("G Programming Language - Interactive Mode")
    print("Type 'exit' to quit.")
    
    lexer = GLexer()
    parser = GParser()
    interpreter = GInterpreter()
    
    while True:
        try:
            code = input("G> ")
            if code.strip().lower() == 'exit':
                break
            if not code.strip():
                continue
            
            tokens = lexer.tokenize(code)
            tree = parser.parse(tokens)
            if tree:
                interpreter.execute(tree)
        except EOFError:
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        run_repl()
    elif sys.argv[1].lower() == 'idle':
        from idle import run_idle
        run_idle()
    else:
        run_file(sys.argv[1])
