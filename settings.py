class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.scr_width = 1200
        self.scr_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 2

        # Bullet settings
        self.blt_speed = 1.0
        self.blt_width = 3
        self.blt_height = 15
        self.blt_color = (60, 60, 60)
        self.blt_allowed = 3
