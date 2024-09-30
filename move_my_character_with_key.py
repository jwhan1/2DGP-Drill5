from pico2d import *

open_canvas()

character_idle = load_image('Unarmed_Idle_full.png')
character_walk = load_image('Unarmed_Walk_full.png')
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
        if x < 750: x+=10
    else:
        if x > 50: x-=10
def moveY():
    global y
    if dir == 2:
        if y < 550: y+=10
    else:
        if y > 50: y-=10
def move_right():
    character_walk.clip_draw(frame * 64, 64, 64, 64, x, y, 200, 200)
def move_left():
    character_walk.clip_draw(frame * 64, 128, 64, 64, x, y, 200, 200)
def move_up():
    character_walk.clip_draw(frame * 64, 0, 64, 64, x, y, 200, 200)
def move_bottom():
    character_walk.clip_draw(frame * 64, 196, 64, 64, x, y, 200, 200)
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
    if dir == 0:
        character_idle.clip_draw(frame * 64, 64, 64, 64, x, y, 200, 200)
        frame = (frame + 1) % 5
    elif dir == 1:
        character_idle.clip_draw(frame * 64, 128, 64, 64, x, y, 200, 200)
        frame = (frame + 1) % 5
    elif dir == 2:
        character_idle.clip_draw(frame * 64, 0, 64, 64, x, y, 200, 200)
        frame = (frame + 1) % 4
    elif dir == 3:
        character_idle.clip_draw(frame * 64, 196, 64, 64, x, y, 200, 200)
        frame = (frame + 1) % 5

   










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
        frame = (frame + 1) % 6
    else:
        stand_dragon()
    update_canvas()
    handle_events()
    delay(0.1)

close_canvas()