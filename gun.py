import pygame

class Gun:
    """A class to represent the gun."""
    def __init__(self, game):
        """Initialize gun attributes"""
        self.settings = game.settings
        
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load('gun.bmp')
        self.image = pygame.transform.scale(self.image, (100, 50))
        self.rect = self.image.get_rect()

        self.rect.x = 0
        self.rect.midleft = self.screen_rect.midleft

        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        """Draw the gun."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Updates gun's positioning."""
        if self.moving_up == True and self.rect.top >= self.screen_rect.top:
            self.rect.y -= self.settings.gun_speed
        if self.moving_down == True and self.rect.bottom <= self.screen_rect.bottom:
            self.rect.y += self.settings.gun_speed
    
    def center_gun(self):
        """Centers the gun."""
        self.rect.x = 0
        self.rect.y = self.screen_rect.midleft
    
    def reset(self):
        """Recenter gun's position."""
        self.rect.x = 0
        self.rect.midleft = self.screen_rect.midleft