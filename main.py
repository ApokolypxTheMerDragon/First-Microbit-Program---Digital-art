def turnLeft(sprite: game.LedSprite):
    sprite.turn(Direction.LEFT, 45)

def on_gesture_tilt_left():
    turnLeft(sprite)
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def turnRight(sprite: game.LedSprite):
    sprite.turn(Direction.RIGHT, 45)

def on_button_pressed_ab():
    global sprite
    sprite = game.create_sprite(2, 2)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    sprite.move(1)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_tilt_right():
    turnRight(sprite)
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

sprite: game.LedSprite = None
basic.show_string("Hello!")