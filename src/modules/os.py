import os as _os
import time as _time
import subprocess as _subprocess

def clear_screen():
    _os.system('cls' if _os.name == 'nt' else 'clear')
    return 1

def sleep(seconds):
    _time.sleep(float(seconds))
    return 1
    
def run_command(cmd):
    result = _subprocess.run(str(cmd), shell=True, capture_output=True, text=True)
    return result.stdout
    
def get_env(key):
    return _os.environ.get(str(key), "")
