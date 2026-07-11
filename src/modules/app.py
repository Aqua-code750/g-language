import customtkinter as ctk

class AppEngine:
    def __init__(self):
        self.app = None
        self.interp = None
        self.widgets = {}

    def set_interpreter(self, interp):
        self.interp = interp

    def init_window(self, width, height, title):
        ctk.set_appearance_mode("dark")
        self.app = ctk.CTk()
        self.app.geometry(f"{int(width)}x{int(height)}")
        self.app.title(title)
        
        # Configure a generic 4-column grid
        for i in range(4):
            self.app.grid_columnconfigure(i, weight=1)

    def add_label(self, id_name, text, row, col, columnspan=1):
        lbl = ctk.CTkLabel(self.app, text=text, font=("Consolas", 24), anchor="e", fg_color="#333333", corner_radius=5)
        lbl.grid(row=int(row), column=int(col), columnspan=int(columnspan), padx=5, pady=10, sticky="ew")
        self.widgets[id_name] = lbl

    def set_label(self, id_name, text):
        if id_name in self.widgets:
            self.widgets[id_name].configure(text=str(text))

    def add_button(self, id_name, text, command_func, row, col, columnspan=1):
        def callback():
            if self.interp and command_func in self.interp.functions:
                params, stmts = self.interp.functions[command_func]
                
                # Make a local copy of env to avoid corrupting global, but actually we WANT side effects
                # So we let it run in the current environment
                try:
                    for s in stmts:
                        self.interp.eval_stmt(s)
                except Exception as e:
                    pass # ReturnException will be caught here
                    
        btn = ctk.CTkButton(self.app, text=text, command=callback, font=("Consolas", 20), height=50)
        btn.grid(row=int(row), column=int(col), columnspan=int(columnspan), padx=5, pady=5, sticky="nsew")
        self.widgets[id_name] = btn

    def run(self):
        if self.app:
            self.app.mainloop()

engine = AppEngine()

def set_interpreter(interp):
    engine.set_interpreter(interp)

def init_window(width, height, title):
    engine.init_window(width, height, title)

def add_label(id_name, text, row, col, columnspan):
    engine.add_label(id_name, text, row, col, columnspan)

def set_label(id_name, text):
    engine.set_label(id_name, text)

def add_button(id_name, text, command_func, row, col, columnspan):
    engine.add_button(id_name, text, command_func, row, col, columnspan)

def run():
    engine.run()
