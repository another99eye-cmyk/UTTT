import pygame
import sys

pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ultimate Tic Tac Toe")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 150, 255)

# Fonts
font = pygame.font.SysFont("arial", 36)

# Scene manager
current_scene = "main_menu"

# Button helper
class Button:
    def __init__(self, text, pos, action):
        self.text = text
        self.pos = pos
        self.action = action
        self.rect = pygame.Rect(pos[0], pos[1], 200, 50)

    def draw(self, screen):
        pygame.draw.rect(screen, BLUE, self.rect)
        label = font.render(self.text, True, WHITE)
        screen.blit(label, (self.pos[0] + 20, self.pos[1] + 10))

    def check_click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return self.action
        return None

# Define menus
main_menu_buttons = [
    Button("Start", (300, 200), "start_menu"),
    Button("Continue", (300, 260), "continue"),
    Button("Shop", (300, 320), "shop"),
    Button("Credits", (300, 380), "credits"),
    Button("Quit", (300, 440), "quit"),
]

start_menu_buttons = [
    Button("New Game", (300, 200), "new_game"),
    Button("Main Menu", (300, 260), "main_menu"),
]

new_game_buttons = [
    Button("AI Mode", (300, 200), "ai_menu"),
    Button("Two Players", (300, 260), "two_players"),
    Button("Multiplayer", (300, 320), "multiplayer"),
    Button("Back", (300, 380), "start_menu"),
]

ai_menu_buttons = [
    Button("Easy", (300, 200), "ai_easy"),
    Button("Normal", (300, 260), "ai_normal"),
    Button("Hard", (300, 320), "ai_hard"),
    Button("Back", (300, 380), "new_game"),
]

# Game loop
running = True
while running:
    screen.fill(BLACK)

    # Draw current scene
    if current_scene == "main_menu":
        for b in main_menu_buttons: b.draw(screen)
    elif current_scene == "start_menu":
        for b in start_menu_buttons: b.draw(screen)
    elif current_scene == "new_game":
        for b in new_game_buttons: b.draw(screen)
    elif current_scene == "ai_menu":
        for b in ai_menu_buttons: b.draw(screen)
    elif current_scene == "shop":
        label = font.render("Shop (coming soon)", True, WHITE)
        screen.blit(label, (250, 250))
    elif current_scene == "credits":
        label = font.render("Credits: Made by You!", True, WHITE)
        screen.blit(label, (250, 250))
    elif current_scene == "quit":
        pygame.quit()
        sys.exit()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check button clicks
        if current_scene == "main_menu":
            for b in main_menu_buttons:
                action = b.check_click(event)
                if action: current_scene = action
        elif current_scene == "start_menu":
            for b in start_menu_buttons:
                action = b.check_click(event)
                if action: current_scene = action
        elif current_scene == "new_game":
            for b in new_game_buttons:
                action = b.check_click(event)
                if action: current_scene = action
        elif current_scene == "ai_menu":
            for b in ai_menu_buttons:
                action = b.check_click(event)
                if action: current_scene = action

    pygame.display.flip()
