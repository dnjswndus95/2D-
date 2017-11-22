from pico2d import*

class Background:
    PIXEL_PER_KMETER = (10.0/0.5)
    RUN_SPEED_KMPH = 36000.0
    RUN_SPEED_KMPM = RUN_SPEED_KMPH / 60
    RUN_SPEED_KMPS = RUN_SPEED_KMPM / 60
    RUN_SPEED_PPS = RUN_SPEED_KMPS * PIXEL_PER_KMETER


    def __init__(self, w, h):
        self.image = load_image('background.png')
        self.speed = 0
        self.width = 0
        self.screen_width = w
        self.screen_height = h

    def draw(self):
        x = int(self.width)
        w = min(self.image.w - x, self.screen_width)
        self.image.clip_draw_to_origin(x, 0, w, self.screen_height, 0, 0)
        self.image.clip_draw_to_origin(0, 0, self.screen_width - w, self.screen_height, w, 0)
        #clip_draw_to_origin(self, left, botton, width, height, x, y, w, h)

    def update(self, frame_time):
        self.speed = Background.RUN_SPEED_PPS
        self.bottom = (self.width + frame_time * self.speed) % self.image.w

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT: self.speed -= Background.RUN_SPEED_PPS
            elif event.key == SDLK_RIGHT: self.speed += Background.SCROLL_SPEED_PPS

        if event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT: self.speed += Background.RUN_SPEED_PPS
            elif event.key == SDLK_RIGHT: self.speed -= Background.SCROLL_SPEED_PPS

