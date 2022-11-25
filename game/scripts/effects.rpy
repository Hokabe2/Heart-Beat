init python:

    def ShowText(characterName, _text):
        renpy.say(characterName, _text)

    config.underlay.append(
        renpy.Keymap(
            mousedown_1 = lambda: renpy.run(renpy.play("audio/mixkit-interface-click-1126.ogg"))
        )
    )

### EFFECTS PREFABS ###

## Effect when the character enter the scene ##
    #show alexandra happy at center with dissolve:
    #    matrixcolor TintMatrix("#777")
    #    yalign 1.0
    #    zoom 0.5

## Animate character when start talking ##
    #show alexandra happy at left:
    #    matrixcolor TintMatrix("#777")
    #    yalign 1.0
    #    zoom 0.5
    #    linear 0.15 yalign 1.0
    #    linear 0.15 yalign 0.85
    #    linear 0.1 matrixcolor TintMatrix("#fff")
    #    linear 0.15 yalign 1.0

## Animate character when stop talking ##
    #show potato sad at right:
    #    matrixcolor TintMatrix("#fff")
    #    yalign 1.0
    #    zoom 0.5
    #    linear 0.1 matrixcolor TintMatrix("#777")

## Music and Sound Effects ##
    #   play sound "audio/effect.ogg"
    #   stop sound fadeout 5.0
    #   play music "audio/illurock.ogg"
    #   play music "audio/illurock.ogg" fadeout 1.0 fadein 1.0 --> Used to fade between an old and a new music

## Scene Transition Effect ##
    #   with fade

##Flash out effect
    #   scene example with flash
init:
    $ flash = Fade(.25, 0, .75, color="#fff")
