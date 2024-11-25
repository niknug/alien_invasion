class Settings:
    """Класс для хранения всех настроек игры"""

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 139)
        self.ship_speed = 2.5
        self.ship_style = 'ship3.bmp'
        self.full_screen_mode = True
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 255, 255
        self.bullets_allowed = 3
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction = 1 вправо; fleet_direction = -1 влево
        self.fleet_direction = 1
