import math as _math
import random as _rnd

def random():
    return _rnd.random()

def randint(a, b):
    return _rnd.randint(int(a), int(b))

def sin(val):
    return _math.sin(float(val))

def cos(val):
    return _math.cos(float(val))

def tan(val):
    return _math.tan(float(val))

def abs_val(val):
    return abs(float(val))

def sqrt(val):
    return _math.sqrt(float(val))

def power(base, exp):
    return _math.pow(float(base), float(exp))
