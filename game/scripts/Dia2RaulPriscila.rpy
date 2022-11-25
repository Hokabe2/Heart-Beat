label Dia2_Raul_Priscila:
    scene bg exterior

    "Eu caminho pelo pátio quando, a distância, noto um cobertor enrolado no chão. Parece apenas um cobertor, mas logo vejo um leve movimento, o qual revela um cabelo castanho escuro e um óculos."
    "Desta maneira, já consigo reconhecer quem está lá, e, por algum motivo, não me surpreendo com o resultado: é ninguém mais ninguém menos que a ladra de cookies, Priscila."

    show priscila dormindo at right with dissolve:
        matrixcolor TintMatrix("#777")
        yalign 2.0
        zoom 0.5

    "Eu estou impressionado porque nem mesmo se eu tivesse que madrugar para fazer dois trabalhos e estudar para uma prova para o dia
    seguinte eu conseguiria dormir num chão de concreto, no meio de um pátio e com um monte de gente olhando."

    "Olhando para outro lado, noto uma energia completamente oposta. Vejo Raul, alguém com uma enorme disposição para organizar o festival do centro comunitário. Ele passa pelo pátio cumprimentando a todos e verificando as ideias para o festival."
    "Logo em seguida, percebo que Raul se move em direção ao enrolado de cobertor e essas duas energias contrastantes iriam entrar em conflito. Algo vai acontecer."

    "Assim que ele me vê, ele sorri e acena para mim."



    Pris "ZZZZZZZZ"

    show raul at left:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Raul "Cara, há quanto tempo ela tá dormindo aí?"

    Ren "Não sei, ela está assim desde que cheguei."

    Pris "ZZZZZZZZZZZZ"

    "Ouvíamos roncos bem altos de Priscila."

    show raul at left:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Raul "…"

    Raul "Me dá um segundo."

    Raul "…"

    Ren "…Por que você pegou um graveto?"

    show raul at left:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Raul "Eu te mostro.
    *Cutuca* *Cutuca*"

    Raul "Ei, Pris, acorda aí, vamos trampar.
    *Cutuca* *Cutuca*"

    show priscila dormindo at right with dissolve:
        matrixcolor TintMatrix("#fff")
        yalign 2.0
        zoom 0.5

    Pris "*Grunhidos* Tô não… ZZZZZ… Jão Cookie, a sua capivara branca… ZZZZZZ"

    show raul at left:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Raul "Tá não o que? Você não estuda nem trabalha. Ficou no Tico Toque até às três da manhã de novo?"


    Pris "Ahhhh… ZZZZZZZ… Tio Astolfo, me deixa montar na capivara branca do Jão Cookie… ZZZZZZZZZZ"


    Raul "Vixi, ela ficou lendo fanfic do gordinho da Coréia."

    show priscila dormindo at right:
        matrixcolor TintMatrix("#777")
        yalign 2.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0


    Pris "Grr… Grrr…"

    "Parece que o comentário surtiu algum efeito."

    show raul at left:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Raul "Isso sempre funciona."

    Raul "Pris, o Jão Biscoito tá fazendo turnê aqui na cidade e a Alexandra tá dando em cima dele."

    Pris "Grrrr… Hmmmmm… Grrrr…."

    Pris "Hmmmmm…. Grrrrrrrr… Hrrrmmmmmmm…!!!!!"

    show priscila indignada at right:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "Jão… Jão Cookie… Quem… QUEM TÁ MEXENDO COM O MEU JÃO COOKIE!!!
    AHHHHHHHHHHHHH, AQUELA BURGUESA PERFEITA DESGRAÇADAAAAAA!!!!"

    show raul at left:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Raul "Não falei que funciona? Agora que a Bela Adormecida acordou, podemos discutir o que vamos tocar no festival. Levanta aí, se não vou chamar o Johnny."

    show priscila indignada at right:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "U-ué, mas cadê o Jão Cookie…? *Boceja*"

label Cena_Dia2RaulPriscila_Escolha_1:
    menu:
        "Namorando a Alexandra":
            jump Cena_Dia2RaulPriscila_Escolha_1_a
        "O Raul está brincando com você, não há Jão Cookie e nenhuma capivara branca também":
            jump Cena_Dia2RaulPriscila_Escolha_1_b

    #Escolha A
    #[Escolha A Raul “Namorando a Alexandra” ]
label Cena_Dia2RaulPriscila_Escolha_1_a:
    show raul at left:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Raul "Eles tão se pegando lá perto da padaria da esquina."

    show priscila pout at right:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "…"

    Pris "Eu já acordei, eu não vou cair nessa de novo… Você faz isso o tempo todo, você é malvado, Raul…"

    Pris "E você aí! Eu esperava mais de você, eu não sabia que você era mal também! Humf!"

    show raul at left:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Raul "Ok, vamos focar no assunto do dia, galera."

    Raul "Temos que decidir o que tocar no festival."

    Raul "Tenho uma lista das sugestões de música que o pessoal me indicou. Entre elas: sertanejo, rock e pop. Preciso que você vá ver se tem uma caixa de som na sala de música."

    show priscila indignada at right:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "Eh?! Por que eu?"

    show raul at left:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Raul "Porque você não pode ficar aí sem fazer nada, enquanto todo mundo tá se esforçando."

    show priscila sorriso at right:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "Na verdade, poder eu posso, tenho plena capacidade de fazer isso, provo pra todos do centro comunitário todos os dias."

    show raul at left:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Raul "*respira fundo* Tá bom, mas pode ir lá ver a caixa de som para mim?"

    show priscila serioisso at right:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "Ahhhh… Por que que não vai você? Você acabou de sair de lá de dentro."

    Ren "…"

    Raul "…"

    Pris "…"

    #Move para Continuação
    jump Cena_Dia2RaulPriscila_Escolha_1_continuacao

    #Escolha B
    #[Escolha B Priscila "O Raul está brincando com você, não há Jão Cookie e nenhuma capivara branca também"]
label Cena_Dia2RaulPriscila_Escolha_1_b:

    show priscila serioisso at right:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "Pelo menos tem alguém que não é malvado comigo, ao contrário do Raul…"

    show raul at left:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Raul "Eu não sou malvado, só tenho que agilizar as coisas do festival."

    show priscila indignada at right:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "Você fazia isso comigo mesmo quando não tinha festival…"

    show raul at left:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Raul "*tossindo* Ok, ok. Enfim, vamos focar no assunto do dia, galera."

    Raul "Temos que decidir o que tocar no festival."

    Raul "Tenho uma lista das sugestões de música que o pessoal me indicou. Entre elas: sertanejo, rock e pop. Preciso que você vá ver se tem uma caixa de som na sala de música."

    show priscila serioisso at right:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "Eh?! Por que eu?"

    show raul at left:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Raul "Porque você não pode ficar aí sem fazer nada, enquanto todo mundo tá se esforçando."

    show priscila sorriso at right:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "Na verdade, poder eu posso, tenho plena capacidade de fazer isso, provo pra todos do centro comunitário todos os dias."

    show raul at left:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Raul "*respira fundo* Tá bom, mas pode ir lá ver a caixa de som para mim?"

    show priscila serioisso at right:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "Ahhhh… Por que que não vai você? Você acabou de sair de lá de dentro."

    Ren "…"

    Raul "…"

    Pris "…"

    #Move para Continuação
    jump Cena_Dia2RaulPriscila_Escolha_1_continuacao
    #Continuação
label Cena_Dia2RaulPriscila_Escolha_1_continuacao:

    Pris "Tá bommm! Eu vou, você me deve uma camiseta do Jão Cookie com uma capivara, Raul."

    show raul at left:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Raul "Tanto faz, só vai lá pegar o som."

    Raul "Que insuportável, ela tem todos os estereótipos dos millennials e da geração Z."

    Raul "Certo, de volta ao trabalho."

    Raul "Fiz uma lista no celular das tarefas para hoje: ver os equipamentos e pesquisar um repertório de músicas de acordo com o perfil musical do nosso público."

    Raul "Você mexe com planilha Excel?"

    Ren "Eu só sei o básico."

    show raul at left:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Raul "Melhor que eu que não sei de nada."

    Raul "Vamos para a biblioteca."


    #INT- BIBLIOTECA - DIA
    scene bg recep
    with fade

    Ren "Já tô ligando aqui o computador."

    show raul at left:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Raul "Beleza, provavelmente vai demorar uns 10 minutos para abrir."

    Ren "Tudo isso?!"

    show raul at left:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Raul "Infelizmente nosso orçamento anual inexistente não cobre os custos de um computador da Nasa."

    Ren "Podemos ir pesquisando umas músicas então."

    show raul at left:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Raul "Beleza, quais tipos você ouve?"

    Ren "…"

    "Eu não ouço quase nada de música."

    Ren "Um pouco de tudo."

    show raul at left:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Raul "Show, vai ser perfeito ter um meio-termo. No time temos gostos muito distintos um do outro, quase como bolhas separadas, vai ajudar bastante ter alguém com um repertório mais variado."

    Ren "É…"

    Ren "Vou ver o que tenho na minha lista do Spotify."

    jump Cena_Dia2RaulPriscila_Escolha_2
    # tela de opções do celular - Repetir todas as opções

label Cena_Dia2RaulPriscila_Escolha_2:
    if(funk == True) and (rock == True) and (pop == True):
        "Acho que já é o bastante."
        jump Escolha_2_continuacao
    else:
        menu:
            "(funk)":
                if funk == False:
                    #Opção 1 Um funk:

                    show raul at center:
                        matrixcolor TintMatrix("#777")
                        yalign 1.0
                        zoom 0.5
                        linear 0.15 yalign 1.0
                        linear 0.15 yalign 0.85
                        linear 0.1 matrixcolor TintMatrix("#fff")
                        linear 0.15 yalign 1.0

                    Raul "Essa daí explodiu uns anos atrás."
                    $ funk = True
                    jump Cena_Dia2RaulPriscila_Escolha_2
                else:
                    "Eu deveria escolher outro tipo de música."
                    jump Cena_Dia2RaulPriscila_Escolha_2

            "(rock)":
                if rock == False:
                    #Opção 2 Música de Rock:

                    show raul at center:
                        matrixcolor TintMatrix("#777")
                        yalign 1.0
                        zoom 0.5
                        linear 0.15 yalign 1.0
                        linear 0.15 yalign 0.85
                        linear 0.1 matrixcolor TintMatrix("#fff")
                        linear 0.15 yalign 1.0

                    Raul "Boa escolha."
                    $ rock = True
                    jump Cena_Dia2RaulPriscila_Escolha_2
                else:
                    "Eu deveria escolher outro tipo de música."
                    jump Cena_Dia2RaulPriscila_Escolha_2

            "(pop)":
                if pop == False:
                    #Opção 3 Música pop:
                    show raul at center:
                        matrixcolor TintMatrix("#777")
                        yalign 1.0
                        zoom 0.5
                        linear 0.15 yalign 1.0
                        linear 0.15 yalign 0.85
                        linear 0.1 matrixcolor TintMatrix("#fff")
                        linear 0.15 yalign 1.0
                    Raul "Acho que essa vai ser perfeita."
                    $ pop = True
                    jump Cena_Dia2RaulPriscila_Escolha_2
                else:
                    "Eu deveria escolher outro tipo de música."
                    jump Cena_Dia2RaulPriscila_Escolha_2

label Escolha_2_continuacao:

    Pris "Raul!"

    show raul at left:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Raul "Pris, conseguiu achar a caixa de som?"

    show priscila feliz at right:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "Não, não estava lá."

    "A Priscila parece estar… Calma demais?"

    show raul at left:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Raul "Não estava lá? Você tentou procurar? Eu tenho certeza que eu deixei a caixa de som lá dentro. E você demorou todo esse tempo só pra vir aqui dizer isso?"

    show priscila indignada at right:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "Eu fiquei tentando procurar lá e depois que eu saí vocês não estavam mais no pátio, então tive que procurar vocês também."

    show raul at left:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Raul "*Suspira* Quer saber? Ren, pode ir com ela até a sala de música para pegar a caixa de som?"

    Ren "Por mim tudo bem."

    show priscila pout at right:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "M-mas eu acabei de falar que não estava lá!"

    show raul at left:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Raul "É só pra ter certeza."

    show priscila serioisso at right:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "Ok… Vamos lá então, Ren."

    #*Move para a sala de música*
    hide raul at left with dissolve

    "Estamos no caminho para a sala de música, a Priscila parece estar ficando cada vez mais nervosa quanto mais nos aproximamos do nosso objetivo. Suas mãos e sua testa parecem estar um pouco suadas."

    Ren "Priscila, está tudo bem? Você está suando bastante."

    show priscila feliz at right:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "E-estou? Ahhh… É que tá bem calor, deve ser o moletom ha ha ha…"

    Ren "Então por que você não tira?"

    show priscila sorriso at right:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "Ahhh… É costume, sabe? Estou sempre usando esse moletom ha ha ha…"

    "Sempre!? LITERALMENTE???"

    Ren "Bom, chegamos. Agora só vou abrir a porta e-"

    show priscila preocupada2 at right:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "ESPERA!"

    Ren "O que foi?"

    show priscila preocupada2 at right:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "Ahhhh… E-eu acho que eu tranquei a porta antes de sair e acho que deixei a chave lá na biblioteca ha ha ha, acho que teremos que ir lá buscar ha ha ha."

    Ren "Você “acha” que trancou, não? Então quer dizer que a gente pode testar antes de voltar."

    show priscila preocupada2 at right:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "NÃO, ESPERAAA!!!"

    #Ren *Gira a maçaneta*
    #*A porta se abre*
    scene bg sala de musica
    with fade

    Ren "Olha, estava destrancada."

    show priscila pout at right:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "A-ah ah… A-ah…"

    Ren "Hã? Estava bem do lado da porta, em um local bem visível, como você não achou?"

    show priscila sorriso at right:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "É… Q-que… Ahhh… Sabe, quando alguém só consegue achar coisas que são mais difíceis de achar e acaba passando despercebida com coisas fáceis de encontrar? É isso ha ha ha"

    "Ela ainda está bem nervosa e suando bastante."

    Ren "Priscila, você estava procrastinando ao invés de vir aqui e pegar a caixa de som?"

    show priscila feliz at right:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "Ahhh… Não, claro que não ha ha ha."

    Ren "Não precisa mentir, eu não vou contar pro Raul, só me diga a verdade."

    show priscila neutro at right:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "…"

    Pris "…Tá bom… Sim, eu estava procrastinando. Logo depois que eu saí do pátio eu fui para a sala de jogos e fiquei jogando por um tempo até que eu decidi procurar vocês e falar que eu não achei nada…"

    Ren "Mas por que você fez isso? A gente confiou que você iria pegar a caixa de som."

    show priscila preocupada at right:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "E por que vocês confiaram em mim? A culpa disso ter demorado mais do que devia foi de vocês, vocês que confiaram em mim. Eu estou o tempo todo sendo preguiçosa e fazendo absolutamente nada, por que vocês acharam que dessa vez iria ser diferente?"

    Ren "Mas-"

    show priscila indignada at right:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "Chega, entrega a caixa de som pro Raul, eu vou voltar para a sala de jogos…"
    #*Priscila sai da cena*

    Ren "…"
