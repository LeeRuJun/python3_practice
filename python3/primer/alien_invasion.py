import  sys
import  pygame
from settings import Settings

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(ai_settings.screen_width,ai_settings.screen_height)
    pygame.display.set_caption("Alien Invasion")
    bg_color = (230, 230, 230)
    while True:
        screen.fill(bg_color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.flip()

run_game()

