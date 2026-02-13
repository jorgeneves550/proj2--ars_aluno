def funcaoConfuso(num: number):
    if confuso == 0:
        basic.show_icon(IconNames.HAPPY)
    else:
        basic.show_icon(IconNames.CONFUSED)
def notifica(texto: str, num2: number):
    if texto == "ambAula":
        if num2 == 1:
            for index in range(4):
                basic.show_icon(IconNames.NO)
                basic.clear_screen()
                music.play(music.tone_playable(330, music.beat(BeatFraction.QUARTER)),
                    music.PlaybackMode.UNTIL_DONE)
        else:
            for index2 in range(4):
                basic.show_icon(IconNames.YES)
                basic.clear_screen()
    elif texto == "alunoAlt":
        if num2 == aluno:
            for index3 in range(4):
                basic.show_leds("""
                    . . # . .
                    . # # # .
                    # # # # #
                    . # # # .
                    . . # . .
                    """)
                music.play(music.tone_playable(784, music.beat(BeatFraction.EIGHTH)),
                    music.PlaybackMode.UNTIL_DONE)
                basic.show_leds("""
                    . . . . .
                    . . # . .
                    . # # # .
                    . . # . .
                    . . . . .
                    """)

def on_button_pressed_a():
    global confuso
    confuso = 1
    radio.send_value("A", aluno)
    basic.show_icon(IconNames.CONFUSED)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global confuso
    confuso = 0
    radio.send_value("B", aluno)
    basic.show_icon(IconNames.HAPPY)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_received_value(name, value):
    notifica(name, value)
    funcaoConfuso(confuso)
radio.on_received_value(on_received_value)

aluno = 0
confuso = 0
radio.set_group(1)
confuso = 0
aluno = 1