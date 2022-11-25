label Dia4Escolha:

    scene bg exterior
    with fade

    play music "audio/cute_bossa_nova.ogg" fadeout 1.0

    Ren "Meu quarto dia aqui no centro comunitário..."

    Ren "O Johnny e a Priscila haviam marcado de ir na sala de música de manhã."

    Ren "E o Raul e a Alexandra marcaram de tarde."

    Ren "Preciso decidir quando eu vou para a sala de música."

    menu:
        "Manhã (Johnny e Priscila)":
            stop music fadeout 1.0
            jump Dia4_PriscilaJohnny
            with fade
        "Tarde (Raul e Alexandra)":
            stop music fadeout 1.0
            jump Dia4_RaulAlexandra
            with fade
