import customtkinter as ctk
import sys
import io
import threading
from tkinter import filedialog
from lexer import GLexer
from parser import GParser
from interpreter import GInterpreter

class RedirectText:
    def __init__(self, text_widget):
        self.output = text_widget

    def write(self, string):
        self.output.insert("end", string)
        self.output.see("end")

    def flush(self):
        pass

class GIDLE(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("G Language IDLE")
        self.geometry("900x600")
        
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        self.current_filepath = None
        
        # --- Toolbar ---
        self.toolbar = ctk.CTkFrame(self, height=40)
        self.toolbar.pack(side="top", fill="x", padx=5, pady=5)
        
        self.btn_run = ctk.CTkButton(self.toolbar, text="Run (F5)", command=self.run_code, fg_color="green", hover_color="darkgreen", width=80)
        self.btn_run.pack(side="left", padx=5)
        
        self.btn_open = ctk.CTkButton(self.toolbar, text="Open", command=self.open_file, width=80)
        self.btn_open.pack(side="left", padx=5)
        
        self.btn_save = ctk.CTkButton(self.toolbar, text="Save", command=self.save_file, width=80)
        self.btn_save.pack(side="left", padx=5)
        
        self.btn_clear = ctk.CTkButton(self.toolbar, text="Clear Output", command=self.clear_output, width=100)
        self.btn_clear.pack(side="left", padx=5)
        
        # --- Main View (Paned Window Simulation) ---
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(side="bottom", fill="both", expand=True, padx=5, pady=5)
        
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(0, weight=3) # Editor gets 3/4 of space
        self.main_frame.rowconfigure(1, weight=1) # Console gets 1/4 of space
        
        # --- Editor ---
        self.editor_frame = ctk.CTkFrame(self.main_frame)
        self.editor_frame.grid(row=0, column=0, sticky="nsew", pady=(0, 5))
        
        self.editor_label = ctk.CTkLabel(self.editor_frame, text="Code Editor", anchor="w")
        self.editor_label.pack(side="top", fill="x", padx=5)
        
        self.editor = ctk.CTkTextbox(self.editor_frame, font=("Consolas", 14), wrap="none")
        self.editor.pack(side="top", fill="both", expand=True)
        
        # --- Console Output ---
        self.console_frame = ctk.CTkFrame(self.main_frame)
        self.console_frame.grid(row=1, column=0, sticky="nsew")
        
        self.console_label = ctk.CTkLabel(self.console_frame, text="Console Output", anchor="w")
        self.console_label.pack(side="top", fill="x", padx=5)
        
        self.console = ctk.CTkTextbox(self.console_frame, font=("Consolas", 13), state="disabled", fg_color="#1E1E1E", text_color="#A5C25C")
        self.console.pack(side="top", fill="both", expand=True)
        
        # Bind F5 to run
        self.bind("<F5>", lambda event: self.run_code())
        self.bind("<Control-s>", lambda event: self.save_file())
        self.bind("<Control-o>", lambda event: self.open_file())

    def open_file(self):
        filepath = filedialog.askopenfilename(filetypes=[("G Language Files", "*.g"), ("All Files", "*.*")])
        if filepath:
            with open(filepath, "r", encoding="utf-8") as f:
                code = f.read()
            self.editor.delete("0.0", "end")
            self.editor.insert("0.0", code)
            self.current_filepath = filepath
            self.title(f"G Language IDLE - {filepath}")

    def save_file(self):
        if not self.current_filepath:
            self.current_filepath = filedialog.asksaveasfilename(defaultextension=".g", filetypes=[("G Language Files", "*.g"), ("All Files", "*.*")])
        
        if self.current_filepath:
            code = self.editor.get("0.0", "end")
            with open(self.current_filepath, "w", encoding="utf-8") as f:
                f.write(code)
            self.title(f"G Language IDLE - {self.current_filepath}")

    def clear_output(self):
        self.console.configure(state="normal")
        self.console.delete("0.0", "end")
        self.console.configure(state="disabled")

    def run_code(self):
        code = self.editor.get("0.0", "end")
        
        # Clear output first
        self.clear_output()
        self.console.configure(state="normal")
        self.console.insert("end", ">>> Running script...\n")
        
        # Redirect stdout and stderr
        old_stdout = sys.stdout
        old_stderr = sys.stderr
        redirected_output = RedirectText(self.console)
        sys.stdout = redirected_output
        sys.stderr = redirected_output
        
        try:
            lexer = GLexer()
            parser = GParser()
            interpreter = GInterpreter()
            
            tokens = lexer.tokenize(code)
            tree = parser.parse(tokens)
            if tree:
                interpreter.execute(tree)
        except Exception as e:
            print(f"Runtime Error: {e}")
        finally:
            # Restore stdout/stderr
            sys.stdout = old_stdout
            sys.stderr = old_stderr
            self.console.insert("end", "\n>>> Script finished.\n")
            self.console.configure(state="disabled")

def run_idle():
    app = GIDLE()
    app.mainloop()

if __name__ == "__main__":
    run_idle()
