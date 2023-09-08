class Settings:
    """Class to hold game settings options."""
    def __init__(self):
        # Gun settings
        self.gun_speed = 10

        # Bullet settings
        self.bullet_color = (200,40,40)
        self.bullet_speed = 40

        # Target settings
        self.target_color = (0,0,0)
        self.target_speed = 3