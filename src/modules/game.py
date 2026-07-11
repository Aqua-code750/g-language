import pygame

class GameEngine:
    def __init__(self):
        pygame.init()
        self.screen = None
        self.clock = pygame.time.Clock()
        self.running = False
        self.keys = {}

    def init_window(self, width, height, title):
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.running = True

    def fill(self, r, g, b):
        if self.screen:
            self.screen.fill((r, g, b))
            
    def draw_rect(self, r, g, b, x, y, w, h):
        if self.screen:
            pygame.draw.rect(self.screen, (r, g, b), pygame.Rect(x, y, w, h))

    def draw_circle(self, r, g, b, x, y, radius):
        if self.screen:
            pygame.draw.circle(self.screen, (r, g, b), (x, y), radius)

    def update(self):
        if self.screen:
            pygame.display.flip()
            self.clock.tick(60)

    def is_running(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                
        # Update key states
        pressed = pygame.key.get_pressed()
        self.keys["left"] = pressed[pygame.K_LEFT] or pressed[pygame.K_a]
        self.keys["right"] = pressed[pygame.K_RIGHT] or pressed[pygame.K_d]
        self.keys["up"] = pressed[pygame.K_UP] or pressed[pygame.K_w]
        self.keys["down"] = pressed[pygame.K_DOWN] or pressed[pygame.K_s]
        self.keys["space"] = pressed[pygame.K_SPACE]
        
        # 1 means true in G
        return 1 if self.running else 0

    def get_key(self, key_name):
        return 1 if self.keys.get(key_name, False) else 0

# Expose a default engine instance
engine = GameEngine()

def init_window(width, height, title):
    engine.init_window(int(width), int(height), str(title))

def fill(r, g, b):
    engine.fill(int(r), int(g), int(b))

def draw_rect(r, g, b, x, y, w, h):
    engine.draw_rect(int(r), int(g), int(b), int(x), int(y), int(w), int(h))

def draw_circle(r, g, b, x, y, radius):
    engine.draw_circle(int(r), int(g), int(b), int(x), int(y), int(radius))

def update():
    engine.update()

def is_running():
    return engine.is_running()

def get_key(key_name):
    return engine.get_key(str(key_name))
