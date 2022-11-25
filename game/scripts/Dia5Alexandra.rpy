label Alexandra_Dia5:

    scene bg exterior
    with fade

    "Ontem, após bastante discussão, todos conseguiram decidir o estilo e os instrumentos que queriam tocar."

    "Então eu acho que vou ir checar a Alexandra, que está na sala de música."

    play music "audio/5_Dramatic_2_Master.ogg"

    "Próximo à entrada da sala, eu consigo ouvir uma melodia de piano sendo tocada novamente…"

    "Mas... A música não está saindo como sempre."

    jump Alexandra_Dia5_Sala_De_Musica
    with fade

label Alexandra_Dia5_Sala_De_Musica:

    scene bg sala de musica
    with fade

    show alexandra sigh at center with dissolve:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5

    "Eu entro na sala de música e vejo ela lá, no piano como de costume."

    "Mas ela está errando várias notas.  E isso não é normal para alguém sempre beirando a perfeição como ela."

    "Ouvir essa melodia falha chega a ser desnorteante."

    "Ela nota minha presença e se vira para mim."

    show alexandra sad at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5

    Ren "A-Alexandra está tudo bem…? Porque você está tremendo assim?"

    show alexandra sad at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Ale "Não… Não é nada..."

    "Ela tenta se recompor, mas eu noto ela tentando esconder uma marca vermelha em seu pulso com sua manga."

    "Imediatamente seguro seu braço para olhar mais de perto."

    show alexandra angry at center:
        matrixcolor TintMatrix("#fff")
        yalign 1.0
        zoom 0.5

    Ale "Ei! O que está fazendo!?"

    show alexandra angry at center:
        matrixcolor TintMatrix("#fff")
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    Ren "Eu que te pergunto!!"

    Ren "O que são essas marcas?! Quem que fez isso com você?"

    "O braço dela estava cheio de marcas vermelhas como se fosse de palmatória."

    "Não consigo conter minha preocupação e raiva."

    "Alexandra puxa seu braço de mim e morde seus lábios."

    show alexandra sad at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Ale "F-Foram meus pais… E-Eles não querem que eu venha mais para o centro."

    Ale "Mas eu relutei e…"

    show alexandra sigh at center:
        matrixcolor TintMatrix("#fff")
        yalign 1.0
        zoom 0.5

    Ale "Sofri as consequências..."

    Ale "Eu estava tentando tocar um pouco para me acalmar... Mas... E-eu não consigo…"

    Ale "Eu sinto a dor latejar em meus braços."

    show alexandra sad at center:
        matrixcolor TintMatrix("#fff")
        yalign 1.0
        zoom 0.5

    Ale "D-Desse jeito eu não vou conseguir tocar no festival. Vai dar tudo errado e vai ser tudo culpa minha–"

    show alexandra sad at center:
        matrixcolor TintMatrix("#fff")
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    Ren "A-Alexandra! Se acalme!"

    "Eu seguro ela pelos ombros."

    "Ela está tremendo muito forte."

    "Eu nunca achei que fosse ver ela de forma tão vulnerável assim."

    show alexandra sad at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Ale "..."

    "Eu solto os ombros dela e seguro suas mãos no lugar. Ela lentamente para de tremer."

    show alexandra sad at center:
        matrixcolor TintMatrix("#fff")
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    Ren "Eu não sei o que aconteceu ou qual a relação entre você e seus pais… Mas se acalme."

    Ren "Você está se esforçando muito para esse festival no final das contas."

    Ren "Então, vamos se desconectar de tudo e dar uma relaxada."

    Ren "O que acha de sairmos um pouco, Alexandra?"

    "Ela respira fundo e se levanta."

    show alexandra sigh at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Ale "Sinto muito que você teve que me ver nesse estado tão indigno de minha pessoa…"

    show alexandra neutral at center:
        matrixcolor TintMatrix("#fff")
        yalign 1.0
        zoom 0.5

    Ale "Mas… Eu aceito sua proposta."

    Ale "Talvez seja bom eu me distrair um pouco."

    "Com isso, eu decidi levar ela para a rua central da cidade. Onde possamos fazer alguma coisa."

    stop music fadeout 2.0

    jump Alexandra_Dia5_Rua
    with fade

label Alexandra_Dia5_Rua:

    scene bg patio
    with fade

    play music "audio/cute_bossa_nova.ogg"

    show alexandra neutral at center with dissolve:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5

    Ren "Bem… Aqui estamos nós, Alexandra. Tem algo que você gostaria de fazer?"

    show alexandra neutral at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Ale "Eu não conheço muito bem por aqui. Então vou deixar você me guiar."

    "Ugh… Eu realmente não sei onde uma menina como Alexandra gostaria de ir."

    "Ela é muito… De alta classe- uma realidade completamente diferente da minha!"

    "Mas essa cidade é tão pequena que não tenho muita opção."

    show alexandra neutral at center:
        matrixcolor TintMatrix("#fff")
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    Ren "Você está com fome? Que tal irmos para a cafeteria daqui para comermos e nos acalmar um pouco?"

    show alexandra neutral at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Ale "Eu aceito. Vamos lá."

    jump Alexandra_Dia5_Cafeteria
    with fade

label Alexandra_Dia5_Cafeteria:

    scene bg cafe
    with fade

    show alexandra neutral at center with dissolve:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5

    "Chegamos na cafeteria e sentamos em uma mesa."

    "Não posso negar que Alexandra realmente se destaca nesse ambiente."

    "Seu jeito de se vestir e portar são muito diferentes da maioria. Até numa simples cafeteria assim ela exala elegância."

    Ren "O que você vai pedir, Alexandra?"

    show alexandra neutral at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Ale "No momento apenas uma xícara de chá preto mesmo."

    Ale "E você? Pode pedir o que quiser, fica por minha conta."

    show alexandra neutral at center:
        matrixcolor TintMatrix("#fff")
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    Ren "N-Não precisa!"

    show alexandra blush at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Ale "Por favor, eu insisto! É meu agradecimento por me levar aqui."

    Ale "Você podia ter só me deixado na sala de música…"

    Ale "Mas decidiu ver se eu estava bem."

    "Novamente, ela demonstra um lado inesperadamente fofo. Fico até sem jeito!"

    #[os pedidos chegam]

    jump Alexandra_Dia5_Cafeteria_PT2
    with fade

label Alexandra_Dia5_Cafeteria_PT2:

    scene bg cafe
    with fade

    show alexandra neutral at center with dissolve:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5

    "Os pedidos chegam"

    "Alexandra calmamente bebe seu chá."

    "Enquanto isso, a gente joga um pouco de conversa fora. Nada relacionado ao centro e ao festival."

    "Fiquei contando das minhas histórias de faculdade e histórias de infância com meu Tio Astolfo."

    "Em troca, ela também falou de vários momentos do meu Tio no centro comunitário. Fico feliz em saber que ele não mudou com todos esses anos."

    "Alexandra sorriu várias vezes durante nossa conversa. Isso me deu um alívio enorme em meu coração…"

    show alexandra neutral at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Ale "Esse chá…"

    show alexandra neutral at center:
        matrixcolor TintMatrix("#fff")
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    Ren "O que foi?"

    show alexandra neutral at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Ale "Esse chá não é muito bom… Essas folhas de chá preto claramente são de baixa qualidade."

    Ale "O aroma e o sabor não são muito fortes."

    Ale "Porém..."

    show alexandra happy at center:
        matrixcolor TintMatrix("#fff")
        yalign 1.0
        zoom 0.5

    Ale "Tomar chá com alguém, faz o sabor de um chá barato ficar muito mais agradável."

    Ale "Até melhor que os chás importados de minha residência."

    "Um sorriso bem calmo se abre em seu rosto, enquanto ela olha o fundo da sua xícara de chá."

    show alexandra neutral at center:
        matrixcolor TintMatrix("#fff")
        yalign 1.0
        zoom 0.5

    Ale "Ren, você vai terminar de comer esse pedaço de bolo?"

    "Ah. Fiquei tão distraído ouvindo ela conversar que me esqueci de continuar comendo."

    show alexandra neutral at center:
        matrixcolor TintMatrix("#fff")
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    Ren "Eu iria. Mas porquê? Você quer para você?"

    show alexandra blush at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Ale "Não! Era só para saber!"

    Ale "Seria rude da minha parte comer o que você está comendo."

    show alexandra blush at center:
        matrixcolor TintMatrix("#fff")
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    Ren "Hahaha. Tudo bem, Alexandra."

    Ren "Pode ficar com o pedaço."

    "Eu empurro o pedaço para ela. E ela dá uma garfada generosa no bolo."

    Ren "Me diga, Alexandra. Você gosta de doces?"

    show alexandra happy at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Ale "Eu gosto sim!"

    Ale "..."

    show alexandra blush at center:
        matrixcolor TintMatrix("#fff")
        yalign 1.0
        zoom 0.5

    Ale "M-Mas não me confunda com aquela gulosa da Priscila!! Toda a minha dieta é balanceada, em quantidades certas e–"

    Ale "Ei!! Do que você está rindo?!"

    show alexandra blush at center:
        matrixcolor TintMatrix("#fff")
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    Ren "Pffftt- Não é nada- hahaha."

    Ren "Apenas fico feliz de ver que você voltou ao normal."

    show alexandra blush at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Ale "Hmpf… Idiota."

    jump Alexandra_Dia5_Floricultura
    with fade

label Alexandra_Dia5_Floricultura:

    scene bg patio
    with fade

    show alexandra neutral at center with dissolve:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5

    "Por aqui ser uma cidade pequena, não há muitos lugares para ir."

    "Acho que me acostumei com a cidade grande."

    "Então só estamos andando um pouco pela rua, debaixo do sol."

    show alexandra neutral at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Ale "Ah. Podemos parar ali um pouco?"

    "Ela aponta para uma loja de flores. É pequena, mas bem arrumadinha."

    Ale "Está na hora de eu ver umas novas flores para o meu quarto. As que tenho, já estão morrendo…"

    show alexandra neutral at center:
        matrixcolor TintMatrix("#fff")
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    Ren "Sem problemas, Alexandra. Vamos lá!"

    jump Alexandra_Dia5_Floricultura_PT2
    with fade

label Alexandra_Dia5_Floricultura_PT2:

    scene bg patio
    with fade

    show alexandra neutral at left with dissolve:
        matrixcolor TintMatrix("#777")
        xalign 0.1
        yalign 1.0
        zoom 0.5

    #Som de entrar em loja

    "Entramos na loja de flores"

    Ren "Wow- Aqui é bem bonito mesmo."

    Ren "..."

    Ren "Espera..."

    #A wild Johnny appeared

    show johnny neutro1 at right with dissolve:
        xalign 0.9
        yalign 1.0
        zoom 0.5
        matrixcolor TintMatrix("#777")

    Ren "O que você está fazendo aqui!?!?"

    "Tomo um susto com uma aparência que não combina nem um pouco com esse lugar delicado."

    "Aqui está Johnny, usando um avental florido."

    show alexandra happy at left:
        matrixcolor TintMatrix("#777")
        xalign 0.1
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Ale "O Johnny nunca te contou? Ele trabalha aqui."

    "Alexandra parece estar se divertindo ao ver o segredo de Johnny exposto dessa forma."

    show alexandra happy at left:
        matrixcolor TintMatrix("#fff")
        xalign 0.1
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    show johnny bravo1 at right:
        matrixcolor TintMatrix("#777")
        xalign 0.9
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Joh "Sinceramente eu acho que você só vem aqui pra me provocar"

    show johnny bravo1 at left:
        matrixcolor TintMatrix("#fff")
        xalign 0.9
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    Ren "Eu sinto que eu deveria tirar uma foto."

    show johnny bravo1 at right:
        matrixcolor TintMatrix("#777")
        xalign 0.9
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Joh "Se você preza pela sua vida, eu sugiro que você NÃO faça isso!"

    show johnny bravo1 at left:
        matrixcolor TintMatrix("#fff")
        xalign 0.9
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    Ren "Tudo bem hahahahaha. Eu imagino que o Raul vai adorar vir aqui para tirar algumas."

    show johnny neutro1 at right:
        matrixcolor TintMatrix("#777")
        xalign 0.9
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Joh "*suspiro* Enfim, bem vindos à 'Floricultura da Cida'. No que posso ajudar?"

    Joh "Imagino que a Alexandra veio buscar a encomenda de sempre."

    show johnny neutro1 at left:
        matrixcolor TintMatrix("#fff")
        xalign 0.9
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    show alexandra neutral at left:
        matrixcolor TintMatrix("#777")
        xalign 0.1
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Ale "Isso mesmo. Me veja um novo buquê de cravos cor de rosa, por favor."

    "Enquanto isso, Johnny começa a separar as melhores flores que encontra."

    show alexandra neutral at left:
        matrixcolor TintMatrix("#fff")
        xalign 0.1
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    Ren "Mas, de verdade, Johnny, eu não esperava te ver aqui. Posso saber o porquê você trabalha aqui? Apenas curiosidade-"

    show alexandra neutral at left:
        matrixcolor TintMatrix("#777")
        xalign 0.1
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Ale "Não é muita novidade para quem vive na cidade. É um negócio de família, certo?"

    show alexandra neutral at left:
        matrixcolor TintMatrix("#fff")
        xalign 0.1
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    show johnny neutro1 at right:
        matrixcolor TintMatrix("#777")
        xalign 0.9
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Joh "Sim. Estamos abertos fazem uns quarenta anos"

    show johnny neutro1 at left:
        matrixcolor TintMatrix("#fff")
        xalign 0.9
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    Ren "Que legal! Pode me contar um pouco mais? Seria uma boa adição para o meu trabalho de faculdade!"

    show alexandra happy 2 at left:
        matrixcolor TintMatrix("#777")
        xalign 0.1
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Ale "Vamos lá, Johnny. Vai ser uma boa oportunidade para mostrar um lado menos bruto seu. Hahaha."

    "Ela realmente gosta de provocar o Johnny…"

    show alexandra neutral at left:
        matrixcolor TintMatrix("#fff")
        xalign 0.1
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    show johnny neutro1 at right:
        matrixcolor TintMatrix("#777")
        xalign 0.9
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Joh "Claro. Eu adoraria responder qualquer dúvida que vocês tivere-…"

    show johnny neutro1 at left:
        matrixcolor TintMatrix("#fff")
        xalign 0.9
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    "???" "Johnny! Com quem você está conversando meu neto?"

    show johnny bravo1 at right:
        matrixcolor TintMatrix("#777")
        xalign 0.9
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Joh "São alguns clientes com dúvidas, vó. Pode deixar que eu tô resolvendo aqui"

    show johnny bravo1 at left:
        matrixcolor TintMatrix("#fff")
        xalign 0.9
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    show alexandra happy at left:
        matrixcolor TintMatrix("#777")
        xalign 0.1
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Ale "Boa tarde, Aparecida!"

    show alexandra happy at left:
        matrixcolor TintMatrix("#fff")
        xalign 0.1
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    Cida "Alexandra? Ohohoho já falei que pode me chamar de Cida, minha querida. Sua encomenda está quase pronta!"

    show alexandra happy at left:
        matrixcolor TintMatrix("#777")
        xalign 0.1
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Ale "Muito obrigada como sempre, Aparec— Quis dizer, Dona Cida!"

    "A avó do Johnny entrega para ela um lindo buquê de cravos."

    Ale "Bem… Já está ficando tarde e logo a loja vai fechar. Muito obrigado por tudo Dona Cida, Johnny."

    "Eu ainda queria perguntar ao Johnny mais sobre essa loja… Talvez eu ainda tenha outra oportunidade."

    jump Alexandra_Dia5_Rua2
    with fade

label Alexandra_Dia5_Rua2:

    scene bg patio
    with fade

    stop music fadeout 2.0

    show alexandra neutral at center with dissolve:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5

    Ren "Essa loja está aqui faz muito tempo, não é?"

    show alexandra neutral at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Ale "Sim. Meus pais iam nessa loja."

    play music "audio/home.ogg"

    Ale "Mas você sabe, essa loja só vai continuar aberta se Johnny decidir continuar o legado dela."

    Ale "Aparecida já tem uma certa idade. Quando ela se for, ninguém sabe qual vai ser o destino dessa loja."

    show alexandra sad at center:
        matrixcolor TintMatrix("#fff")
        yalign 1.0
        zoom 0.5

    Ale "Ela pode fechar e cair no esquecimento…"

    Ale "A não ser que tenha algo para deixar a memória viva."

    Ale "Afinal, nós nos lembramos de lugares, mas lugares não lembram de nós."

    "Essa conversa melancólica vinda de uma simples pergunta me pega de surpresa. Ela fala isso enquanto encara seu buquê de cravos rosas."

    show alexandra sad at center:
        matrixcolor TintMatrix("#fff")
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    Ren "N-Não sei muito o que dizer. Talvez porque eu moro na cidade grande, mudanças acontecem muito rápido e o tempo todo."

    Ren "Mas imagino que seja diferente para uma cidade pequena como essa."

    "'Nós nos lembramos de lugares, mas lugares não lembram de nós.'"

    "Essa frase ecoa em minha cabeça. Talvez seja verdade."

    "Aliás, eu passei a infância nessa cidade, mas literalmente ninguém daqui me conhece."

    "Única pessoa que me conhecia, é Dona Cida, por conta do meu Tio Astolfo."

    Ren "Talvez seja por isso que todo mundo se afetou com o anúncio do fechamento do centro."

    Ren "Muitas memórias, muitas vozes de pessoas vão ser esquecidas."

    Ren "Porém… É por isso que amo minha carreira!"

    Ren "Com jornalismo, consigo dar vozes a essas pessoas e histórias esquecidas."

    Ren "E fazer com que sua memória passe adiante."

    show alexandra happy at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Ale "Hahaha… É bom saber que ainda existem pessoas que pensam como você."

    show alexandra happy at center:
        matrixcolor TintMatrix("#fff")
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    Ren "Assim eu fico meio sem graça, haha."

    Ren "Bem… Já que temos um tempinho antes de voltar ao centro. Quero te levar num lugar que eu ia muito quando criança! Você topa?"

    show alexandra happy at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Ale "Vamos lá."

    jump Alexandra_Dia5_Rua3
    with fade

label Alexandra_Dia5_Rua3:

    scene bg patio
    with fade

    Ren "O pôr do sol aqui é muito bonito, não é?"

    Ren "Quando criança eu gostava de descer esse morro com um pedaço de papelão."

    Ren "Até que um dia eu caí pra fora e me ralei todo, hahahaha."

    show alexandra happy 2 at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Ale "Haha. Meus pais nunca iam deixar eu fazer uma brincadeira dessas."

    "A menção aos pais dela faz o clima ficar um pouco tenso."

    "Me lembro da situação de mais cedo e fico preocupado novamente."

    show alexandra happy at center:
        matrixcolor TintMatrix("#fff")
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    Ren "Aliás… Desculpa te perguntar mas… Seus machucados já estão melhores?"

    Ren "Qualquer coisa podemos olhar o kit de tratamento do centro."

    show alexandra happy at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Ale "Ah, sim… Não está doendo mais. Obrigada por perguntar."

    "A gente fica uns momentos em silêncio."

    "Apenas olhando o sol se pôr… Pintando todo o nosso cenário de laranja."

    "…"

    show alexandra happy at center:
        matrixcolor TintMatrix("#fff")
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    Ren "Alexandra, posso te perguntar uma coisa?"

    show alexandra blush at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Ale "Ah- Desculpa, me distraí um pouco. Pode sim."

    show alexandra neutral at center:
        matrixcolor TintMatrix("#fff")
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    Ren "Se você dizia que era melhor aceitar o fechamento do centro, porque está se esforçando tanto para contribuir para o festival?"

    Ren "É algo que apenas não consegui parar de pensar. Eu não acho que alguém que não se importa, iria tão longe assim."

    "Ao menos não a ponto de aturar abusos dos pais para isso."

    show alexandra neutral 2 at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Ale "*suspiro* Você até que é bem perceptível às vezes, não é?"

    Ale "Desde sempre, eu tive que ser perfeita… Não foi algo que escolhi, mas sim que foi imposto a mim."

    Ale "Mas isso não era um problema. É apenas meu dever como herdeira da minha família. Não posso desgraçar o nosso nome."

    Ale "E tudo bem aturar isso, pois eu tenho a música do meu lado."

    show alexandra sad at center:
        matrixcolor TintMatrix("#fff")
        yalign 1.0
        zoom 0.5

    Ale "Música sempre me fez feliz, não importa onde eu tenha que tocar, seja em casa, na escola, no centro, em concertos. Sempre vou dar o meu melhor nisso."

    Ale "Porque mesmo que todas as coisas sejam efêmeras e vão embora um dia, música é o que sempre estará comigo."

    "Suas palavras são um pouco complexas para eu entender o que ela quer dizer… Mas ela fala isso do coração."

    "Deve ser a primeira vez que estou vendo ela sem sua máscara de princesa do gelo."

    "Eu queria entender ela, ouvir ela falar, não como um jornalista mas sim… Como um amigo."

    show alexandra sad at center:
        matrixcolor TintMatrix("#fff")
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    Ren "Será que você poderia elaborar um pouco mais nisso?"

    show alexandra sad at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Ale "Por conta de carregar o nome de minha família, eu nunca consegui ser próxima de ninguém… Exceto, uma única pessoa."

    Ale "Ela era a única pessoa que me via como 'Alexandra' e quem eu pude ser eu ao redor. Sem me importar com família, aparência, impressões."

    Ale "Todo momento que eu tive com ela… Eu pude genuinamente sorrir."

    Ale "Foram dias divertidos como jóias preciosas… Até que…"

    "Sua voz quebra em sua última frase."

    show alexandra cry at center:
        matrixcolor TintMatrix("#fff")
        yalign 1.0
        zoom 0.5

    Ale "Sua saúde era muito frágil, mas isso nunca a impediu de se divertir e de aproveitar os pequenos prazeres da vida."

    Ale "Eu, que sempre tive tudo, aprendi muito com ela."

    Ale "M-Mesmo quando ela tossia sangue, ou desmaiava, e-ela ainda vinha brincar comigo."

    Ale "Eu talvez no fundo soubesse que isso ia ter um fim, mas não quis acreditar."

    Ale "Quis acreditar que ela ia se recuperar, nem que fosse um milagre."

    Ale "Mas milagres não existem… E eventualmente. Ela se foi."

    "Lágrimas caem em seu rosto, e a voz dela se estremece cada vez mais."

    "Me sinto um pouco mal de ter feito ela lembrar de coisas tão dolorosas."

    "Mas também, sinto que finalmente estou entendendo ela."

    Ale "Após isso, eu só conseguia pensar no quanto eu queria nunca tê-la conhecido."

    Ale "Toda dor que eu senti de perder ela, eu sei que apenas senti porque eu me apeguei a nossas memórias. Inocentemente querendo que tudo aquilo durasse para sempre."

    Ale "Mas nada é eterno, tudo é efêmero."

    Ale "Por isso, eu não gosto de me aproximar demais dos outros, ou me apegar a lugares. Tudo vem sempre pra frente, e minha vida vai andando."

    Ale "Está tudo bem para mim, contanto que eu tenha música."

    Ale "Você não entende, mas a música é minha vida, e o único motivo que eu continuo."

    Ale "Enquanto tudo se for, a música ainda estará comigo."

    Ale "Ou ao menos era o que eu pensava…"

    show alexandra cry at center:
        matrixcolor TintMatrix("#fff")
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    Ren "Alexandra… Você…"

    "Ficamos um minuto em silêncio."

    "O vento faz seus cabelos esvoaçarem, e as flores em sua mão também."

    show alexandra sad at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Ale "Esses últimos dias no centro… Depois de muito tempo, consegui conversar com pessoas mais a fundo."

    Ale "Conhecer elas, entender as diferenças… Johnny, Priscila, Raul, Você."

    Ale "E-Eu me diverti… Realmente me diverti."

    Ale "Mas foi assim que eu percebi, que se o centro fechar eu vou perder toda conexão com todo mundo aqui."

    Ale "Quer dizer. Esse tempo todo eu agi distante. Não os culpo eles me odiarem, ou não quiserem mais me ver, haha."

    show alexandra sad at center:
        matrixcolor TintMatrix("#fff")
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    Ren "Isso não é verdade!"

    Ren "Nós todos aqui tivemos diferenças para trabalhar, mas por mais que vocês se desentendiam às vezes, vocês aprenderam muito um com o outro."

    Ren "Principalmente com você! Você tem um conhecimento e paixão enorme sobre o que faz."

    Ren "Você foi uma das mais dedicadas a querer salvar o centro, Alexandra."

    Ren "Por isso eu consegui ver o quão mal você ficou não conseguindo tocar hoje de manhã."

    show alexandra cry at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Ale "É. Mas agora tudo vai acabar."

    Ale "De novo eu cometi o mesmo erro do passado. Me deixei ser vulnerável e me apeguei a sentimentos calorosos de novo."

    Ale "Sou tão tola…"

    show alexandra cry at center:
        matrixcolor TintMatrix("#fff")
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    Ren "Você não é! Mas está sendo uma agora."

    Ren "Não tem nada de errado em criar conexões com os outros. E não acabou tudo ainda, Alexandra!"

    "Eu me levanto e seguro a mão dela para ela levantar também."

    Ren "Vamos voltar para o centro, ensaiar a noite toda e depois dar o melhor show que essa cidade já viu!"

    show alexandra happy at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Ale "Obrigada… Ren."

    Ale "Vou tentar o meu melhor hoje de novo, assim como sempre faço."

    "E assim retornamos pro centro. E com todo mundo lá, nós ensaiamos. Numa harmonia e sintonia da qual nunca vi antes."
