import customtkinter as ctk

class AppEngine:
    def __init__(self):
        self.app = None

    def init_window(self, width, height, title):
        self.app = ctk.CTk()
        self.app.geometry(f"{int(width)}x{int(height)}")
        self.app.title(title)

    def run(self):
        if self.app:
            self.app.mainloop()

engine = AppEngine()

def init_window(width, height, title):
    engine.init_window(width, height, title)

def run():
    engine.run()
