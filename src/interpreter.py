import importlib

class GInterpreter:
    def __init__(self):
        self.env = {}
        self.modules = {}

    def execute(self, stmts):
        for stmt in stmts:
            self.eval_stmt(stmt)

    def eval_stmt(self, stmt):
        if not stmt:
            return
        op = stmt[0]
        if op == 'say':
            print(self.eval_expr(stmt[1]))
        elif op == 'assign':
            self.env[stmt[1]] = self.eval_expr(stmt[2])
        elif op == 'import':
            mod_name = stmt[1]
            try:
                if mod_name == 'game':
                    import modules.game as game
                    self.modules['game'] = game
                elif mod_name == 'app':
                    import modules.app as app
                    self.modules['app'] = app
                else:
                    print(f"Unknown module {mod_name}")
            except ImportError as e:
                print(f"Failed to import {mod_name}: {e}")
        elif op == 'if':
            condition = self.eval_expr(stmt[1])
            if condition:
                for s in stmt[2]:
                    self.eval_stmt(s)
            else:
                for s in stmt[3]:
                    self.eval_stmt(s)
        elif op == 'while':
            while self.eval_expr(stmt[1]):
                for s in stmt[2]:
                    self.eval_stmt(s)
        elif op == 'func_call_stmt':
            self.eval_expr(('call', stmt[1], stmt[2]))
        elif op == 'method_call_stmt':
            self.eval_expr(('method_call', stmt[1], stmt[2], stmt[3]))
        elif op == 'set_property':
            obj_name = stmt[1]
            prop_name = stmt[2]
            val = self.eval_expr(stmt[3])
            if obj_name in self.modules:
                setattr(self.modules[obj_name], prop_name, val)
            elif obj_name in self.env:
                setattr(self.env[obj_name], prop_name, val)
            else:
                print(f"Unknown object {obj_name}")

    def eval_expr(self, expr):
        op = expr[0]
        if op == 'num': return expr[1]
        elif op == 'str': return expr[1]
        elif op == 'var':
            if expr[1] in self.env: return self.env[expr[1]]
            else:
                print(f"Undefined variable {expr[1]}")
                return 0
        elif op == 'add': return self.eval_expr(expr[1]) + self.eval_expr(expr[2])
        elif op == 'sub': return self.eval_expr(expr[1]) - self.eval_expr(expr[2])
        elif op == 'mul': return self.eval_expr(expr[1]) * self.eval_expr(expr[2])
        elif op == 'div': return self.eval_expr(expr[1]) / self.eval_expr(expr[2])
        elif op == 'eq': return self.eval_expr(expr[1]) == self.eval_expr(expr[2])
        elif op == 'neq': return self.eval_expr(expr[1]) != self.eval_expr(expr[2])
        elif op == 'lt': return self.eval_expr(expr[1]) < self.eval_expr(expr[2])
        elif op == 'le': return self.eval_expr(expr[1]) <= self.eval_expr(expr[2])
        elif op == 'gt': return self.eval_expr(expr[1]) > self.eval_expr(expr[2])
        elif op == 'ge': return self.eval_expr(expr[1]) >= self.eval_expr(expr[2])
        elif op == 'and': return self.eval_expr(expr[1]) and self.eval_expr(expr[2])
        elif op == 'or': return self.eval_expr(expr[1]) or self.eval_expr(expr[2])
        elif op == 'not': return not self.eval_expr(expr[1])
        elif op == 'neg': return -self.eval_expr(expr[1])
        elif op == 'call':
            func_name = expr[1]
            args = [self.eval_expr(a) for a in expr[2]]
            if func_name == 'int': return int(args[0])
            elif func_name == 'str': return str(args[0])
            elif func_name == 'input': return input(args[0] if len(args) > 0 else "")
            elif func_name == 'len': return len(args[0])
            else:
                print(f"Unknown function {func_name}")
                return 0
        elif op == 'method_call':
            obj_name = expr[1]
            method_name = expr[2]
            args = [self.eval_expr(a) for a in expr[3]]
            if obj_name in self.modules:
                func = getattr(self.modules[obj_name], method_name)
                return func(*args)
            elif obj_name in self.env:
                obj = self.env[obj_name]
                func = getattr(obj, method_name)
                return func(*args)
            else:
                print(f"Unknown object {obj_name}")
                return 0
        elif op == 'property':
            obj_name = expr[1]
            prop_name = expr[2]
            if obj_name in self.modules:
                return getattr(self.modules[obj_name], prop_name)
            elif obj_name in self.env:
                return getattr(self.env[obj_name], prop_name)
            else:
                print(f"Unknown object {obj_name}")
                return 0
