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
