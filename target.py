import pygame

class Target:
    """A class to represent the target to be shot."""
    def __init__(self, game):
        """Initialize target attributes and spawnpoint."""
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings

        self.rect = pygame.rect.Rect(0, 0, 25, 100)
        self.rect.topright = self.screen_rect.topright
    
        self.moving_down = False
        self.moving_up = False

        self.speed = self.settings.target_speed

    def blitme(self):
        pygame.draw.rect(self.screen, self.settings.target_color, self.rect)
    
    def update(self):
        """Updates the targets position."""
        if self.rect.top <= self.screen_rect.top:
            self.moving_down = True
        elif self.rect.bottom >= self.screen_rect.bottom:
            self.moving_down = False
        if self.moving_down == True:
            self.rect.y += self.speed
        else:
            self.rect.y -= self.speed