label JohnnyAlexandra:

    scene bg sala de musica
    with fade

    show johnny neutro1 at left with dissolve:
        xalign 0.1
        yalign 1.0
        zoom 0.5
        matrixcolor TintMatrix("#777")

    show alexandra neutral at right with dissolve:
        xalign 0.9
        yalign 1.0
        zoom 0.5
        matrixcolor TintMatrix("#777")

    "Alexandra se encontra de pé na frente do piano enquanto junta algumas partituras que estavam sobre o mesmo. Johnny está de braços cruzados apoiado em uma parede próxima."

    show johnny irritado2 at left:
        matrixcolor TintMatrix("#777")
        xalign 0.1
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Joh "Então, você acha que essa música chata é realmente a melhor escolha para a gente colocar durante o festival?"

    show johnny irritado2 at left:
        matrixcolor TintMatrix("#fff")
        xalign 0.1
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    show alexandra angry at right:
        matrixcolor TintMatrix("#777")
        xalign 0.9
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Ale "Não tem nada de errado com os clássicos, talvez você só não tenha classe para apreciá-los"

    show alexandra angry at right:
        matrixcolor TintMatrix("#fff")
        xalign 0.9
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    show johnny irritado2 at left:
        matrixcolor TintMatrix("#777")
        xalign 0.1
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Joh "Pffft! Você sabe que você vai fazer todo mundo dormir com isso né?"

    show johnny irritado2 at left:
        matrixcolor TintMatrix("#fff")
        xalign 0.1
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    show alexandra angry at right:
        matrixcolor TintMatrix("#777")
        xalign 0.9
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Ale "Ao menos não vai dar dor de cabeça a todos eles com seu barulho."

    "O clima está bem tenso na sala de música. Alexandra e Johnny parecem estar brigando."

    show alexandra angry at right:
        matrixcolor TintMatrix("#fff")
        xalign 0.9
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    show johnny irritado2 at left:
        matrixcolor TintMatrix("#777")
        xalign 0.1
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Joh "Pelo menos o meu barulho tem personalidade. E não é uma música de elevador chata!"

    show johnny irritado2 at left:
        matrixcolor TintMatrix("#fff")
        xalign 0.1
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    show alexandra angry at right:
        matrixcolor TintMatrix("#777")
        xalign 0.9
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Ale "Tenha um pouco de respeito com os convidados que vão vir! É a última chance deles de vir ao centro. Você não concorda, Ren?"

    "Ela me nota parado aqui observando a briga… E me puxa imediatamente para o lado dela. Engulo em seco com isso."

    show alexandra angry at right:
        matrixcolor TintMatrix("#fff")
        xalign 0.9
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    show johnny irritado2 at left:
        matrixcolor TintMatrix("#777")
        xalign 0.1
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Joh "O que você acha Ren? O que deveria tocar no festival?"

    show johnny irritado2 at left:
        matrixcolor TintMatrix("#fff")
        xalign 0.1
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    menu:
        "Eu prefiro a música do Johnny. Pode até ser barulhenta mas traz um pouco mais de animação pro evento":
            call Resposta_Johnny
        "Bem… Eu acho que os clássicos podem trazer uma boa imagem para o centro. Além de ser muito agradável!":
            call Resposta_Alexandra
        "Acho que ambas são escolhas excelentes!":
            call Resposta_NeutraJohnnyAlexandra

label Resposta_Johnny:

    $pointsJohnny += 1

    show johnny rindo1 at left:
        matrixcolor TintMatrix("#777")
        xalign 0.1
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Joh "Viu! É disso que eu tava falando!"

    show johnny sorrindo1 at left:
        matrixcolor TintMatrix("#fff")
        xalign 0.1
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    show alexandra disgust at right:
        matrixcolor TintMatrix("#777")
        xalign 0.9
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Ale "…"

    "Alexandra se cala, mas ela parece um pouco chateada com isso… Me sinto um pouco mal agora."

    "O Johnny olha um pouco para ela e suspira."

    show alexandra disgust at right:
        matrixcolor TintMatrix("#fff")
        xalign 0.9
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    show johnny pensativo1 at left:
        matrixcolor TintMatrix("#777")
        xalign 0.1
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Joh "…Olha, talvez eu conheça algumas músicas que tem alguns instrumentos clássicos e um ritmo um pouco mais calmo. O que você acha?"

    show johnny pensativo1 at left:
        matrixcolor TintMatrix("#fff")
        xalign 0.1
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    show alexandra sigh at right:
        matrixcolor TintMatrix("#777")
        xalign 0.9
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Ale "*suspira* Bem… Eu não seria digna de uma estudante de música se eu fosse contra experimentar coisas diferentes."

    show alexandra neutral at right:
        matrixcolor TintMatrix("#fff")
        xalign 0.9
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    Ale "Talvez depois você possa me mostrar algumas. Existem músicas clássicas que são mais agitadas também, você sabe?"

    "Fico feliz deles terem achado um meio termo, e acho que isso pode trazer um pouco de empolgação para o festival."

label Resposta_Alexandra:

    $ pointsAlexandra += 1

    show alexandra happy 2 at right:
        matrixcolor TintMatrix("#777")
        xalign 0.9
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Ale "Hah. Viu só? Sua música petulante só ia afastar as pessoas do centro."

    "Por mais que eu concorde com ela, não precisava ser tão ríspida assim."

    show alexandra happy 2 at right:
        matrixcolor TintMatrix("#fff")
        xalign 0.9
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    show johnny irritado2 at left:
        matrixcolor TintMatrix("#777")
        xalign 0.1
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Joh "Hmpf…"

    show johnny irritado2 at left:
        matrixcolor TintMatrix("#fff")
        xalign 0.1
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    show alexandra sad at right:
        matrixcolor TintMatrix("#777")
        xalign 0.9
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Ale "..."

    Ale "Desculpa. Acabei me exaltando um pouco. Não costumo ser assim…"

    Ale "Olha. Talvez a gente possa entrar em um acordo?"

    show alexandra sad at right:
        matrixcolor TintMatrix("#fff")
        xalign 0.9
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    show johnny triste1 at left:
        matrixcolor TintMatrix("#777")
        xalign 0.1
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Joh "*suspiro* Relaxa… talvez de fato a minha música não seja a mais apropriada para essa situação…"

    show johnny triste1 at left:
        matrixcolor TintMatrix("#fff")
        xalign 0.1
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    show alexandra sad at right:
        matrixcolor TintMatrix("#777")
        xalign 0.9
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Ale "N-Não é verdade! Mas os exemplos que você me mostrou são um pouco…"

    show alexandra sigh at right:
        matrixcolor TintMatrix("#777")
        xalign 0.9
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Ale "Demais para a situação."

    show alexandra sad at right:
        matrixcolor TintMatrix("#fff")
        xalign 0.9
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    show johnny neutro1 at left:
        matrixcolor TintMatrix("#777")
        xalign 0.1
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Joh "Eu acho que eu conheço algumas músicas que estejam mais de acordo, aí a gente pode ir vendo isso junto, que tal?"

    show johnny triste1 at left:
        matrixcolor TintMatrix("#fff")
        xalign 0.1
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    show alexandra happy 2 at right:
        matrixcolor TintMatrix("#777")
        xalign 0.9
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Ale "Vejo que agora temos um acordo."

    show alexandra happy 2 at right:
        matrixcolor TintMatrix("#fff")
        xalign 0.9
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    Ren "Viu só pessoal? Vocês podem encontrar qualidades em comum com as suas músicas no fim!"

    "Fico feliz que Alexandra tenha repensado um pouco sua fala. Ela e Johnny são duas pessoas extremamente cabeça dura."

    "Não consigo imaginar o que aconteceria se eles brigassem de verdade."

label Resposta_NeutraJohnnyAlexandra:

    show alexandra sigh at right:
        matrixcolor TintMatrix("#777")
        xalign 0.9
        yalign 1.0
        zoom 0.5

    show johnny irritado2 at left:
        matrixcolor TintMatrix("#777")
        xalign 0.1
        yalign 1.0
        zoom 0.5

    "Os dois me encaram intensamente."

    "Talvez eu não devesse ter dito isso."

    "Mas eu realmente queria que eles parassem de brigar. A gente nunca vai conseguir organizar o festival com eles discordando o tempo todo!!"

    Ren "B-Bem! Música clássica certamente dá uma boa impressão ao centro! Mas rock e metal costumam manter a galera animada e engajada."

    Ren "T-Talvez conseguíssemos… Misturar os dois?"

    "Fico nervoso. Olhar de Alexandra me faz sentir como se fosse um vento gelado cortante, e do Johnny é como se minha mão estivesse numa brasa quente."

    "Ser puxado nessa discussão é um causador de hipotermia psicológica… E talvez eu esteja ficando um pouco criativo demais com essas analogias."

    show alexandra disgust at right:
        matrixcolor TintMatrix("#777")
        xalign 0.9
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Ale "..."

    show alexandra disgust at right:
        matrixcolor TintMatrix("#fff")
        xalign 0.9
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    show johnny irritado2 at left:
        matrixcolor TintMatrix("#777")
        xalign 0.1
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Joh "..."

    show johnny irritado2 at left:
        matrixcolor TintMatrix("#fff")
        xalign 0.1
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    hide johnny irritado2 at left with dissolve

    hide alexandra disgust at right


    "Os dois saíram sem falar nada..."

    " Talvez eu devesse ter dito outra coisa..."
