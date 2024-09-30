from pico2d import *

open_canvas()

character = load_image('dragon.png')
# background = load_image('TUK_GROUND.png')

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
               pass
            elif event.key == SDLK_LEFT:
                pass
            elif event.key == SDLK_UP:
                pass
            elif event.key == SDLK_DOWN:
                pass
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                pass
            elif event.key == SDLK_LEFT:
                pass
            elif event.key == SDLK_UP:
                pass
            elif event.key == SDLK_DOWN:
                pass

def move_right():
    pass
def move_left():
    pass
def move_up():
    pass
def move_bottom():
    pass
def move_dragon():
    if dir == 0:
         move_right()
    elif dir == 1:
        move_left()
    elif dir == 2:
        move_up()
    elif dir == 3:
        move_bottom()
def stand_dragon():
    pass











running = True
move = False
x = 800 // 2
frame = 0
dir = 0
while running:
    clear_canvas()
    # TUK_GROUND.draw(400, 300)
    if move:
        move_dragon()
    else:
        stand_dragon()
    update_canvas()
    handle_events()
    frame = (frame + 1) % 3
    delay(0.1)

close_canvas()