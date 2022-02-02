basic.forever(function () {
    while (pins.digitalReadPin(DigitalPin.P1) == 0) {
        music.startMelody(music.builtInMelody(Melodies.Nyan), MelodyOptions.ForeverInBackground)
        break;
    }
    if (pins.digitalReadPin(DigitalPin.P0) == 0) {
        music.stopAllSounds()
        basic.showLeds(`
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            `)
    }
})
