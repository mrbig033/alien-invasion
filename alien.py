import pygame as pg  # type: ignore
from pygame.sprite import Sprite  # type: ignore


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize alien and set start position."""
        super().__init__()
        self.s = ai_game.s
        self.scr = ai_game.scr

        # Load the alien image and set its rect attribute.
        self.image = pg.image.load("img/alien.bmp")
        self.rect = self.image.get_rect()

        # Start each new alien near top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)

    def check_edges(self):
        """True if alien is at edge of screen."""
        scr_rect = self.scr.get_rect()
        if (
            self.rect.right >= scr_rect.right
            or self.rect.left <= 0
        ):
            return True

    def update(self):
        """Move the alien to right or left."""
        self.x += self.s.ali_speed * self.s.fleet_dir
        self.rect.x = self.x
