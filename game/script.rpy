# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileenn")
define Ren = Character("Ren")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    "Na escuridão completa, escutamos um som de um telefone vibrando."
    "BZZZZ!
    BZZZZ!
    BZZZZ!"
    Ren "(Gemido de irritação)"

    Ren "Quem será a essa hora?!"

    "Vemos uma tela de um smartphone. No display, vemos um email com as informações."
    "Assunto: Centro Comunitário prestes a ser fechado! Urgente"
    "Caro Ren,
    Vi que você postou no fórum de jornalistas que estava a procura de uma história para seu trabalho de final de semestre. Acredito que tenho uma história quente pra você. Segue em anexo algumas informações para uma possível matéria
    Espero que tenha ajudado” "


    Ren "Uma resposta do fórum de jornalistas independentes? Eu postei um pedido de ajuda lá faz uns três dias, e até agora nenhuma das histórias que me passaram me parecia interessante."


    "Sinceramente, é meio difícil escrever uma matéria interessante sobre um carro que fala apenas frases de efeito. Depois que ele repete a mesma frase pela 10ª vez, começa a ficar meio irritante"


    "Ok… Um centro comunitário… Relevância histórica, bom… No meio do nada, tá… Fechado por falta de visitantes… Eu posso trabalhar com isso. Especialmente já que eu estou atrasado com esse trabalho."


    "E ainda por cima é na cidade do meu Tio Astolfo! Posso aproveitar e visitar ele, faz um bom tempo que a gente não se vê. Vou mandar mensagem pra ele perguntando se posso ficar com ele enquanto escrevo a matéria."


    "Estranho. O e-mail não foi assinado e não dá pra saber quem mandou pelo apelido… Minha primeira fonte anônima! Isso vai ser interessante, ou um desastre. Mas é melhor do que o carro que fala. Vou comprar a passagem pra amanhã."


    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
