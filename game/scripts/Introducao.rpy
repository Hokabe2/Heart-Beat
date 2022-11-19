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

        # Introdução
label Cena_Introducao_email:

        scene bg cafe

        "Onde está o tio Astolfo? Ele me mandou mensagem a menos de cinco minutos atrás falando pra me encontrar aqui…"

        "Será que ele se perdeu?... Ele já se perdeu num parque aquático e a gente ficou procurando ele por duas horas pra encontrar ele tentando trazer um monte de patos pra piscina de ondas…"

        Ren "Pera… que som é esse?"

        "???" "TIIIIIIIIIIOOOOOOOOOOOOOOO AAASSSSSSSSSSSSSSSSTOOOOOOOOOLLLLLLLLFFFFFFFFOOOOOOOOOO A CAMIIIIIIIINHOOOOOOOOOOOOOOOOOOO"

        Ren "O senhor sempre foi ‘único’ nas suas entradas Tio Astolfo"

        Tio_Astolfo "Ora, uma boa entrada sempre precede uma conversa fenomenal"

        Tio_Astolfo "Então meu sobrinho, fiquei sabendo que você está aqui para fazer um trabalho acadêmico"

        Ren "Ah sim! Tenho uma matéria pra entregar pro final do mês e…"

        Tio_Astolfo "Sobre o que vai ser esta matéria? Será sobre seu adorável tio?"


        "Uma matéria sobre o Tio Astolfo seria interessante, porém acho difícil que os professores aceitariam… Talvez eu faça algo sobre as histórias dele em um próximo semestre"

        Ren "Na verdade é sobre o centro comunitário local. Recebi um e-mail outro dia falando sobre o lugar, então eu vim pesquisar"

        Tio_Astolfo "O Centro Comunitário? Olha mas que sorte, pelos últimos vinte anos eu fui responsável pelo centro. Venha, vou te contar sobre isso tudo enquanto vamos para lá"

        Tio_Astolfo "PARA O ASTOLFO MÓVEL!!!"

        "Pelo amor de Deus aquela Kombi velha de novo não… A última vez que eu entrei lá o Tio Astolfo quase jogou a gente em um barranco tentando se livrar de uma mosca…"

        "O Tio Astolfo corre de maneira cômica em direção a uma Kombi cheia de decalques enquanto Ren segue lentamente decepcionado"

        #Eles vão para o centro comunitário

        jump Cena_Introducao_personagens

label Cena_Introducao_personagens:

        scene bg exterior

        #Menu de decisões para conhecer os personagens
        menu:
            "Biblioteca":
                jump Cena_Introducao_Raul
            "Copa":
                jump Cena_Introducao_Priscila
            "Sala de música":
                jump Cena_Introducao_Alexandra
            "Pátio":
                jump Cena_Introducao_Johnny

label Cena_Introducao_Raul:
        Ren "Decidi ir para a biblioteca."

        Ren "Havia três prateleiras com diversos gibis, livros infantis e infantojuvenis."

        Ren "Fui vendo e folheando alguns dos catálogos. Eu costumava ler muitos gibis quando eu era criança. Sempre tinha um desses quando ia ao consultório médico fazer um daqueles exames que demoram uma hora para chegar a sua vez para uns 15 minutos de exame de verdade."

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

        Ren "Passei o meu contato para ele e sorrimos juntos, definitivamente gostei da vibe desse cara."

        jump Cena_Introducao_personagens
label Raul_positiva_1_a:
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
    return

label Cena_Introducao_Alexandra:
    return

label Cena_Introducao_Johnny:

    "Em um dos bancos no pátio do centro comunitário se encontra um jovem ouvindo música"

    "Ele emana uma aura bem intimidadora, enquanto observava o seu entorno. Ele usa um colete jeans rasgado, uma camiseta preta com uma estampa vermelha, suas calças são rasgadas e ele usa coturnos bem altos."

    "Seu cabelo é uma mistura de um moicano com um mullet, ele possui um cavanhaque apenas no queixo, semelhante a um bode. Seu rosto quadrado possui um nariz meio torto, uma cicatriz que cruza sua sobrancelha direita, um brinco em sua orelha esquerda e um olhar frio e distante. "

    "Quem é esse cara? Por quê ele tá me encarando? Ele parece ser durão, tem maior cara de encrenqueiro. A gente tá em uma disputa pra quem pisca primeiro?"

    "???"  "Ow!... Quem é você?..."

    Ren "OI? Ah! Meu… Meu nome é Ren"

    "Droga, já to começando a me enrolar"

    "???" "E o que você tá fazendo aqui?."

    Ren  "Vim pra cá escrever uma matéria sobre o centro comunitário"

    "O jovem no banco resmunga algo para si mesmo e anda até Ren. Ele para bem diante de mim com um olhar de escárnio"

    "???"  "Que tipo de matéria?"

    Ren  "E..e..e eu sou es… estudan… estudante de jornalismo e… e… precisava de…de uma matéria intere..re..re..ssante pro trabalho fi…fi..final de uma das mi...mi…minhas matérias"

    "A ansiedade bateu forte"

    "???"  "Jornalismo?"

    "???" "Então você é o sobrinho do Seu Astolfo? Vi você com ele na entrada"

    Ren "…*suspiro* Sim sou eu…"

    "Esse cara ainda é intimidador."

    "???"  "Meu nome é Johnny."

    Ren  "Prazer em te conhecer Johnny. Pode me responder algumas perguntas sobre o centro?"

    Joh  "Dependendo das perguntas… Prefiro manter certos detalhes pessoais fora da conversa…"

    menu:
        "Que tipo de atividades você costuma fazer aqui no centro comunitário?":
            call Johnny_positiva_1_a
        "Por que você ainda vem ao centro?":
            call Johnny_negativa_1_b
label Cena_Introducao_Johnny_Escolha_1:
label Johnny_positiva_1_a:   #[Escolha A (Positiva- Joh) "Que tipo de atividades você costuma fazer aqui no centro comunitário?"
label Johnny_negativa_1_b:    #[Escolha B (Negativa- Joh) "Porquê você ainda vem ao centro?" 

return
