label Dia5Escolha:

    Ren "É meu quinto dia aqui no centro comunitário..."

    Ren "Hoje é o último dia para a organização do festival..."

    Ren "Eu vou passar o dia com quem eu mais tenho afinidade para ser mais produtivo."

    jump Dia5Menu

label Dia5Menu:

    menu:
        "Sala de Música (Johnny)":
            if pointsJohnny >= 2:
                stop music fadeout 1.0
                jump Dia3_RaulJohnny
                with fade
            else:
                "Não tenho muita afinidade com o Johnny."
                stop music fadeout 1.0
                jump Dia5Menu
                with fade

        "Sala de Música (Raul)":
            if pointsRaul >= 2:
                stop music fadeout 1.0
                jump Dia3_RaulJohnny
                with fade
            else:
                "Não tenho muita afinidade com o Raul."
                stop music fadeout 1.0
                jump Dia5Menu
                with fade

        "Pátio (Priscila)":
            if pointsPriscila >= 2:
                stop music fadeout 1.0
                jump Dia3_RaulJohnny
                with fade
            else:
                "Não tenho muita afinidade com a Priscila."
                stop music fadeout 1.0
                jump Dia5Menu
                with fade

        "Sala de Música (Alexandra)":
            if pointsAlexandra >= 2:
                stop music fadeout 1.0
                jump Dia3_RaulJohnny
                with fade
            else:
                "Não tenho muita afinidade com a Alexandra."
                stop music fadeout 1.0
                jump Dia5Menu
                with fade
