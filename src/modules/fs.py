import os

def read_file(path):
    with open(str(path), 'r', encoding='utf-8') as f:
        return f.read()

def write_file(path, content):
    with open(str(path), 'w', encoding='utf-8') as f:
        f.write(str(content))
        
def append_file(path, content):
    with open(str(path), 'a', encoding='utf-8') as f:
        f.write(str(content))

def file_exists(path):
    return 1 if os.path.exists(str(path)) else 0

def delete_file(path):
    if os.path.exists(str(path)):
        os.remove(str(path))
        return 1
    return 0
