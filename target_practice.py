import sys
from time import sleep

import pygame

from gun import Gun
from bullet import Bullet
from target import Target

class TargetPractice:
    """A class to create a target practice game."""
    def __init__(self):
        """Initialize the game attributes."""
        pygame.init()
        self.screen = pygame.display.set_mode((1280,720))
        self.screen_rect = self.screen.get_rect()
        self.screen_color = (189,160,125)
        self.clock = pygame.time.Clock()

        # Gun attributes
        self.gun = Gun(self)

        self.game_active = True

        # Bullet attributes
        self.bullets = pygame.sprite.Group()

        # Target
        self.target = Target(self)

    def run_game(self):
        """Main loop for the game."""
        while self.game_active:
            self.screen.fill(self.screen_color)
            self._check_events()

            self.gun.update()

            self._update_bullets()

            self._update_target()

            self._update_screen()
            self.clock.tick(60)
            pygame.display.flip()

    def _check_events(self):
        """Checks for keyboard events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                 self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Check for keydown events."""
        if event.key == pygame.K_q:
                    sys.exit()
        if event.key == pygame.K_UP or event.key == pygame.K_w:
             self.gun.moving_up = True
        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
             self.gun.moving_down = True
        if event.key == pygame.K_SPACE:
             self._create_bullet()

    def _check_keyup_events(self, event):
        """Check for keyup events."""
        if event.key == pygame.K_UP or event.key == pygame.K_w:
             self.gun.moving_up = False
        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
             self.gun.moving_down = False

    def _create_bullet(self):
        """Creates a bullet at the gun."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_bullets(self):
         """Updates bullets positioning/existence"""
         self.bullets.update()
         for bullet in self.bullets.copy():
              if bullet.rect.x > self.screen_rect.right:
                   self.bullets.remove(bullet)

    def _update_target(self):
         """Updates target's position."""
         self.target.update()

    def _update_screen(self):
        """Spawn the gun."""
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.gun.blitme()
        self.target.blitme()

if __name__ == '__main__':
    tp = TargetPractice()
    tp.run_game()