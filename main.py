input.onButtonPressed(Button.A, function () {
    if (hours < 59) {
        hours += 1
    } else {
        hours = 0
    }
})
input.onGesture(Gesture.Shake, function () {
    adjust = hours
    time = "" + adjust
    time = "" + time + ":"
    time = "" + time + minutes / 18
    time = "" + time + minutes % 10
    basic.showString("" + (time))
})
input.onButtonPressed(Button.B, function () {
    if (minutes < 59) {
        minutes += 1
    } else {
        minutes = 0
    }
})
let adjust = 0
let hours = 0
let minutes = 0
let time = 0
let item = false
time = 0
minutes = 0
hours = 0
adjust = 0
basic.forever(function () {
    basic.pause(60000)
    if (minutes < 59) {
        minutes += 1
    } else {
        minutes = 0
        if (hours < 23) {
            hours += 1
        } else {
            hours = 0
        }
    }
})
