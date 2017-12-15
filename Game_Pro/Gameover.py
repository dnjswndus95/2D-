from pico2d import*
import game_framework
import main_state
import title_state

image = None
font = None
BGM = None

def enter():
    global image, font, BGM
    image = load_image('gameover.png')
    font = load_font('ENCR10B.TTF', 50)
    BGM = load_wav('gameover.wav')
    BGM.set_volume(60)
    BGM.play()

def draw(frame_time):
    global image, font, Score
    clear_canvas()
    image.draw(400, 300)
    font.draw(600, 400, 'Score : %d' % main_state.Score, (0, 0, 0))
    update_canvas()

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_r):
            game_framework.pop_state()

def update(frmae_time):
    pass

def pause():
    pass

def resume():
    pass