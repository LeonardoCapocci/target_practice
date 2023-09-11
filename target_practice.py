import sys
from time import sleep

import pygame

from settings import Settings
from button import Button
from gun import Gun
from bullet import Bullet
from target import Target

class TargetPractice:
    """A class to create a target practice game."""
    def __init__(self):
        """Initialize the game attributes."""
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((1280,720))
        self.screen_rect = self.screen.get_rect()
        self.screen_color = (189,160,125)
        pygame.display.set_caption("Target Practice - Leonardo Capocci")

        # Settings
        self.settings = Settings()
        # Start button
        self.button = Button(self, "PLAY")
        # Gun attributes
        self.gun = Gun(self)
        self.game_active = False
        # Bullet attributes
        self.bullets = pygame.sprite.Group()
        # Target
        self.target = Target(self)

    def run_game(self):
        """Main loop for the game."""
        while True:
            print(len(self.bullets))
            self.screen.fill(self.screen_color)
            self._check_events()
            if self.game_active == True:
                self.gun.update()
                self._update_bullets()
                self._update_target()
                
                
            self._update_screen()
            self.clock.tick(60)
            pygame.display.flip()
            self._check_end_game()
            self._check_collision()

    def _check_events(self):
        """Checks for keyboard events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                 mouse_pos = pygame.mouse.get_pos()
                 self._check_play_button(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                 self._check_keyup_events(event)

    def _check_play_button(self, mouse_pos):
        """Checks if the mouse clicked the play button"""
        button_clicked = self.button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self.game_active = True
            pygame.mouse.set_visible(False)
            self.bullets.empty()
            self.gun.reset()
            self.target.reset()
            sleep(0.25)
            self.gun.center_gun()

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
        if event.key == pygame.K_SPACE and not self.game_active:
            self.game_active = True
            pygame.mouse.set_visible(False)
            self.bullets.empty()
            self.gun.reset()
            self.target.reset()
            sleep(0.25)
            self.gun.center_gun()

    def _check_keyup_events(self, event):
        """Check for keyup events."""
        if event.key == pygame.K_UP or event.key == pygame.K_w:
            self.gun.moving_up = False
        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.gun.moving_down = False

    def _create_bullet(self):
        """Creates a bullet at the gun."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Updates bullets positioning/existence"""
        self.bullets.update()
        #for bullet in self.bullets.copy():
            #if bullet.rect.x > self.screen_rect.right:
                #self.bullets.remove(bullet)

    def _update_target(self):
        """Updates target's position."""
        self.target.update()

    def _check_collision(self):
        """Checks for collisions between bullets and target."""
        if pygame.sprite.spritecollideany(self.target, self.bullets):
            print("Good shot")
            sleep(1)
            self.target.level_up()
            self.bullets.empty()
            self.gun.center_gun()
        
    def _check_end_game(self):
        """Checks if the player is out of bullets and all the bullets are off 
        screen"""
        if len(self.bullets) == self.settings.bullets_allowed and all(bullet.rect.x >= self.screen_rect.right for bullet in self.bullets):
            sleep(0.25)
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _update_screen(self):
        """Spawn the gun."""
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.gun.blitme()
        self.target.blitme()
        if self.game_active == False:
            self.button.draw_button()

if __name__ == '__main__':
    tp = TargetPractice()
    tp.run_game()