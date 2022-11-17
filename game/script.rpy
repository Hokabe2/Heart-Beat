# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Ren = Character("Ren")
define Raul = Character("Raul")
define Joh = Character("Johnny")
define Pris = Character("Priscila")
define Ale = Character("Alexandra")

define Astolfo = Character("Astolfo")
# The game starts here.

label start:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    python:
        ShowText("","{sc=4}BZZZZ! BZZZZ! BZZZZ!{/sc}")

    show alexandra happy at center:
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.8
        linear 0.15 yalign 1.0


    Ren "Quem será a essa hora?!"

    "Vejo na tela do meu celular um email."
    "Assunto: Centro Comunitário prestes a ser fechado! Urgente"
    "Caro Ren,
    Vi que você postou no fórum de jornalistas que estava a procura de uma história para seu trabalho de final de semestre. Acredito que tenho uma história quente pra você. Segue em anexo algumas informações para uma possível matéria
    Espero que tenha ajudado”."


    Ren "Uma resposta do fórum de jornalistas independentes? Eu postei um pedido de ajuda lá faz uns três dias, e até agora nenhuma das histórias que me passaram me parecia interessante."
    "Sinceramente, é meio difícil escrever uma matéria interessante sobre um carro que fala frases de efeito. Depois que ele repete a mesma frase pela 10ª vez, começa a ficar meio irritante."
    "Ok… Um centro comunitário… Relevância histórica, bom… No meio do nada, tá… Fechado por falta de visitantes… Eu posso trabalhar com isso, já que eu estou atrasado com esse trabalho."
    "E ainda por cima é na cidade do meu tio Astolfo! Posso aproveitar e visitar ele, faz um bom tempo que a gente não se vê. Vou mandar mensagem pra ele perguntando se posso ficar com ele enquanto escrevo a matéria."
    "Estranho. O e-mail não foi assinado e não dá pra saber quem mandou pelo apelido… Minha primeira fonte anônima! Isso vai ser interessante, ou um desastre. Mas é melhor do que o carro que fala. Vou comprar a passagem pra amanhã."

    jump Cena_Introducao_email

    # Introdução
label Cena_Introducao_email:

    Ren "Essa foi com certeza uma das decisões mais impulsivas que já fiz.. Me esqueço o quanto a grana de um universitário é curta. É bom no fim essa viagem valer a pena!"

    Ren "Com o sol ardente na minha cara, eu pego o celular do meu bolso para mandar uma mensagem para meu tio dizendo que já cheguei."

    #[Efeito de som de pássaro ou inseto]

    Ren "A vida no interior é realmente bem mais pacata que a da cidade grande. O sol está muito forte, mas o ar parece mais fresco e–"

    #[Barulho de carro buzinando muito alto]

    "Astolfo aparece da janela do carro acenando"

    Astolfo "MEU GAROTO!! QUANTO TEMPO!!"

    Ren "A voz alta e característica do meu tio me distraí de meus pensamentos apreciando a beleza do interior ao meu redor-"

    Ren "Então eu pego minha mala e ando até o carro onde ele acena e sento no banco da frente ao lado dele."

    Ren "Oi Tio!! Quanto tempo a gente não se vê né– Aghgh"

    Ren "Do nada minha respiração foi cortada pela força de dois braços me agarrando- O que também pode ser conhecido como um abraço."

    #Eles vão para o centro comunitário

    jump Cena_Introducao_personagens

label Cena_Introducao_personagens:
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

    jump Escolha_1

    #Escolha 1
label Escolha_1:
    menu:
        "Você frequenta o centro comunitário há quanto tempo?":
            call Raul_positiva_1_a
        "Eu acabei entrando no projeto por causa de um trabalho da faculdade":
            call Raul_positiva_1_b

    label Escolha_1_continuacao:

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

    return

label Raul_positiva_1_b:
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

    return

label Cena_Introducao_Priscila:

label Cena_Introducao_Alexandra:


label Cena_Introducao_Johnny:


    return
