function turnLeft (sprite: game.LedSprite) {
    sprite.turn(Direction.Left, 180)
}
input.onButtonPressed(Button.A, function () {
    sprite.turn(Direction.Right, 90)
})
function turnRight (sprite: game.LedSprite) {
    sprite.turn(Direction.Right, 180)
}
input.onButtonPressed(Button.B, function () {
    sprite.move(1)
})
input.onGesture(Gesture.Shake, function () {
    basic.showString("Next!")
    sprite = game.createSprite(2, 2)
})
let sprite: game.LedSprite = null
basic.showString("HELLO!")
sprite = game.createSprite(2, 2)
