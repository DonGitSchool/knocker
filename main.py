def on_forever():
    images.create_big_image("""
        . # # # . . . # . #
                # . # # # . # . # .
                # # # # # . . . . .
                # # # # # . . # . #
                . # . # . . # . # .
    """).show_image(1, 20)
    while pins.digital_read_pin(DigitalPin.P1) == 0:
        music.start_melody(music.built_in_melody(Melodies.NYAN),
            MelodyOptions.FOREVER_IN_BACKGROUND)
        pins.digital_write_pin(DigitalPin.P1, 1)
        break
    if pins.digital_read_pin(DigitalPin.P0) == 0:
        music.stop_all_sounds()
        basic.show_leds("""
            # . . . #
                        . # . # .
                        . . # . .
                        . # . # .
                        # . . . #
        """)
basic.forever(on_forever)
