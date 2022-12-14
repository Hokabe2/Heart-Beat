label Dia5Escolha:

    scene bg exterior
    with fade

    play music "audio/cute_bossa_nova.ogg" fadeout 1.0

    Ren "É meu quinto dia aqui no centro comunitário..."

    Ren "Hoje é o último dia para a organização do festival..."

    Ren "Eu vou passar o dia com quem eu mais tenho afinidade para ser mais produtivo."

    jump Dia5Menu

label Dia5Menu:

    menu:
        "Desistir":
            if (pointsJohnny < 2) and (pointsRaul < 2) and (pointsAlexandra < 2) and (pointsPriscila < 2):
                jump FinalRuim
                with fade
            else:
                "Não posso desistir agora."
                jump Dia5Menu
        "Sala de Música (Johnny)":
            if pointsJohnny >= 2:
                stop music fadeout 1.0
                jump Johnny_Dia5
                with fade
            else:
                "Não tenho muita afinidade com o Johnny."
                stop music fadeout 1.0
                jump Dia5Menu
                with fade

        "Sala de Música (Raul)":
            if pointsRaul >= 2:
                stop music fadeout 1.0
                jump Dia5_Raul
                with fade
            else:
                "Não tenho muita afinidade com o Raul."
                stop music fadeout 1.0
                jump Dia5Menu
                with fade

        "Pátio (Priscila)":
            if pointsPriscila >= 2:
                stop music fadeout 1.0
                jump Dia5_Priscila
                with fade
            else:
                "Não tenho muita afinidade com a Priscila."
                stop music fadeout 1.0
                jump Dia5Menu
                with fade

        "Sala de Música (Alexandra)":
            if pointsAlexandra >= 2:
                stop music fadeout 1.0
                jump Alexandra_Dia5
                with fade
            else:
                "Não tenho muita afinidade com a Alexandra."
                stop music fadeout 1.0
                jump Dia5Menu
                with fade
