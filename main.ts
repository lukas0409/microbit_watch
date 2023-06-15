input.onButtonPressed(Button.A, function () {
    if (hours < 24) {
        hours += 1
    } else {
        hours = 0
    }
})
input.onGesture(Gesture.Shake, function () {
    adjust = hours
    time = "" + adjust
    time = "" + time + ":"
    time = "" + time + minutes
    basic.showString(time)
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
let time = ""
let item = false
time = ""
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
