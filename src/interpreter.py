import importlib

class ReturnException(Exception):
    def __init__(self, value):
        self.value = value

class GInterpreter:
    def __init__(self):
        self.env = {}
        self.modules = {}
        self.functions = {}

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
        elif op == 'func_def':
            self.functions[stmt[1]] = (stmt[2], stmt[3])
        elif op == 'return':
            raise ReturnException(self.eval_expr(stmt[1]))
        elif op == 'read_file':
            filepath = self.eval_expr(stmt[1])
            var_name = stmt[2]
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    self.env[var_name] = f.read()
            except Exception as e:
                print(f"Error reading file: {e}")
                self.env[var_name] = ""
        elif op == 'write_file':
            content = self.eval_expr(stmt[1])
            filepath = self.eval_expr(stmt[2])
            try:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(str(content))
            except Exception as e:
                print(f"Error writing file: {e}")
        elif op == 'fetch':
            url = self.eval_expr(stmt[1])
            var_name = stmt[2]
            try:
                import urllib.request
                with urllib.request.urlopen(url) as response:
                    self.env[var_name] = response.read().decode('utf-8')
            except Exception as e:
                print(f"Error fetching URL: {e}")
                self.env[var_name] = ""
        elif op == 'set_index':
            obj = self.eval_expr(stmt[1])
            idx = self.eval_expr(stmt[2])
            val = self.eval_expr(stmt[3])
            try:
                obj[idx] = val
            except Exception as e:
                print(f"Error setting index: {e}")
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
        elif op == 'list':
            return [self.eval_expr(e) for e in expr[1]]
        elif op == 'dict':
            return {k: self.eval_expr(v) for k, v in expr[1]}
        elif op == 'index':
            obj = self.eval_expr(expr[1])
            idx = self.eval_expr(expr[2])
            try:
                return obj[idx]
            except Exception as e:
                print(f"Error accessing index: {e}")
                return 0
        elif op == 'call':
            func_name = expr[1]
            args = [self.eval_expr(a) for a in expr[2]]
            if func_name in self.functions:
                params, stmts = self.functions[func_name]
                old_env = self.env
                self.env = dict(self.env)
                for p, a in zip(params, args):
                    self.env[p] = a
                ret_val = 0
                try:
                    for s in stmts:
                        self.eval_stmt(s)
                except ReturnException as r:
                    ret_val = r.value
                self.env = old_env
                return ret_val
            elif func_name == 'int': return int(args[0])
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
