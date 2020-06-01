import pygame as pg  # type: ignore
from pygame.sprite import Sprite  # type: ignore


class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.scr
        self.s = ai_game.s
        self.color = self.s.blt_color

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pg.Rect(0, 0, self.s.blt_width, self.s.blt_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.y -= self.s.blt_speed
        # Update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pg.draw.rect(self.screen, self.color, self.rect)
