    #DIA 3 - ALEXANDRA E PRISCILA
    #INT - COPA (QUE NÃO É A DO MUNDO) DO CENTRO COMUNITÁRIO- DIA


    #[Vou ir checar a copa]
label Dia3_AlexandraPriscila:

    scene bg copa
    with fade

    "Decido ir olhar a copa do centro hoje. Talvez tenha um daqueles biscoitos sobrando-
    Se a Priscila já não devorou todos. "

    #[Ren entra na copa]

    Ale "Priscila."

    Ale "Suponho que você é a sujeita na qual é responsável por comer as trufas que eu guardei na geladeira, estou correta?"

    Pris "*Cospe o suco que estava tomando*"

    Pris "E-eu? Por que você acha que eu faria isso? "

    Pris "Hmpf! Bem feito, se você foi roubada, você deveria ter pensado duas vezes antes de colocar comida em uma geladeira pública, não achei que a mais inteligente do centro comunitário não fosse pensar nisso."

    Ale "A minha pessoa jamais recolheria comidas fora do horário! E expecto os demais de apresentarem mínima decência igualmente, entretanto aparenta-se como impossível para indivíduos patifes como você."

    "Alexandra fecha seus punhos com raiva… Tentando ainda manter sua dignidade. Embora seu rosto esteja quase vermelho."

    Ale "O centro está prestes a fechar e você, depois de ontem ter feito todo aquele drama, podia manifestar um bocado a mais de consideração com o restante dos trabalhadores do centro comunitário. Você não compreende?"

    Pris "Consideração? Pelo menos eu trato de forma amigável as outras pessoas do centro, não sou uma princesinha de gelo igual você! Desculpa se você é perfeita demais para as outras pessoas."

    "Eu já percebia que as duas não se davam bem, mas parece que é pior do que eu imaginava."

    Ale  "Seja livre para me designar de princesa, burguesa, mimada, seja o que for! Eu sequer me interesso se esse centro vai fechar, porém eu estou considerando as pessoas que se importam. Todo mundo está levando isso a sério, menos a garota de baixíssimo nível que se manifesta à minha frente. "

    "As palavras de Alexandra são cortantes. Priscila está com uma cara de quem parece que vai chorar… Além de que essa conversa está ficando fora do assunto- "

    Pris "Grrr… É-é muito fácil 'levar a sério' e ser produtivo quando você é boa em tudo e todos te mimam e endeusam por conta disso."

    #[Ren intervém na briga das duas]
    Ren "Vocês duas, parem com isso, agora! Aqui não é hora e nem lugar para brigar. Vocês não deveriam estar desenvolvendo as coisas do festival?"

    jump Dia3_AlexandraPriscila_Escolha_1
label Dia3_AlexandraPriscila_Escolha_1:
    menu:
        "Priscila… Se você realmente comeu as trufas, é bom pedir desculpas":
            jump Dia3_Alexandra_positiva_1_a
        "Alexandra…Você pegou pesado, melhor se desculpar à Priscila":
            jump Dia3_Priscila_positiva_1_b
        "Vocês duas estão erradas nessa situação, vocês deviam desculpar uma a outra":
            jump Dia3_AlexandraPriscila_neutra_1_c

label Dia3_Alexandra_positiva_1_a:
    #Escolha A
    #[Priscila… Se você realmente comeu as trufas, é bom pedir desculpas.]
    Pris "Humpf! Eu falei, todos mimam a princesa, não adianta discutir."

    Ren "Não é sobre isso, Priscila. É que por mais que seja uma geladeira comunitária, muita gente guarda a própria comida ali. "

    Ren "Além de que você não sabe quais eram as intenções da Alexandra com essas trufas. E se ela quisesse distribuir pros outros? "

    "Alexandra olha um pouco pro lado, com vergonha."

    Pris "T-tá bom, fui eu que comi, desculpa, eu não sabia que era de alguém.
    Mas desde quando ela se importa em distribuir as coisas pros outros? Ela mesma disse que não se importa se o centro comunitário fechar. Provavelmente foram doces feitos por algum mordomo dela e exclusivamente para ela."

    Ale "T-Talvez eu quisesse fazer algo generoso para as pessoas do centro já que está prestes a fechar! Mas agora você nunca vai saber, pois todas as trufas já se foram.
    Hmpf… Estou mais ofendida com você assumindo que tenho a mesma gula que você."

    Pris "Hi hi hi, eu estou vendo a princesa de gelo, sempre fria com todos, envergonhada? Fu fu fu, não precisa mentir, é claro que alguém de sua classe social come muito, você tem comida de sobra. E você queria ‘fazer algo generoso’? Então quer dizer que a situação do centro comunitário está fazendo seu gelo está derreter? Hi hi hi."

    Ale "O-Ora sua…! "

    "As palavras de Priscila são ditas com veneno nelas. Consigo ver, Alexandra saindo do sério quase- estou com medo disso dar algo muito errado. "

    Ren "Priscila! Não precisa ser assim. Independente do que você acha dela, ela tentou fazer algo generoso, não? "

    #[CONTINUAÇÃO]
    jump Cena_Dia3AlexandraPriscila_Escolha_1_continuacao

label Dia3_Priscila_positiva_1_b:
    #Escolha B
    #[Alexandra…Você pegou pesado, melhor se desculpar à Priscila.]

    Pris "Hi hi hi, então você entende do que eu estou falando!"

    Ale "…" #[Expressão brava/desacreditada]

    Ren "Ainda assim, Priscila, você pegou mesmo as trufas da Alexandra?"

    Pris "Olha, na verdade eu comi trufas que tinham na geladeira, mas eu não sabia que eram da Alexandra. Ela devia ter colocado o nome dela no pote ou algo do tipo."

    Ren "Talvez ajudasse, mas tome mais cuidado quando for assaltar a geladeira."

    Pris "Okayyy!"

    Ale "Ren, você verdadeiramente crê que um indivíduo tal como ela manterá seus prometimentos? A Priscila age de maneira semelhantemente desprezível absolutamente todos os dias, uma promessa ordinária como esta não desencadeará quaisquer renovação em suas características pessoais."

    Pris "Lá vem a burguesa com as palavras difíceis…"
    #[CONTINUAÇÃO]
    jump Cena_Dia3AlexandraPriscila_Escolha_1_continuacao

label Dia3_AlexandraPriscila_neutra_1_c:
    #Escolha C
    #[Vocês duas estão erradas nessa situação, vocês deviam desculpar uma a outra]

    Pris "…"

    Pris "Desde quando você está ouvindo tudo isso?"

    Ale "Hmpf, patético…"

    "Eu falei algo de tão errado assim!?"

    Ren "Eu só acho que vocês tem que parar de brigar!"

    Ale "Se ela não mudar a atitude dela, não vai ajudar em nada para o festival! "

    Pris "Olha quem fala!"

    #[CONTINUAÇÃO]
    jump Cena_Dia3AlexandraPriscila_Escolha_1_continuacao

label Cena_Dia3AlexandraPriscila_Escolha_1_continuacao:
    #CONTINUAÇÃO

    Ren "Vocês duas brigam demais… Precisam achar algum ponto em comum! Ou senão esse festival não vai para frente."

    Pris "Hmmm… Difícil, essa daí e eu somos como óleo e água."

    Ren "Priscila quer ajudar a salvar o centro, Alexandra quer ter um bom festival. Essas duas coisas andam juntas. Vocês já sabem o que querem apresentar pro público?"

    Pris "Hihihi… FUFUFU… HAHAHAHAHAH!! É óbvio que eu sei!"

    "A Priscila parecia saber perfeitamente o que responder. E isso me dá medo…"

    Pris "Um grupo de dançarinos coreanos lindos, charmosos, musculosos e sem camisa dançando 'Manteiga', o último lançamento do BLZ… KYAAAAAAA, O JÃO COOKIE TÁ TÃO LINDO NESSA MÚSICA!!! MWAHAHAHAHAHAHAHAHAHAHA!!"

    Ale "Essa música certamente vai agradar as pessoas mais jovens. Contudo, da mesma forma teremos bastantes pessoas de idades mais avançadas no festival.
    Diante disso, imagino que uma melodia como Chopin seja intensamente apropriada-"

    "E novamente, lá vamos nós, mesma discussão do outro dia sobre gêneros musicais.
    Eu preciso achar alguma coisa que faça elas se entenderem melhor!"

    Ren "Olha, vamos ter vários tipos de pessoas lá! Talvez vocês possam aprender um pouco mais sobre o que a outra gosta, assim poderão se entender melhor. Vamos à sala de música, uma vai apresentar sua ideia à outra."

    Pris "Ahhh… Tá bom… Chato…"

    Ale "*Suspira*, Após tamanho escândalo dessa garota, ainda terei que debater sobre gostos musicais com ela, que momento deveras menosprezável…"

    "Juntar essas duas vai ser bem difícil, mas eu preciso tentar, pelo bem do festival e do centro comunitário…"

    #INT - SALA DE MÚSICA DO CENTRO COMUNITÁRIO- DIA

    scene bg sala de musica
    with fade

    Ren "Certo, chegamos, quem quer começar?"

    Ale "Eu devo começar. Apresentarei uma melodia que vocês nunca se esquecerão."

    Pris "Ela nem me deu tempo pra falar!"

    Ren "Tá certo, sinta-se a vontade."

    "Alexandra se move calmamente até o piano presente na sala, emanando uma forte confiança. Cada um dos passos que ela dá parecem ser milimetricamente calculados com extrema precisão, como se o simples ato de andar já fizesse parte de sua performance."

    Ale "…"

    "Ela respira de forma calma e precisa, seus olhos não demonstram nenhuma emoção, sua concentração está em seu mais alto nível. Parece que ela realmente quer nos impressionar com essa música."

    "O ar transmitido por Alexandra faz até mesmo Priscila ficar em silêncio e respeitar esse momento."
    "Cada respiração, cada movimento, até os mais usuais, pareciam demonstrar uma superioridade e delicadeza inigualáveis."
    "Alexandra se senta na cadeira à frente do piano com extrema leveza, exibindo um nível de sofisticação tão alto que dá a impressão que ela pesa menos do que uma pena."

    #Algum efeito visual

    "Uma linda melodia adentra nossos ouvidos. Nos arrepiamos com tamanha perfeição em cada uma das notas passadas. As batidas de nossos corações seguem o belo ritmo da música, acalmando nossas almas. Os movimentos dos dedos de Alexandra tocando as teclas do piano eram tão delicados quanto pequenas gotas de uma leve garoa matinal tocando as pequenas poças espalhadas pela cidade."
    "Não consigo ver qual a reação da Priscila, pois não consigo tirar os olhos do piano e da pianista que estavam ali presentes."

    "Na verdade, eu nem preciso olhar para a Priscila. Eu posso sentir daqui que ela está se impressionando tanto quanto eu… Não, ela está se impressionando até mais do que eu. Alexandra está apresentando a concentração que Priscila não possui e talvez nunca possua, e a Priscila sabe disso."

    #Fecha o efeito visual


    "Alexandra terminou de tocar a melodia de uma forma bastante dramática, simplesmente impecável."

    Ren "Olho para o lado e a Priscila já está mexendo na caixa de som, provavelmente colocando sua música."

    #Pris *Se move para o centro da sala*

    Ale "Vamos ver se o tempo que ela usa para procrastinar serve pra alguma coisa."

    "Os punhos de Priscila se fecham com muita força, parece até que eles sangrariam se ela continuasse apertando. Eu nunca havia visto ela desse jeito, alguém que simplesmente não para de falar em nenhum momento está completamente quieta, deixando um clima de mistério na sala. Nós não temos ideia do que pode sair dessa apresentação: uma surpreendente performance ou um envergonhante fracasso."


    "Além disso… Eu posso estar enganado por conta da distância, mas… Aquilo são lágrimas nos olhos da Priscila?"
    "*A música começa a tocar*"


    "As batidas da música começam em um ritmo lento, as pernas de Priscila se movem levemente seguindo o ritmo das batidas."


    "As batidas param repentinamente. Eu e Alexandra ficamos confusos. Teria a caixa de som deixado de funcionar? Com o silêncio incerto presente na sala, conseguimos ouvir apenas uma respiração profunda de Priscila."
    "*Música retorna*"


    "Uma animação 3D da Priscila com rosto de Jojo dançando a dança do Fortnite ao som de Megalovania se inicia. Eu não faço ideia do que está acontecendo com a minha vida. Hmmm… Então talvez os boatos sobre o tio Astolfo ser traficante de drogas fossem reais…
    Olho para o lado e vejo a Alexandra deitada no chão chorando em posição fetal. Calma… Então não é uma ilusão!?"


    "Instantaneamente o som da música se torna altamente agitado e os movimentos de Priscila seguem a mesma onda. Seus movimentos são eletrizantes, fazendo com que a enorme animação da música fosse contagiada por mim e pela Alexandra, é como se cada passo dado por ela emanasse as ondas sonoras junto das batidas da música. Os passos de Priscila são rápidos e difíceis de acompanhar, principalmente para pessoas que não estão ligadas ao mundo da dança."


    "Para nos surpreender ainda mais, Priscila começa a cantar em coreano enquanto dança! A música é um hip hop bastante frenético, as sentenças pronunciadas velozmente atingem nossos ouvidos como um raio, embaralhando nossos sentidos. Talvez nem se entendêssemos coreano nós conseguiríamos entender o que Priscila estava falando."

    "Priscila se vira para Alexandra, olhando-a diretamente nos olhos. Mesmo que não entendamos nada do que está sendo falado na letra da canção, é perceptível que cada uma das palavras faladas são voltadas para atacar de alguma forma Alexandra."

    "Parece que a Priscila escolheu essa música propositalmente para confrontar sua rival. O olhar direto da Kpopper aliado à complexa dança e as rimas sem interrupção chegam a incomodar a garota rica. Dessa vez quem estava apertando os próprios punhos era a Alexandra."

    Ale "Como ela… Sem nem mesmo se esforçar… Ela apenas dorme e come… Então como…?"

    "Ela tem uma boa pergunta… Como Priscila teria tamanha habilidade em dançar e cantar se ela está o tempo todo dormindo fechada na sala de jogos ou tentando roubar comida da geladeira da copa?"

    "Espera… A sala de jogos… Será…?"

    #*Finaliza a dança em um pose dramática e respira ofegante*
    Pris "Huff… Huff…"

    Ale "…"

    Ale "S-sua…"

    Pris "Grrr…"

    "Ah não… De novo não…"

    Ale "De que maneira você é capaz de ter tamanho talento e não usar esse talento para o festival!?"

    Pris "Queeeee!? E nem chego perto das suas habilidades, menina prodígio! Como você pode chamar o que eu tenho de talento!? Você está em um nível completamente além do meu!"

    Ale "COMO OUSA!? AINDA TENHO MUITO O QUE APRENDER!
    SEUS MOVIMENTOS…! A VELOCIDADE DE APLICAÇÃO DAS RIMAS EM UMA LÍNGUA COMPLETAMENTE DISTINTA DA NOSSA… É ALGO QUE EU JAMAIS PODERIA REALIZAR!"

    Pris "HÃÃÃ!? GRRRR! AS MINHAS HABILIDADES NÃO CHEGAM NEM PERTO DAS SUAS!!! A FORMA COMO VOCÊ TOCA O PIANO E ATÉ A FORMA COMO VOCÊ ANDA E SE SENTA SÃO PERFEITAS! É TUDO MUITO DRAMÁTICO! EU TE INVEJO, PRINCESA DE GELO!"

    Pris "GRRRR!!!"

    Ale "HUUUMMMMM…!!!"

    "Calma… As duas estão…"

    "Se elogiando?"

    Ren "Ah… Pessoal…"

    "Alexandra e Priscila" "O QUE!?"

    Ren "Vocês perceberam que vocês estão se elogiando ao invés de se ofender?"

    Pris "Hã?"

    Ale "Hm?"

    "As duas começaram a se encarar por alguns segundos."

    Pris "…"

    Ale "…"

    Pris "…"

    Ale "…"

    Pris "…"

    Ale "…"

    Pris "Piff…"

    Ale "Hm, hm…"

    Pris "HAHAHAHAHAHAHAHAHA!!"

    Ale "Hahahaha!"

    Pris "HAHAHAHAHAHAHAHAHAHAHAHAHA!!! AHHHHH, EU NÃO CONSIGO PARAR DE RIR! EU VOU CHORAR!! HAHAHAHAHAH!!"

    Ale "Pare! Está me contagiando!! Hahahahaha!!!"


    "Eu queria rir também, mas eu acho que eu estava tão tenso pela dúvida em relação a esse desfecho que eu só consigo suspirar de alívio…"

    Ale "Como você sente inveja de mim? Você tem um enorme talento que eu não possuo nem de longe."

    Pris "É claro que eu sinto! Eu sempre quis ser igual a você! Você é perfeita! Você é boa em tudo o que faz, além de também ser super popular! Talvez… As pessoas não me pressionariam tanto se eu fosse como você…"

    Pris "E provavelmente você é a única que consegue realmente namorar o Jão Cookie!"

    Ale "É evidente que não! Você tem qualidades que eu certamente não tenho e isso é deveras admirável."

    Ale "Eu… Também queria ser um pouco como você, alguém amigável com o próximo. Mas eu, apesar de ser perfeita como você se refere à minha pessoa, não tenho ideia de como fazer isso."

    Pris "Hi hi hi! Relaxa! Eu te ajudo com isso!"

    Ale "Me sinto lisonjeada. E eu estarei disposta a te ajudar a se tornar melhor em suas outras habilidades. Talvez até para conquistar o tal do Jão Cookie."

    "Parece que a situação finalmente se acalmou… Fico muito feliz que as duas finalmente tenham se dado bem. Agora deu uma sensação de missão cumprida."

    "Inclusive, tenho que tirar uma dúvida"

    Ren "Priscila, desde quando você é fluente em coreano?"

    Pris "Eu? Fluente?"

    Pris "Haha! Nhé!"

    Pris "Eu não sei nada de coreano, eu só decorei as letras das músicas de tanto ouvir elas e só repito o que eles falam na hora de cantar! Hahaha!"

    Ren "Por que eu não estou surpreso…? Haha…"

    return
    #Ale *Ri delicadamente*

    #[FIM DA CENA]
