label Dia3Escolha:

    Ren "Meu terceiro dia aqui no centro comunitário..."

    Ren "O Johnny e o Raul estão na sala de música."

    Ren "E acho que a Priscila e a Alexandra estão na Copa."

    Ren "Preciso decidir para onde eu vou."

    menu:
        "Sala de música (Johnny e Raul)":
            stop music fadeout 1.0
            jump Dia3_RaulJohnny
            with fade
        "Copa (Priscila e Alexandra)":
            stop music fadeout 1.0
            jump Dia3_AlexandraPriscila
            with fade
