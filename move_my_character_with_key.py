from pico2d import *

open_canvas()

character = load_image('dragon.png')
background = load_image('TUK_GROUND.png')

def handle_events():
    global running, move, dir
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                move=True
                dir = 0
            elif event.key == SDLK_LEFT:
                move=True
                dir = 1
            elif event.key == SDLK_UP:
                move=True
                dir = 2
            elif event.key == SDLK_DOWN:
                move=True
                dir = 3
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                move=False
            elif event.key == SDLK_LEFT:
                move=False
            elif event.key == SDLK_UP:
                move=False
            elif event.key == SDLK_DOWN:
                move=False
def moveX():
    global x
    if dir == 0:
        x+=10
    else:
        x-=10
def moveY():
    global y
    if dir == 2:
        y+=10
    else:
        y-=10
def move_right():
    character.clip_draw(frame * 192, 192, 192, 192, x, y, 200, 200)
def move_left():
    character.clip_draw(frame * 192, 384, 192, 192, x, y, 200, 200)
def move_up():
    character.clip_draw(frame * 192, 0, 192, 192, x, y, 200, 200)
def move_bottom():
    character.clip_draw(frame * 192, 576, 192, 192, x, y, 200, 200)
def move_dragon():
    if dir == 0:
         moveX()
         move_right()
    elif dir == 1:
        moveX()
        move_left()
    elif dir == 2:
        moveY()
        move_up()
    elif dir == 3:
        moveY()
        move_bottom()
def stand_dragon():
    global frame
    frame = 1
    if dir == 0:
         move_right()
    elif dir == 1:
        move_left()
    elif dir == 2:
        move_up()
    elif dir == 3:
        move_bottom()

   










running = True
move = False
x = 800 // 2
y = 600 // 2
frame = 0
dir = 0
while running:
    clear_canvas()
    background.draw(400, 300)
    if move:
        move_dragon()
    else:
        stand_dragon()
    update_canvas()
    handle_events()
    frame = (frame + 1) % 3
    delay(0.1)

close_canvas()