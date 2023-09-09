class Settings:
    """Class to hold game settings options."""
    def __init__(self):
        """Set settings."""
        # Button settings
        self.button_dimension = 100, 100
        self.button_color = (0,0,0)
        self.button_text_color = (255,255,255)

        # Gun settings
        self.gun_speed = 10

        # Bullet settings
        self.bullet_color = (200,40,40)
        self.bullet_speed = 20
        self.bullets_allowed = 3

        # Target settings
        self.target_color = (0,0,0)
        self.target_speed = 3
        self.speed_multiplier = 1.2