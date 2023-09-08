import pygame

class Target:
    """A class to represent the target to be shot."""
    def __init__(self, game):
        """Initialize target attributes and spawnpoint."""
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.rect = pygame.rect.Rect(0, 0, 25, 100)
        self.rect.topright = self.screen_rect.topright
    
        self.moving_down = False
        self.moving_up = False

        self.speed = 3

    def blitme(self):
        pygame.draw.rect(self.screen, (0,0,0), self.rect)
    
    def update(self):
        """Updates the targets position."""
        if self.rect.top <= self.screen_rect.top:
            self.moving_down = True
            self.moving_up = False
        if self.rect.bottom >= self.screen_rect.bottom:
            self.moving_up = True
            self.moving_down = False
        if self.moving_up == True:
            self.rect.y -= self.speed
        if self.moving_down == True:
            self.rect.y += self.speed