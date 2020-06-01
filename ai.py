#!/usr/bin/env python3

import sys
import pygame as pg  # type: ignore

from alien import Alien
from bullet import Bullet
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""

        self.s = Settings()

        self.scr = pg.display.set_mode(
            (self.s.scr_width, self.s.scr_height)
        )

        self.ship = Ship(self)
        self.blts = pg.sprite.Group()
        self.aliens = pg.sprite.Group()
        self._create_fleet()

        pg.init()
        pg.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start main loop game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_blts()
            self._update_aliens()
            self._update_scr()

    def _check_events(self):
        """Respond to keypresses."""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pg.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pg.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pg.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pg.K_q:
            sys.exit()
        elif event.key == pg.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pg.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pg.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create bullet and add it bullets group."""
        if len(self.blts) < self.s.blt_allowed:
            new_blt = Bullet(self)
            self.blts.add(new_blt)

    def _update_blts(self):
        """Update bullet position and delete old
        bullets."""
        # Update bullet positions.
        self.blts.update()

        # Get rid of bullets that have disappeared.
        for blt in self.blts.copy():
            if blt.rect.bottom <= 0:
                self.blts.remove(blt)

    def _update_aliens(self):
        """Check if fleet is at an edge and update
        positions of all aliens."""
        self._check_fleet_edges()
        self.aliens.update()

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create first row of aliens
        ali = Alien(self)
        ali_width, ali_height = ali.rect.size  # 1
        ali_spc = ali_width * 2
        av_spc_x = self.s.scr_width - ali_spc
        num_ali_x = av_spc_x // ali_spc

        # Determine number of rows that fit on the screen.
        ship_height = self.ship.rect.height  # 2
        av_spc_y = (
            self.s.scr_height
            - (3 * ali_height)
            - ship_height
        )
        num_rows = av_spc_y // (2 * ali_height)

        # Create full fleet of aliens.
        for row_num in range(num_rows):  # 3
            for ali_num in range(num_ali_x):
                self._create_alien(ali_num, row_num)

    def _create_alien(self, ali_num, row_num):
        """Create alien and place it."""
        ali = Alien(self)
        ali_width, ali_height = ali.rect.size
        ali_width = ali.rect.width
        ali.x = (ali_num * (ali_width * 2)) + ali_width
        ali.rect.x = ali.x
        ali.rect.y = (  # 4
            ali.rect.height
            + 2 * ali.rect.height * row_num
        )
        self.aliens.add(ali)

    def _check_fleet_edges(self):
        """Respond if aliens reache the edges."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_diretion()
                break

    def _change_fleet_diretion(self):
        """Drop fleet and change direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.s.fleet_drop_speed
        self.s.fleet_dir *= -1

    def _update_scr(self):
        """Update images and flip to the new screen."""
        self.scr.fill(self.s.bg_color)
        self.ship.blitme()
        for blt in self.blts.sprites():
            blt.draw_bullet()
        self.aliens.draw(self.scr)

        pg.display.flip()


if __name__ == "__main__":
    # Make game instance and run.
    ai = AlienInvasion()
    ai.run_game()
