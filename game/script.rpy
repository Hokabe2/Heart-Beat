# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define Ren = Character("Ren")
define Raul = Character("Raul")
define Johnny = Character("Johnny")
define Priscila = Character("Priscila")
define Alexandra = Character("Alexandra")

define Astolfo = Character("Astolfo")
# The game starts here.

label start:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    "BZZZZ!
    BZZZZ!
    BZZZZ!"

    Ren "{cps=40}Quem será a essa hora?!{/cps}"

    "{cps=40}Vejo na tela do meu celular um email.{/cps}"
    "{cps=40}Assunto: Centro Comunitário prestes a ser fechado! Urgente{/cps}"
    "{cps=40}Caro Ren,
    Vi que você postou no fórum de jornalistas que estava a procura de uma história para seu trabalho de final de semestre. Acredito que tenho uma história quente pra você. Segue em anexo algumas informações para uma possível matéria
    Espero que tenha ajudado”.{/cps}"


    Ren "{cps=40}Uma resposta do fórum de jornalistas independentes? Eu postei um pedido de ajuda lá faz uns três dias, e até agora nenhuma das histórias que me passaram me parecia interessante.{/cps}"
    "{cps=40}Sinceramente, é meio difícil escrever uma matéria interessante sobre um carro que fala frases de efeito. Depois que ele repete a mesma frase pela 10ª vez, começa a ficar meio irritante.{/cps}"
    "{cps=40}Ok… Um centro comunitário… Relevância histórica, bom… No meio do nada, tá… Fechado por falta de visitantes… Eu posso trabalhar com isso, já que eu estou atrasado com esse trabalho.{/cps}"
    "{cps=40}E ainda por cima é na cidade do meu tio Astolfo! Posso aproveitar e visitar ele, faz um bom tempo que a gente não se vê. Vou mandar mensagem pra ele perguntando se posso ficar com ele enquanto escrevo a matéria.{/cps}"
    "{cps=40}Estranho. O e-mail não foi assinado e não dá pra saber quem mandou pelo apelido… Minha primeira fonte anônima! Isso vai ser interessante, ou um desastre. Mas é melhor do que o carro que fala. Vou comprar a passagem pra amanhã.{/cps}"

    jump Cena_Introducao_email

    # Introdução
label Cena_Introducao_email:

    Ren "{cps=40}Essa foi com certeza uma das decisões mais impulsivas que já fiz.. Me esqueço o quanto a grana de um universitário é curta. É bom no fim essa viagem valer a pena!{/cps}"

    Ren "{cps=40}Com o sol ardente na minha cara, eu pego o celular do meu bolso para mandar uma mensagem para meu tio dizendo que já cheguei.{/cps}"

    #[Efeito de som de pássaro ou inseto]

    Ren "{cps=40}A vida no interior é realmente bem mais pacata que a da cidade grande. O sol está muito forte, mas o ar parece mais fresco e–{/cps}"

    #[Barulho de carro buzinando muito alto]

    "{cps=40}Astolfo aparece da janela do carro acenando{/cps}"

    Astolfo "{cps=40}MEU GAROTO!! QUANTO TEMPO!!{/cps}"

    Ren "{cps=40}A voz alta e característica do meu tio me distraí de meus pensamentos apreciando a beleza do interior ao meu redor-{/cps}"

    Ren "{cps=40}Então eu pego minha mala e ando até o carro onde ele acena e sento no banco da frente ao lado dele.{/cps}"

    Ren "{cps=40}Oi Tio!! Quanto tempo a gente não se vê né– Aghgh{/cps}"

    Ren "{cps=40}Do nada minha respiração foi cortada pela força de dois braços me agarrando- O que também pode ser conhecido como um abraço.{/cps}"

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
    "TESTE"

label Cena_Introducao_Priscila:

label Cena_Introducao_Alexandra:

label Cena_Introducao_Johnny:

    return
