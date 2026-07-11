import pygame

class GameEngine:
    def __init__(self):
        pygame.init()
        self.screen = None
        self.clock = pygame.time.Clock()
        self.running = False

    def init_window(self, width, height, title):
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.running = True

    def fill(self, r, g, b):
        if self.screen:
            self.screen.fill((r, g, b))

    def update(self):
        if self.screen:
            pygame.display.flip()
            self.clock.tick(60)

    def is_running(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        return self.running

# Expose a default engine instance
engine = GameEngine()

def init_window(width, height, title):
    engine.init_window(int(width), int(height), str(title))

def fill(r, g, b):
    engine.fill(int(r), int(g), int(b))

def update():
    engine.update()

def is_running():
    return engine.is_running()
