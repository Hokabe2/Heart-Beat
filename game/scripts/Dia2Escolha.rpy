label Dia2Escolha:

    Ren "Meu segundo dia aqui no centro comunitário..."

    Ren "Até onde eu sei, o Johnny e a Alexandra estão na sala de música."

    Ren "E a o Raul e a Priscila estão no pátio."

    Ren "Preciso decidir para onde eu vou."

    menu:
        "Sala de música (Johnny e Alexandra)":
            stop music fadeout 1.0
            jump JohnnyAlexandra
            with fade
        "Pátio (Raul e Priscila)":
            stop music fadeout 1.0
            jump Dia2_Raul_Priscila
            with fade
