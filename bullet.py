import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to represent a single bullet."""
    def __init__(self, game):
        """Initialize bullet attributes and set position at gun."""
        super().__init__()
        self.screen = game.screen
        self.rect = pygame.rect.Rect(0,0, 20, 8)

        self.rect.midright = game.gun.rect.midright
        self.rect.y -= 3
    
    def draw_bullet(self):
        """Draws the bullet."""
        pygame.draw.rect(self.screen, (200,40,40), self.rect)

    def update(self):
        """Update the positioning of a single bullet."""
        self.rect.x += 40