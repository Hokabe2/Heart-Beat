label Dia5_Priscila:
    #EXT - PÁTIO DO CENTRO COMUNITÁRIO - MANHÃ
    scene bg patio

    play music "audio/home.ogg" fadeout 1.0

    "Certo, esse é o último dia para arrumar as coisas para o festival. Cada um dos membros do centro comunitário já se direcionaram para suas tarefas."

    "O Raul, a Alexandra e o Johnny já estão ensaiando com seus respectivos instrumentos. Mas… E a Priscila? Eu não vi ela desde o início do dia…"

    "Talvez ela esteja roubando comida da geladeira da copa e esqueceu de fazer as coisas dela, acho bom eu dar um puxão de orelha nela antes de fazer o que eu planejei pra hoje."
    #[Move-se para a Copa do Centro Comunitário]

    #INT - COPA DO CENTRO COMUNITÁRIO - MANHÃ
    scene bg copa

    "Cheguei, agora é só olhar para a geladeira que ela…"

    "Ué, ela não está aqui?"

    "Hmm… Ela não está aqui na copa, a sala de música está ocupada e ela não está deitada no chão do pátio. A Priscila passa a maior parte do tempo aqui no centro comunitário, então deve ter mais algum lugar que ela possa estar. Vou tentar perguntar pra alguém aqui do centro comunitário."

    "Estou com um mal pressentimento…"

    #EXT - PÁTIO DO CENTRO COMUNITÁRIO - MANHÃ
    scene bg patio
    "Avistei o Johnny, ele deve estar fazendo um breve intervalo da sua prática com a guitarra, acho que vou perguntar pra ele."

    Ren "Opa, olá, Johnny."

    show joh neutro1 at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Joh "Ren? E aí."

    Ren "Johnny, posso te perguntar uma coisa?"

    show joh sorrindo1 at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Joh "Contando com essa são duas."

    Ren "É sobre a P-Priscila! Ela está sumida desde o início do dia, você viu ela em algum lugar?"

    show joh neutro2 at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Joh "A anã de jardim? Não vi."

    Ren "Talvez… Mas, ainda assim, ela normalmente estaria em algum lugar aqui do centro comunitário. Você sabe de alguém que sabe onde ela está?"

    show joh neutro1 at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Joh "Tenta falar com a Alexandra ou o Raul."

    Joh "Foi mal eu preciso voltar a praticar, falou."
    #[Sai da cena]

    Ren "Ah… Falou…"

    #INT - SALA DE MÚSICA DO CENTRO COMUNITÁRIO - MANHÃ

    scene bg sala de musica
    "Vou até a sala de música e encontro a Alexandra tocando uma bela melodia em seu piano com extrema concentração. Ela deve estar levando o festival realmente a sério, acho melhor eu esperar ela terminar de tocar a música para que eu fale com ela."

    show alexandra neutral at center:
        matrixcolor TintMatrix("#fff")
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    Ale "*Tocando a melodia*"

    Ren "…"

    Ale "*Continua tocando*"

    Ren "..."

    Ale "*Finaliza a melodia com perfeição*"

    show alexandra happy at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Ale "Ren?"

    Ren "Ah, Alexandra. Eu preciso fazer uma pergunta, você sabe onde está a Priscila? Eu não vi ela desde o início do dia."

    show alexandra neutral at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Ale "A Priscila? Não a vi, estive aqui na sala de música desde que cheguei. Possivelmente o Raul sabe, ele sempre está interagindo com todos no centro comunitário. Ele está na recepção realizando algumas tarefas para o festival."

    Ren "Ahh, tá certo! Obrigado pela informação."

    Ale "Por nada."

    #INT - RECEPÇÃO DO CENTRO COMUNITÁRIO - MANHÃ
    scene bg recep

    "Cheguei na recepção. Logo de cara eu avisto um grupo de pessoas em torno de um único indivíduo. Já sei onde está o Raul."
    Raul "Ok, então eu preciso que você arrume isso lá na biblioteca enquanto nós mexemos com a entrada."

    Ren "Opa, Raul."

    show raul neutro at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0


    Raul "Ah, Ren? Tranquilo? Precisa de alguma coisa?"

    Ren "Na verdade sim, eu estou procurando a Priscila, ela está sumida desde o início do dia."

    show raul neutro at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0


    Raul "Priscila? Você procurou na geladeira da copa?"

    Ren "Sim."

    show raul neutro at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0


    Raul "Na cama provisória dela no pátio, também conhecida como 'chão'?"

    Ren "Sim, também."

    show raul pensativo at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0


    Raul "*Suspira* Hmmm, eu imaginei que isso poderia acontecer."

    Ren "Mas você acha mesmo que a Priscila iria procrastinar logo no último dia de preparação do festival?"

    show raul neutro at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0


    Raul "Na real, é exatamente por conta de ser o último dia que eu imaginei que ela faria isso."

    Ren "Como assim? O que tem haver?"

    show raul neutro at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0


    Raul "Bom, eu não sei os detalhes e nem sei se isso é realmente verdade, mas ao meu ver parece que a Priscila tem seus motivos para ser preguiçosa do jeito que ela é."

    Raul "Eu já vi gente preguiçosa, só que o jeito preguiçoso dela é diferente, manja?"

    Ren "Diferente? Em qual sentido?"

    show raul pensativo at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0


    Raul "Hã… Como eu posso explicar…?"

    Raul "Não é como se ela não tivesse nenhuma habilidade, na verdade é bem o contrário. É só que… Parece que tem algo que segura ela, saca?"

    #[OPÇÃO 1: Caso o Jogador tenha visto a cena do dia 3 da Priscila e da Alexandra]
    if talkToPriscila3 == True:
        Ren "Realmente, eu já vi a Priscila cantando e dançando, ela é muito boa, não parece que ela é alguém que só come, dorme e joga videogame o dia todo…"
    else:
    #[OPÇÃO 2: Caso a opção 1 não seja verdade]
        Ren "Quais habilidades a Priscila tem? Até agora eu só vi ela comendo e dormindo o dia todo."

        show raul feliz at center:
            matrixcolor TintMatrix("#777")
            yalign 1.0
            zoom 0.5
            linear 0.15 yalign 1.0
            linear 0.15 yalign 0.85
            linear 0.1 matrixcolor TintMatrix("#fff")
            linear 0.15 yalign 1.0


        Raul "Ah, você nunca viu a Priscila dançando e cantando? Se não, deveria ver, ela é boa demais. Eu nem curto o estilo de música dela, mas ver ela dançando e cantando faz todo mundo se contagiar com a animação das músicas."

        Ren "Hmmm… Mas então se ela tem habilidades nesse nível, por que ela não demonstra isso com mais frequência?"

    #[CONTINUAÇÃO]

    show raul neutro at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Raul "Exatamente, esse é o meu ponto."

    Ren "Outra questão é saber onde ela está…"

    Raul "Hmmm…"

    show raul feliz at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0


    Raul "Ah! Cara, como eu não pensei nisso!"

    Ren "O que foi?"

    show raul feliz at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0


    Raul "Você já foi dar uma olhada na sala de jogos?"

    Ren "Não fui, mas é que na verdade eu nunca fui lá, então não sei onde fica."

    show raul feliz at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0


    Raul "Fica em um canto no fundo do pátio do centro comunitário. Você vai ver tipo um quarto pequeno com uma porta de metal."

    "Essa descrição não ajudou muito… ha ha ha…"

    Ren "…Será que não é melhor você ir junto?"

    show raul neutro at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0


    Raul "Foi mal, Ren, vou ter que deixar essa com você, eu estou bastante ocupado por aqui."

    Ren "Ah, ok. Eu vou dar um jeito."

    show raul sorrindo at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0


    Raul "Beleza, confio em você."

    #EXT - PÁTIO DO CENTRO COMUNITÁRIO - MANHÃ

    scene bg patio
    "Tá certo, agora eu tenho que achar a sala de jogos…"

    "*Anda até o fundo do pátio*"

    "O Raul disse que fica em um canto no fundo do pátio… e… Vai ter tipo um quarto…"

    "*Procura*"

    "Ah! Eu achei!"

    "Pelo incrível que pareça, foi exatamente como o Raul descreveu, um pequeno quarto com uma porta de metal em um canto no fundo do pátio. Apesar de ser relativamente grande, é bem maior do que eu imaginava."

    "Por favor, que a Priscila esteja aqui…"

    Ren "*Bate na porta*"

    Ren "Priscila, você está aí?"

    "…"

    "Nenhuma resposta… Será que ela está dormindo?"

    Ren "*Bate na porta novamente, dessa vez um pouco mais forte*"

    Ren "Priscila, aqui é o Ren, se você estiver aí, por favor responda."

    Ren "*Bate na porta mais uma vez*"

    Ren "Hoje é o último dia para arrumar as coisas do festival e as pessoas estão precisando de você. Mas… Na verdade eu só vim aqui pra saber se você está bem. Você sumiu desde o início do dia, eu estou preocupado…"

    "Será que na verdade ela não está aqui e eu estou falando sozinho?"

    "…"

    "*Ouve um som*"

    "Espera… Tem algum som vindo da sala de jogos…"

    "…"

    "*Ouve uma fungada*"

    "É uma fungada… A Priscila… Está chorando?"

    Ren "*Bate na porta*"

    Ren "Priscila, eu consigo te ouvir. Por favor, só me fala o que está acontecendo…"

    "Eu consigo ouvir alguns passos, ela está se aproximando da porta lentamente."

    Pris "*Fungada*"

    Ren "Priscila?"

    Pris "…"

    Ren "Hm…?"

    Pris "Dá medo, não dá?"

    Ren "Medo…?"

    Pris "Toda essa situação… Os olhares… "

    Pris "O julgamento das pessoas…"

    Pris "O esforço de todo mundo…"

    Pris "O Raul está criando a comunicação entre todos os setores do centro comunitário e está organizando o festival para trazer a melhor experiência possível."

    Pris "O Johnny, apesar de sempre de um jeito assustador, está tentando ajudar todo mundo em suas tarefas, além de também auxiliar com as aulas de violão."

    Pris "E a Alexandra está praticando sem parar para manter a perfeição de suas músicas."

    Pris "E todo mundo do centro comunitário também está dando o melhor de si…"

    Pris "Toda essa pressão para ser o melhor possível e superar expectativas é assustadora. É como se todos estivessem te observando a todo momento para que você alcance ou até ultrapasse os resultados que eles esperam."

    "É notável a aflição de Priscila em sua entonação. A voz chamativa que eu ouvi todos os outros dias desapareceu completamente, parece outra pessoa."

    Ren "Mas… Então por que não se esforçar também? As pessoas te enxergariam de forma positiva e não te julgariam."

    Pris "Mas e se der tudo errado?"

    Pris "E se eu falhar e meu esforço for em vão?"

    Pris "E se meu esforço não for suficiente e eu decepcionar as pessoas?"

    Ren "…"

    "Acho que agora eu entendi…"

    "Parece que a suposição do Raul estava certa, a Priscila realmente tem um motivo para ser preguiçosa."

    Ren "Priscila… Eu posso entrar? Acho que fica mais fácil para nós conversarmos…"

    Pris "…"

    Ren "Eu estou sozinho. Mais ninguém sabe que você está aqui."

    Pris "A porta da sala de jogos não tem tranca…"

    Ren "Ah…"

    "Verdade, por que eu não tinha pensado em girar a maçaneta?"

    "*Abre a porta*"

    show priscila preocupada at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0


    "Ao abrir eu vejo a expressão melancólica de Priscila."

    "Ao fundo, me deparo com uma grande sala quase vazia. A única coisa que tem aqui são duas mesas, uma com uma caixa de som, que suponho que a Priscila use para aumentar o som dos jogos, e outra com o PC gamer que a Priscila usa, o qual está bem descuidado pra falar a verdade… Será que a Priscila sequer limpa ele?"

    "Por que essa sala de jogos está tão vazia? Até onde eu sei, normalmente uma sala de jogos teria diversos objetos, como mesas de tênis de mesa ou mesas de pebolim…"

    Ren "Você deve estar bem pra baixo mesmo… Por que não joga um pouco no PC pra se distrair um pouco? O que você joga aqui?"

    "Vou ligar o PC pra ela pra dar uma forcinha."

    show priscila preocupada at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0


    Pris "N-não, espera!"

    "*Pega o cabo do PC*"

    "Espera… Mas… Cadê a tomada?"

    Ren "Não… Não tem tomada…?"

    Pris "…"

    "Eu procuro ao redor, mas também não encontro nenhum lugar para conectar…"

    Ren "Priscila… Esse computador… Você…"

    Ren "Sequer usa ele…?"

    show priscila preocupada at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "E-eu…"

    "Então por qual motivo a Priscila utilizaria essa sala de jogos?"

    "Hmm… A resposta… Deve estar aqui…"

    "Olhando ao meu redor…"

    "…"

    "É… É claro! Faz completo sentido!"

    "O computador sujo… A sala vazia…"

    "A caixa de som… O medo da Priscila… As habilidades dela… Uma sala onde ninguém vai…"

    Ren "Priscila…"

    show priscila preocupada at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "E-eu."

    Ren "Você… "

    Ren "Usa essa sala para praticar dança e canto?"

    show priscila preocupada at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "Hm!? P-por que você acha isso?"

    Ren "Bom, faz todo sentido! Você tem medo que os outros te julguem em sua competência para fazer as coisas, então por isso você se esconde para praticar. Além disso, aqui não tem tomada para ligar o PC e a sala é vazia e inutilizada pelo Centro Comunitário, sendo um lugar muito conveniente para você praticar sua dança. O que quer dizer, portanto, que o PC é apenas uma desculpa para não desconfiarem do que você faz aqui."

    Ren "Eu estou certo, não estou?"

    Pris "…"

    Ren "Hã… Estou?"

    show priscila neutro at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "S-sim…"

    Ren "…"

    show priscila serioisso at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "Mas eu sei que é idiotice! Não tem por que alguém ficar se escondendo dos outros! Por favor, não conta pra ninguém! Eu-"

    Ren "Pfft…"

    show priscila serioisso at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "Hã?"

    Ren "Hmhmhmh… Hmhmhmhmhmhm…"

    Ren "HAHAHAHAHAHA!!"

    "Eu não sei o porquê, mas toda essa situação me fez rir sem parar."

    show priscila indignada2 at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "D-do que você está rindo!?"

    Ren "HAHAHAHAHA! Desculpa, é que- HAHAHAHAHAHA!!!"

    Ren "Priscila, você é incrível!"

    show priscila preocupada2 at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "Hã!?"

    Ren "Sim! Eu realmente te admiro!"

    show priscila chorando at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "Como assim você me admira!? Eu sou sempre super preguiçosa e eu além disso sou medrosa! E agora você sabe de tudo isso!"

    Ren "Você não é medrosa! Muito pelo contrário! Você é alguém muito corajosa!"

    show priscila neutro at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "O que!?"

    Ren "Priscila, coragem não é a falta de ter medo, mas sim ter medo, mas enfrentar as situações mesmo assim!"

    show priscila serioisso at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "Mas eu… Só fujo de tudo e finjo ser preguiçosa… Eu pratico sozinha porque eu tenho medo que os outros vejam o que eu faço e me julguem caso eu cometa algum erro. Esse medo não me torna corajosa, me torna egoísta! Eu sempre atrapalho os outros…"

    Ren "Mas ainda assim você se esforça! Mesmo que escondida, você se esforça para se tornar alguém melhor! Isso significa que você não se sente confortável em se manter no mesmo nível e por conta disso você decide treinar! É isso que eu admiro em você!"

    show priscila preocupada at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "Mas o que adianta se eu não consigo fazer as coisas quando os outros estão olhando!?"

    Ren "É claro que consegue!"

    Ren "Priscila, ninguém consegue fazer tudo sozinho, não importa o quanto nos esforcemos. Às vezes nós precisamos de um empurrão de outras pessoas. Pessoas que são importantes e queridas para nós."

    Ren "Eu percebi isso aqui no Centro Comunitário."

    Ren "Eu não conseguiria estar fazendo o meu trabalho da faculdade se o Tio Astolfo não tivesse me enviado o e-mail cinco dias atrás."

    Ren "Eu não iria conseguir ajudar a arrumar o festival e me sentir bem fazendo isso se não fosse pela própria ajuda das pessoas incríveis que eu conheci aqui no centro comunitário. O Raul, a Alexandra, o Johnny e, você também, Priscila… Todos me ajudaram com isso."

    Ren "Então o que você precisa é de um empurrão. E eu posso te ajudar com isso se você quiser, assim como você me ajudou."

    #[OPÇÃO: Caso o Jogador tenha visto a cena do dia 3 da Priscila e da Alexandra]
    if talkToPriscila3 == True:
        Ren "E você já recebeu esse empurrão uma vez. Você lembra daquela hora na sala de música com a Alexandra? Você arrasou naquele momento!"

    #[CONTINUAÇÃO]

    show priscila preocupada at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "Ren…"

    "Começo a ver lágrimas nos olhos da Priscila."

    show priscila chorando2 at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "R-ren… Buaaaahhhhhh!!! Obrigadaaaaa!!!! Ahhhhh!!!"

    Ren "Ha ha, por nada! Eu- Na verdade, não só eu, todos daqui do centro comunitário, estamos aqui por você."

    show priscila chorando2 at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "Buaaaaaaahhhhh!
    *Fungada*"

    "As fungadas voltaram ha ha ha…"

    show priscila chorando2 at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "*Super fungada*"

    Ren "Priscila, eu só preciso que você me ajude a te ajudar."

    Pris "Sniff, Sniff… Como assim?"

    Ren "Você tem medo de como os outros vão te julgar certo? No sentido que você não quer que eles imponham expectativas mais altas do que deveriam."

    Pris "Sim… Sniff"

    Ren "Então eu preciso que você me conte quais são suas habilidades e suas limitações. Ou seja, eu quero que você me mostre do que você é realmente capaz!"

    Pris "Você quer dizer…"

    Ren "Sim, eu preciso que você me mostre a sua apresentação para o festival do centro comunitário. Eu quero saber o que devemos esperar de sua apresentação. Com isso, eu consigo comunicar para os outros as suas verdadeiras capacidades."

    Pris "…"

    Ren "Hm… Tudo bem por você?"

    Pris "…"

    hide priscila at center with dissolve

    "Ela se virou e saiu andando…"

    "Ela pegou a caixa de som e ligou."

    show priscila feliz at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "Hi hi hi! É claro que sim!"

    #[música toca]

    Ren "Priscila…!"

    show priscila feliz at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "Hi hi hi! Jão Cookie! Me abençoe com sua beleza! E olhe para mim!"

    "O Jão Cookie por acaso é um deus!?"

    show priscila sorriso at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "DJ, arrebenta, pode ligar o som!"

    "Hã… Não tem nenhum DJ aqui além da própria caixa de som…"

    Ren "I-isso aí! Essa é a Priscila que eu conheço!"

    #[time skip de alguns minutos]

    "A música foi tocando e a Priscila dançava e cantava no decorrer dela. A sensação de ver ela se apresentando é realmente animadora! Ela contagia quem assiste com tamanha alegria, é como se eu estivesse com mais energia, eu estou ligado no 220!"

    show priscila feliz at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "Huff… Huff… Huff…"

    Pris "E aí? Foi… Razoável, né?"

    Ren "Razoável!? Priscila! Você foi simplesmente sensacional!"

    Pris "Pera, sério!?"

    Ren "Sim! Com certeza o Jão Cookie estaria orgulhoso de você!"

    show priscila animada at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "Yaaaaayyy!! Hahahaha!"

    "Parece que a alegria dela voltou ha ha ha!"

    Ren "Agora eu já sei o que esperar das suas habilidades, não precisa se preocupar mais com isso."

    Ren "E em relação a ajudar na organização do centro comunitário… Hmmm…"

    Ren "Só faça o que for possível, não precisa se pressionar para fazer algo que você não se sente confortável em fazer, ok?"

    show priscila sorriso at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "Okayyy!"

    Ren "Agora deveríamos ir até a recepção, o Raul deve estar precisando de uma ajuda, ele está com bastante coisa pra fazer."

    #*Transição de tela*

    #EXT - PÁTIO DO CENTRO COMUNITÁRIO - MANHÃ
    scene bg patio

    "No caminho eu e Priscila estávamos conversando. Quer dizer… Mais ou menos… Admito que era uma conversa unilateral, ela ficou o tempo todo falando do Jão Cookie.
    No meio disso, uma dúvida se instalou em minha cabeça."

    Ren "Inclusive, Priscila, não querendo cortar o assunto, mas eu tenho uma pergunta."

    show priscila sorriso at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "Hm? Pode falar!"

    Ren "Bom, é que-"

    Pris "Hi hi hi! Eu já sei! Você quer saber da vez que o Jão Cookie salvou milhares de pessoas do ataque de um dragão capivara gigante branco de três cabeças e olhos azuis, né?"

    "De onde ela tirou isso!?"

    Ren "Na verdade-"

    show priscila feliz at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "Tudo bem, fica tranquilo! Ele não matou a capivara, ele é bondoso demais para isso! Ele e a capivara se tornaram amigos e hoje em dia o Jão Cookie-"

    Ren "PRISCILA!"
    show priscila neutro at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "E-eu!"

    Ren "Na verdade, se você não se importar em dizer, eu queria saber o motivo de você ter medo do julgamento das pessoas."

    Pris "Ah, isso?"

    Ren "Sim. Porque aqui no centro comunitário eu não vejo as pessoas te pressionando para ser super produtiva. Na verdade, apesar de você agir de forma preguiçosa, as pessoas nem se importam tanto assim com isso. Então esse problema deve ter surgido de outro lugar, não?"

    Pris "Sim. Esse problema surgiu na minha casa."

    show priscila preocupada at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "Os meus pais sempre me pressionaram muito para ser a melhor pessoa possível: notas altas, boa nos esportes, extremamente madura. E eu me esforçava para conseguir isso, mas nunca era suficiente, porque eu tenho a minha irmã mais velha."

    Ren "Você tem uma irmã?"

    show priscila preocupada at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "Sim, e ela é tudo que meus pais sempre quiseram, ela é extremamente esforçada e sempre conseguiu superar as expectativas em tudo. E por conta disso eles sempre quiseram que eu fosse como ela. Mesmo que eu tivesse a maior nota da minha turma na escola, mesmo que eu tivesse habilidades físicas melhores do que de muitas pessoas, nunca era o suficiente, eu nunca consegui alcançar o nível dela."



    Ren "Então você passa muito tempo aqui no centro comunitário exatamente porque você não tem toda essa pressão aqui, certo?"

    show priscila neutro at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "Sim, aqui é o único lugar em que eu posso ficar mais tranquila, é onde eu posso relaxar sem que estejam o tempo todo me julgando."

    show priscila preocupada at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "Mas, ainda assim, o medo que eu tenho do julgamento dos meus pais ainda me persegue. É como se eles ficassem na minha cabeça o tempo todo dizendo que eu ainda não sou boa o suficiente."

    "Isso deve ser difícil, acho que agora eu entendo um pouco sobre o que a Priscila passa…"

    Ren "Obrigado, Priscila, por compartilhar sua experiência."

    show priscila sorriso at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "Ah, por nada!"

    show priscila feliz at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "Hahaha! Você pareceu um jornalista falando!"


    Ren "Ahaha! Fico feliz em ouvir isso. Aliás, eu estou estudando para ser um!"

    jump FinalPriscila
    with fade
    #[Fim]
