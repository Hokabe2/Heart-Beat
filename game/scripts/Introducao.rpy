label Introducao:
        play sound "audio/phone_vibration.mp3"

        python:
            ShowText("","{sc=4}BZZZZ! BZZZZ! BZZZZ!{/sc}")

        Ren "Quem será a essa hora?!"

        stop sound fadeout 3.0

        "Vejo na tela do meu celular um email."
        "Assunto: Centro Comunitário prestes a ser fechado! Urgente"
        "Caro Ren,
        Vi que você postou no fórum de jornalistas que estava a procura de uma história para seu trabalho de final de semestre. Acredito que tenho uma história quente pra você. Segue em anexo algumas informações para uma possível matéria
        Espero que tenha ajudado."


        Ren "Uma resposta do fórum de jornalistas independentes? Eu postei um pedido de ajuda lá faz uns três dias, e até agora nenhuma das histórias que me passaram me parecia interessante."
        "Sinceramente, é meio difícil escrever uma matéria interessante sobre um carro que fala frases de efeito. Depois que ele repete a mesma frase pela 10ª vez, começa a ficar meio irritante."
        "Ok… Um centro comunitário… Relevância histórica, bom… No meio do nada, tá… Fechado por falta de visitantes… Eu posso trabalhar com isso, já que eu estou atrasado com esse trabalho."
        "E ainda por cima é na cidade do meu tio Astolfo! Posso aproveitar e visitar ele, faz um bom tempo que a gente não se vê. Vou mandar mensagem pra ele perguntando se posso ficar com ele enquanto escrevo a matéria."
        "Estranho. O e-mail não foi assinado e não dá pra saber quem mandou pelo apelido… Minha primeira fonte anônima! Isso vai ser interessante, ou um desastre. Mas é melhor do que o carro que fala. Vou comprar a passagem pra amanhã."

        jump Cena_Introducao_email
        with fade
        # Introdução
label Cena_Introducao_email:

        scene bg cafe
        with fade

        play music "audio/blithe_part_b.ogg"

        "Onde está o tio Astolfo? Ele me mandou mensagem a menos de cinco minutos atrás falando pra me encontrar aqui…"

        "Será que ele se perdeu?... Ele já se perdeu num parque aquático e a gente ficou procurando ele por duas horas pra encontrar ele tentando trazer um monte de patos pra piscina de ondas…"

        Ren "Pera… que som é esse?"

        "???" "TIIIIIIIIIIOOOOOOOOOOOOOOO AAASSSSSSSSSSSSSSSSTOOOOOOOOOLLLLLLLLFFFFFFFFOOOOOOOOOO A CAMIIIIIIIINHOOOOOOOOOOOOOOOOOOO"

        Ren "O senhor sempre foi ‘único’ nas suas entradas Tio Astolfo"

        Tio_Astolfo "Ora, uma boa entrada sempre precede uma conversa fenomenal"

        Tio_Astolfo "Então meu sobrinho, fiquei sabendo que você está aqui para fazer um trabalho acadêmico"

        Ren "Ah sim! Tenho uma matéria pra entregar pro final do mês e…"

        Tio_Astolfo "Sobre o que vai ser esta matéria? Será sobre seu adorável tio?"


        "Uma matéria sobre o Tio Astolfo seria interessante, porém acho difícil que os professores aceitarem… Talvez eu faça algo sobre as histórias dele em um próximo semestre"

        Ren "Na verdade é sobre o centro comunitário local. Recebi um e-mail outro dia falando sobre o lugar, então eu vim pesquisar"

        Tio_Astolfo "O Centro Comunitário? Olha mas que sorte, pelos últimos vinte anos eu fui responsável pelo centro. Venha, vou te contar sobre isso tudo enquanto vamos para lá"

        Tio_Astolfo "PARA O ASTOLFO MÓVEL!!!"

        "Pelo amor de Deus, aquela Kombi velha de novo não… A última vez que eu entrei lá o Tio Astolfo quase jogou a gente em um barranco tentando se livrar de uma mosca…"

        "O Tio Astolfo corre de maneira cômica em direção à sua Kombi cheia de decalques enquanto eu sigo lentamente e decepcionado."

        play sound "audio/mixkit-short-car-ignition-1541.ogg"

        "Entramos no carro e nos movemos rumo ao centro comunitário."

        #Eles vão para o centro comunitário

        stop music fadeout 1.0

        jump Cena_Introducao_personagens
        with fade

label Cena_Introducao_personagens:

        scene bg exterior
        with fade

        play music "audio/cute_bossa_nova.ogg" fadeout 1.0

        if (talkToRaul1 == True) and (talkToPriscila1 == True) and (talkToAlexandra1 == True) and (talkToJohnny1 == True):
            Ren "Estou exausto, já conheci todo o centro comunitário. Acho que vou para casa."
            jump Cena_Quarto_dia1
            with fade
        else:

            if firstTimeInCenter == False:

                play sound "audio/mixkit-old-car-arriving-1536.ogg"

                Ren "Chegamos."

                Ren "O Tio Astolfo disse que tinha algumas questões urgentes para resolver, então ele me deixou no pátio do centro comunitário."

                Ren "Hmmm... Então esse é o centro comunitário..."

                Ren "É relativamente pequeno se for comparar com outros centros comunitários, mas parece bem organizado."

                Ren "Bom, eu devia dar uma explorada aqui."

                Ren "Preciso decidir para onde eu vou."

                $firstTimeInCenter = True

            else:

                Ren "Preciso decidir para onde eu vou agora."

        #Menu de decisões para conhecer os personagens
        menu:
            "Biblioteca":
                if talkToRaul1 == False:
                    jump Cena_Introducao_Raul
                    with fade
                else:
                    Ren "Eu já fui na biblioteca."
                    jump Cena_Introducao_personagens
                    with fade
            "Copa":
                if talkToPriscila1 == False:
                    stop music fadeout 1.0
                    jump Cena_Introducao_Priscila
                    with fade
                else:
                    Ren "Eu já fui na copa."
                    jump Cena_Introducao_personagens
                    with fade
            "Sala de música":
                if talkToAlexandra1 == False:
                    stop music fadeout 1.0
                    jump Cena_Introducao_Alexandra
                    with fade
                else:
                    Ren "Eu já fui na sala de música."
                    jump Cena_Introducao_personagens
                    with fade
            "Pátio":
                if talkToJohnny1 == False:
                    stop music fadeout 1.0
                    jump Cena_Introducao_Johnny
                    with fade
                else:
                    Ren "Eu já fui no pátio."
                    jump Cena_Introducao_personagens
                    with fade

label Cena_Introducao_Raul:
        scene bg recep
        with fade

        Ren "Decidi ir para a biblioteca."

        Ren "Havia três prateleiras com diversos gibis, livros infantis e infantojuvenis."

        Ren "Fui vendo e folheando alguns dos catálogos."

        Ren "Eu costumava ler muitos gibis quando eu era criança. Sempre tinha um desses quando ia ao consultório médico fazer um daqueles exames que demoram uma hora para chegar a sua vez para uns 15 minutos de exame de verdade."

        Ren "Acho que quem lê muito é uma pessoa culta."

        Ren "Não que eu esteja me gabando… Ok, estou me gabando."

        Ren "Foi aí que ouvi alguém do outro lado da biblioteca."

        "(???)"  "Lembre de devolver antes de ir para casa."

        "(Criança aleatória)"  "Tá bom, Raul."

        Ren "Uma menina passou correndo por mim."

        Raul "Olá… Está interessado em um gibi?"

        Ren "Ele tem a mesma altura que eu, provavelmente era um dos jovens do centro, mas tinha cara de ser mais velho por causa da barba."

        Raul  "Espera, você é o tal do Ren, o sobrinho do Astolfo? Sou o Raul, geralmente tô por aqui cuidando do vai e vem da biblioteca."

        Ren  "Sim, sou eu mesmo. Como soube?"

        Raul  "Matemática básica, cara! É só somar dois mais dois. Não tem muitos jovens da nossa idade por aqui, a maioria acaba saindo por causa de trabalho ou por estudos, e, além disso, o tio Astolfo nos avisou antecipadamente da sua chegada."

        Ren  "Ah! Sério? Ele costuma falar bastante de mim para outras pessoas."

        Ren "Digo isso um pouco envergonhado, porque às vezes ele costuma exagerar demais nas minhas poucas qualidades."

        Ren  "O que ele disse?"

        Raul  "Bem… Foram muitas… Deixe eu ver: que você está estudando jornalismo e vai ajudar no nosso projeto, que você quase se afogou numa piscina quando tinha uns 5 anos e que curte tudo quanto é tipo de música."

        Ren  "Minha playlist é bem caótica, na verdade não tenho nenhum gosto específico. Às vezes tenho fases diferentes que eu fico obcecado com um gênero e depois mudo para outro."

        Raul  "Queria ser mais bicho solto, tô precisando variar no meu repertório."

        "Ele fala de maneira relaxada e descontraída, já senti que ia me dar bem com ele. Talvez devesse começar a minha pesquisa de campo por ele, ou só deixar a conversa fluir."

        jump Cena_Introducao_Raul_Escolha_1

        #Escolha 1
label Cena_Introducao_Raul_Escolha_1:
        menu:
            "Você frequenta o centro comunitário há quanto tempo?":
                call Raul_positiva_1_a
            "Eu acabei entrando no projeto por causa de um trabalho da faculdade":
                call Raul_neutra_1_b
label Cena_Introducao_Raul_Escolha_1_continuacao:

        Raul "Temos um grupo no Whatsapp dos Jovens do Centro, por enquanto não pensamos num nome melhor para o grupo, se quiser já adiciono agora o seu contato."

        "Passei o meu contato para ele e sorrimos juntos, definitivamente gostei da vibe desse cara."

        $ talkToRaul1 = True

        jump Cena_Introducao_personagens
        with fade
label Raul_positiva_1_a:
        $ pointsRaul+= 1

        Raul  "Mais ou menos uns dez anos e pouco."

        Raul  "Mas tem gente que tá aqui desde que se lembram como ser humano."

        Ren  "Aqui deve ser um lugar bem especial para vocês."

        Raul  "Alguns ficam no contraturno escolar porque não tem como almoçar em casa ou porque os pais estão no trabalho."

        Raul  "Aqui pelo menos servem refeições e salas com tudo quanto é tipo de coisa."

        Ren "Ele sorri como se estivesse orgulhoso de fazer parte daquele lugar. Faz sentido, e respeito muito, não tinha ideia de como aquele lugar era importante para as pessoas do bairro."

        jump Cena_Introducao_Raul_Escolha_1_continuacao
        return
label Raul_neutra_1_b:
        Raul "Faz sentido. Vi numa reportagem que as faculdades pedem horas complementares de trabalho voluntário pros alunos de alguns cursos."

        Ren "Não é nada disso, é um trabalho que pediram."

        Raul  "É o seu TCC?"

        Ren "Não, é só um trabalho semestral."

        Raul "Então você deve tá fazendo com um grupo esse trabalho! Seus colegas também vão estar por aqui?"

        Ren "…"

        Raul "Não… é?"

        Ren "Sou só eu."

        Ren "Meu único amigo foi para outro grupo"

        Raul "Oh…"

        Ren "Ficou um silêncio constrangedor entre nós dois."

        Raul "Tenso isso daí. Entendo que formar amizades pode ser complicado, mas aqui você vai conhecer uma galera muito foda. "

        jump Cena_Introducao_Raul_Escolha_1_continuacao
        return

label Cena_Introducao_Priscila:
    scene bg copa
    with fade

    play music "audio/1_Menu_Master.mp3" volume 0.7

    "Resolvi dar uma olhada na cozinha primeiro."

    "Ia ser uma péssima primeira impressão se me pegarem assaltando a geladeira no meu primeiro dia de trabalho de campo."

    "E claro que eu não ia fazer isso."

    "Mas quando eu entro…"

    "Vejo que a porta da geladeira estava aberta e o alarme de temperatura da geladeira estava tocando, indicando que ela estava assim já faz um bom tempo."

    "Não sei quem esqueceria a porta da geladeira de um centro comunitário aberta, deve ser muita falta de responsabilidade."

    "Deixei meus pensamentos de lado e me aproximei para fechar o eletroeletrônico. Entrando…"

    "Quando olho para baixo, encontro uma garota agachada comendo um cookie."

    "???" "…"

    Ren "…"

    "???" "…"

    "Continuamos nos encarando em silêncio por alguns segundos devido ao choque da situação."

    show priscila neutro at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    "???" "*Chomp *Chomp… P-peua! Eu não extou cumendo nada da feladeila, voxê tá enfanado!"

    "Eu não entendi quase nada que a garota me falou, mas ela parecia bastante desesperada com o momento, como se ela estivesse fazendo algo de muito errado."

    "???" "C-calma, tá tudo bem, eu sou novo aqui no centro comunitário, estou apenas passando para conhecer haha."

    "A menina se levantava em um salto enquanto terminava de comer o cookie, dessa vez parecia um pouco mais aliviada."

    "???" "Enfão voxê não feio aqui pra me denunpiar pro tio Asfolfo? *Chomp *Chomp, Desculpa-"

    "Ela terminou rapidamente de comer seu biscoito, deixando diversos farelos caírem no chão, e logo depois chupou seus dedos que estavam sujos com chocolate."


    Pris "Hum, Hum… Me chamo Priscilla, muito prazer! Espero que possamos termos uma boa amizade e nos divertirmos muito juntos!"

    show priscila feliz at center:
        matrixcolor TintMatrix("#fff")
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    "A menina estendeu amigavelmente a mão para me cumprimentar, enquanto apresentava um grande sorriso radiante. Senti como se ela emanasse luz com essa tamanha alegria. Estendi minha mão igualmente."

    Ren "O prazer é meu, me chamo Ren, sou o sobrinho do tio Astolfo e espero a mesma coisa."

    show priscila feliz at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "Ahhh, então você é o sobrinho! Ele tinha comentado com a gente! Hi hi hi! Então, então, o que te trouxe ao centro comunitário?"

    show priscila feliz at center:
        matrixcolor TintMatrix("#fff")
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    Ren "Eu preciso fazer uma atividade da minha faculdade de jornalismo, então acabei recebendo uma proposta de pesquisar sobre o centro comunitário."

    show priscila serioisso at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "Hmmm… Faculdade? Pesquisa?... Soa bem chato… Você poderia aproveitar que está aqui para conhecer novas pessoas e relaxar, tem gente bem legal aqui! Tem o Raul, o tio Astolfo, o Johnny e… Bom, na verdade são só eles, mas são bem legais haha!"

    jump Cena_Introducao_Priscila_Escolha_1
label Cena_Introducao_Priscila_Escolha_1:
    menu:
        "Eu discordo, jornalismo às vezes pode ser cansativo, mas é algo que eu amo fazer, pretendo focar bastante na pesquisa":
            call Priscila_neutra_1_a
        "É verdade, talvez eu devesse relaxar um pouco mais de vez em quando. Socializar também é importante":
            call Priscila_positiva_1_b
label Priscila_neutra_1_a:
    #[Escolha 1 Neutra - Priscila: "Eu discordo, jornalismo às vezes pode ser cansativo, mas é algo que eu amo fazer, pretendo focar bastante na pesquisa"]

    show priscila serioisso at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "Hããã… Que chato… Acho que você não vai entrar na lista de pessoas legais… -_-"

    Ren "Ei!"

    show priscila feliz at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "Hahaha, brincadeira! Só o fato de você não ter me denunciado pro tio Astolfo já te torna uma pessoa legal, ninguém me deixa comer a vontade aqui hahaha!"

    Ren "Mas eles não estão certos por fazer isso?"

    show priscila feliz at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "Depende do ponto de vista! Aqui é um centro COMUNITÁRIO, o que significa que ele é aberto à comunidade, como eu faço parte dela então eu tecnicamente tenho o direito de comer essa comida!"

    Pris "Além disso, nem todos os alimentos aqui são comidos, o que quer dizer que eu estou evitando desperdício!"

    Ren "…"

    "Comecei a olhar para ela com um olhar de julgamento."

    show priscila serioisso at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "…"

    Ren "…"

    show priscila serioisso at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "N-não me olha com essa cara! T-tá bom, eu admito, é errado! Eu sei que é! Mas é difícil controlar a minha fome quando eu preciso aguardar até o almoço para comer apenas algumas das comidas tão gostosas que ficam dentro dessa geladeira!"

    "Bom, pelo menos ela tem algum nível de autocrítica"

    Pris "Vou ir pra sala de jogos daqui do centro comunitário, se você mudar de ideia e quiser relaxar um pouco você pode me chamar. Só não me olhe com esse olhar de desprezo."

    "Quando a Priscila se virou para ir embora, notei mais dois cookies que segurava em suas mãos, mas decidi não falar nada."

    "Parece que ela não aprendeu nada com essa situação..."

    $ talkToPriscila1 = True

    jump Cena_Introducao_personagens
    with fade
label Priscila_positiva_1_b:

    #[Escolha 2 Positiva - Priscila: "É verdade, talvez eu devesse relaxar um pouco mais de vez em quando. Socializar também é importante"]

    $ pointsPriscila+=1

    show priscila feliz at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "Hi hi hi, não é? Trabalhar é chato e cansativo, a gente deveria ir comer no Capputinho pra relaxar, tem comidas muito boas lá!"

    Pris "Ou a gente pode levar algumas comidas daqui da geladeira para comer enquanto anda! Super recomendo esses cookies e chocolates que tem guardado no fundo, são sempre muito bons! Hahaha!"

    Ren "Haha, eu agradeço o convite, mas eu ainda preciso conhecer o resto do centro comunitário e depois voltar para falar com meu tio."

    show priscila neutro at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "Humm, faz sentido. Bom, qualquer hora que você quiser relaxar um pouco você pode falar comigo! Eu sou a melhor daqui na arte de não fazer nada, ninguém nunca nem ousou me superar nisso!"

    "Isso deveria ser algo para se ter orgulho!?"

    Ren "Certo haha. Bom, então já vou indo, até mais!"

    show priscila feliz at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Pris "Até mais! Tcha-tchau!"

    "Após andar um pouco, olhei para trás e notei a geladeira aberta novamente… Mas dessa vez eu sabia o porquê."

    $ talkToPriscila1 = True

    jump Cena_Introducao_personagens
    with fade

label Cena_Introducao_Alexandra:

    scene bg sala de musica
    with fade

    play music "audio/autumn_leaves_part_a.ogg" volume 0.5

    "No piano da sala de música, há uma garota tocando de forma super concentrada. Ela aparenta ser muito elegante. Com cabelo cinza comprido que é ondulado nas pontas."

    show alexandra neutral 2 at center with dissolve:
        yalign 1.0
        zoom 0.5
        matrixcolor TintMatrix("#777")

    "Tem uma franja reta e uma trança acima da franja parecendo que há uma coroa em sua cabeça."

    "Também usa um óculos redondo dourado, uma camisa de gola branca com um laço preto e uma saia longa preta."

    "Resolvi ir olhar a sala de música. Embora eu não entenda nada sobre música, eu estava ouvindo uma bela melodia vindo do corredor."

    "Ao abrir a porta, vi uma figura de uma bela menina sentada no piano. Extremamente concentrada na melodia que estava tocando."

    "A delicadeza da música parecia que realçava sua beleza."

    "De repente ela para. E se vira para trás."

    "Deve ter notado minha presença ali."

    "A menina se levanta e me encara. Será que eu deixei ela brava?! Sua aura é extremamente forte. Quase como se fosse chefe de uma família extremamente rica… "

    Ren "A-Ah! Me desculpa, e-eu devo ter te atrapalhado. Pode continuar se quiser!"

    show alexandra neutral at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Ale "Está tudo bem. Eu estava apenas matando tempo aqui."

    show alexandra happy at center:
        matrixcolor TintMatrix("#fff")
        yalign 1.0
        zoom 0.5

    Ale "Seu rosto é novo por aqui. Qual é o seu nome?"

    show alexandra happy at center:
        matrixcolor TintMatrix("#fff")
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    "Apesar da sua aura fria, ela dá um pequeno sorriso."

    Ren "Eu sou Ren! Prazer."

    show alexandra happy at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Ale "Prazer. Eu sou Alexandra. De vez em quando venho aqui no centro para tocar música para as pessoas."

    show alexandra happy at center:
        matrixcolor TintMatrix("#fff")
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    Ren "Você é muito boa nisso. Que música era essa que você estava tocando?"

    "Eu tento criar algum tipo de conversação para quebrar o gelo. Mas a presença dela é tão forte que me deixa nervoso de qualquer forma."

    show alexandra neutral at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Ale "Chopin Nocturne op.9 No.2"

    show alexandra neutral at center:
        matrixcolor TintMatrix("#fff")
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    "É… Eu realmente não entendo nada sobre música. Mas com o jeito que ela me encara, eu sinto que tenho que dizer alguma coisa. Nem que tenha que mentir-"

    jump Cena_Introducao_Alexandra_Escolha_1
label Cena_Introducao_Alexandra_Escolha_1:
    menu:
        "E-Eu conheço!! Já escutei em algum lugar ao menos…":
            call Alexandra_neutra_1_a
        "Eu não conheço, mas era muito bonita a música!":
            call Alexandra_positiva_1_b
label Alexandra_neutra_1_a:
    #Escolha 1[Neutro] - Ren
    #"E-Eu conheço!! Já escutei em algum lugar ao menos…"

    show alexandra neutral at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Ale "Ter escutado não é muita surpresa. É bem conhecida. Mas e outras do Chopin? Como Revolutionary Étude ou Waltz?"

    "…"

    "É. Com isso eu quebro a cara. Dificilmente vou conhecer essas. "

    "Fui idiota- eu devia ter falado a verdade."

    show alexandra neutral at center:
        matrixcolor TintMatrix("#fff")
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    Ren "Eu preciso de verdade me informar mais sobre música clássica ahahaha-"

    show alexandra neutral at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Ale "Bem, eu não espero que as pessoas conheçam as músicas."

    Ale "Mas pode vir aqui para me ouvir tocar novamente. E quem sabe assim você não aprende um pouco mais?"

    "Me sinto completamente dominado aqui. Como se estivesse numa jaula com um leão que pudesse me devorar a qualquer momento–"

    show alexandra neutral at center:
        matrixcolor TintMatrix("#fff")
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    Ren "Eu com c-certeza visitarei de novo! Foi um prazer, Alexandra!"

    "Com um pequeno sorriso de volta, me retiro da sala de música."

    $ talkToAlexandra1 = True

    jump Cena_Introducao_personagens
    with fade
label Alexandra_positiva_1_b:
    #Escolha 2[Positiva] - Ren
    #"Eu não conheço, mas era muito bonita a música!"

    $ pointsAlexandra+=1

    show alexandra happy at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Ale "É. Eu não espero que as pessoas conheçam mesmo."

    "Não adianta. É extremamente difícil quebrar a partir desse gelo dela. É como se estivéssemos em planos de existência completamente diferentes."

    Ale "Mas sinta-se livre para vir me ver tocar quando eu estiver aqui. É para isso que venho aqui mesmo."

    show alexandra happy at center:
        matrixcolor TintMatrix("#fff")
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    "Ela deu um pequeno sorriso… Talvez eu tenha conseguido derreter um pouco desse gelo no fim. "

    Ren "Com certeza irei visitar mais vezes! Foi um prazer, Alexandra!"

    "Com um pequeno sorriso de volta, me retiro da sala de música."

    $ talkToAlexandra1 = True

    jump Cena_Introducao_personagens
    with fade

label Cena_Introducao_Johnny:

    scene bg patio
    with fade

    play music "audio/dramatic_boi_v3.ogg" volume 0.5

    "Em um dos bancos no pátio do centro comunitário se encontra um jovem ouvindo música"

    show johnny neutro1 at center with dissolve:
        yalign 1.0
        zoom 0.5
        matrixcolor TintMatrix("#777")

    "Ele emana uma aura bem intimidadora, enquanto observava o seu entorno. Ele usa um colete jeans rasgado, uma camiseta preta com uma estampa vermelha, suas calças são rasgadas e ele usa coturnos bem altos."

    "Seu cabelo é uma mistura de um moicano com um mullet, ele possui um cavanhaque apenas no queixo, semelhante a um bode."

    "Seu rosto quadrado possui um nariz meio torto, uma cicatriz que cruza sua sobrancelha direita, um brinco em sua orelha esquerda e um olhar frio e distante."

    "Quem é esse cara? Por quê ele tá me encarando? Ele parece ser durão, tem maior cara de encrenqueiro. A gente tá em uma disputa pra quem pisca primeiro?"

    show johnny irritado2 at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    "???"  "Ow!... Quem é você?..."

    show johnny irritado2 at center:
        matrixcolor TintMatrix("#fff")
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    Ren "OI? Ah! Meu… Meu nome é Ren."

    "Droga, já to começando a me enrolar."

    show johnny irritado2 at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    "???" "E o que você tá fazendo aqui?"

    show johnny irritado2 at center:
        matrixcolor TintMatrix("#fff")
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    Ren  "Vim pra cá escrever uma matéria sobre o centro comunitário."

    "O jovem no banco resmunga algo para si mesmo e anda até Ren. Ele para bem diante de mim com um olhar de escárnio."

    show johnny irritado2 at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    "???"  "Que tipo de matéria?"

    show johnny irritado2 at center:
        matrixcolor TintMatrix("#fff")
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    Ren  "E..e..e eu sou es… estudan… estudante de jornalismo e… e… precisava de…de uma matéria intere..re..re..ssante pro trabalho fi…fi..final de uma das mi...mi…minhas matérias..."

    "A ansiedade bateu forte."

    show johnny neutro1 at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    "???"  "Jornalismo?"

    "???" "Então você é o sobrinho do Seu Astolfo? Vi você com ele na entrada."

    show johnny neutro1 at center:
        matrixcolor TintMatrix("#fff")
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    Ren "…*suspiro* Sim sou eu…"

    "Esse cara ainda é intimidador."

    show johnny sorrindo1 at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    "???"  "Meu nome é Johnny."

    show johnny sorrindo1 at center:
        matrixcolor TintMatrix("#fff")
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    Ren  "Prazer em te conhecer Johnny. Pode me responder algumas perguntas sobre o centro?"

    show johnny neutro1 at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Joh  "Dependendo das perguntas… Prefiro manter certos detalhes pessoais fora da conversa…"

    show johnny neutro1 at center:
        matrixcolor TintMatrix("#fff")
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")
    jump Cena_Introducao_Johnny_Escolha_1

label Cena_Introducao_Johnny_Escolha_1:
    menu:
        "Que tipo de atividades você costuma fazer aqui no centro comunitário?":
            call Johnny_positiva_1_a
        "Por que você ainda vem ao centro?":
            call Johnny_negativa_1_b
label Johnny_positiva_1_a:   #[Escolha A (Positiva- Joh) "Que tipo de atividades você costuma fazer aqui no centro comunitário?"

    $ pointsJohnny+=1

    show johnny sorrindo1 at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Joh "Eu dou aulas de violão e guitarra aqui no centro durante as tardes. É uma boa maneira de praticar e ajudar algumas das pessoas da comunidade."

    Joh "Além, de vez em quando, ajudar com algumas coisas de manutenção do centro quando eu tenho algum tempo livre nos finais de semana."

    show johnny sorrindo1 at center:
        matrixcolor TintMatrix("#fff")
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    "A sua expressão passa de intimidadora para algo mais alegre."

    Ren  "E você faz isso há quanto tempo?"

    show johnny sorrindo1 at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Joh "Eu comecei com as aulas há mais ou menos uns 2 anos, mas eu frequento o centro já faz uns…"

    show johnny sorrindo1 at center:
        matrixcolor TintMatrix("#fff")
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    "Voz no fundo"  "Johnny! Pode dar uma mão aqui? Não to conseguindo fazer o acorde de fá menor."

    show johnny neutro1 at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Joh  "Tô indo aí! Tenho que ir, mais tarde a gente continua."

    Ren "Ok!"

    hide johnny neutro1 at center with dissolve

    "Ele parece uma pessoa legal."

    $ talkToJohnny1 = True

    jump Cena_Introducao_personagens
    with fade

label Johnny_negativa_1_b:    #[Escolha B (Negativa- Joh) "Porquê você ainda vem ao centro?"
    "A expressão dele fica mais séria."

    show johnny irritado2 at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Joh  "Que tipo de pergunta é essa?!… Eu venho aqui porque eu quero."

    show johnny irritado2 at center:
        matrixcolor TintMatrix("#fff")
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    Ren "Tá, mas há quanto tempo você vem aqui?"

    show johnny neutro1 at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Joh "Sei lá, há algum tempo eu acho."

    show johnny neutro1 at center:
        matrixcolor TintMatrix("#fff")
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    Ren "Mas, quanto tempo? Eu preciso de números."

    show johnny irritado2 at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Joh "Muito tempo, ok? Achei que você não ia fazer perguntas pessoais."

    show johnny irritado2 at center:
        matrixcolor TintMatrix("#fff")
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    Ren  "Desculpa, achei que essa pergunta não era muito…"

    show johnny neutro1 at center:
        matrixcolor TintMatrix("#fff")
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    "Voz no fundo" "Johnny! Pode dar uma mão aqui? Não to conseguindo fazer…"

    show johnny neutro1 at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Joh "Tenho que ir, boa sorte com a sua matéria."

    hide johnny neutro1 at center with dissolve

    "Talvez… eu tenha começado com o pé errado…"

    $ talkToJohnny1 = True

    jump Cena_Introducao_personagens
    with fade

label Cena_Quarto_dia1:

    scene bg quarto
    with fade

    play music "audio/4_Dramatic_1_Master.mp3" fadeout 1.0

    "Foi um dia bem agitado mas muito divertido. Apesar de ter acabado de conhecer, senti uma grande conexão com o ambiente do centro comunitário."

    "Vai dar muito ao que eu escrever sobre para minha matéria!"

    "Conheci muitas pessoas diferentes e únicas… Mas a que mais está em minha cabeça no momento é..."

    menu:
        "Johnny":
            "O Johnny me pareceu um cara bem intimidador, fechado… mas parece que tem um bom coração… lá no fundo… bem no fundo na verdade."

            "Talvez amanhã eu converse mais com ele."
        "Priscila":
            "A Priscila parece ser alguém bem preguiçosa, mas é bastante amigável com os outros. Por conta disso, em pouquíssimo tempo já me senti confortável perto dela."

            "Porém eu sinto que ela pode acabar não sendo a melhor pessoa para ajudar em qualquer tipo de atividade que exija esforço e isso pode atrapalhar para socializar com algumas pessoas que valorizam mais trabalho duro."

            "Humm… Me pergunto o porquê dela ser tão preguiçosa…"
        "Raul":
            "Raul é muito gente boa, temos muitos gostos em comum."

            "Ele é definitivamente uma pessoa que eu chamaria para um rolê. A vibe que ele passa é de alguém aberto para os outros e sempre pronto para puxar conversa."
        "Alexandra":
            "Alexandra é uma garota linda. Acho que aquela imagem dela meticulosamente tocando piano na sala vai para sempre ficar na minha cabeça…"

            "Mas eu não consegui atravessar a atitude fria dela como consegui com os outros. Talvez eu tenha feito uma primeira impressão ruim."

            "Pensando bem… A Priscila não mencionou o nome dela quando falou sobre os outros frequentadores do centro. Será que elas não se conhecem?"

            "Mas acho que é impossível. Considerando como todo mundo ali parece que frequenta há bastante tempo."

            "Espero amanhã conseguir conversar melhor com ela. Algo sobre ela me intriga e não sai da minha cabeça…"
return
