label Johnny_Dia5:

    scene bg sala de musica
    with fade

    show johnny neutro1 at center with dissolve:
        yalign 1.0
        zoom 0.5
        matrixcolor TintMatrix("#777")

    "Chego à sala de música e Johnny está praticando com sua guitarra."

    show johnny neutro2 at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Joh "Ei! Ainda bem que você chegou. Pode me fazer um favor? Preciso correr até em casa pra buscar o pedal pro festival. Pode ficar de olho nas minhas coisas? É aqui do lado."

    show johnny neutro2 at center:
        matrixcolor TintMatrix("#fff")
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    Ren "Ahmm… claro! Vou aproveitar e praticar um pouco também!"

    show johnny sorrindo1 at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Joh "Perfeito! Volto já já!"

    hide johnny sorrindo1 at center with dissolve

    jump Johnny_Dia5_PT2
    with fade

label Johnny_Dia5_PT2:

    scene bg sala de musica
    with fade

    play sound "audio/phone_vibration.mp3"

    "Eita, o Johnny deve ter esquecido o celular."

    "Parece que alguém está ligando da casa dele."

    "Talvez seja importante. Eu vou atender pra avisar que ele está a caminho."

    stop sound fadeout 3.0

    Ren "É... Alô?"

    "???" "Johnny? É você meu neto?"

    Ren "Não minha senhora, aqui é o Ren. Sou… amigo do Johnny."

    Ren "Isso. E daqui a pouco ele está chegando aí."

    "???" "'Ren'?"

    "???" "Ah... Você é o sobrinho do Astolfo?"

    "???" "Aquele pedaço de mal caminho..."

    Ren "Hmm, sim, sou eu..."

    Cida "Haha! Onde estão os meus modos?"

    Cida "Meu nome é Cida."

    Cida "Sou a avó do Johnny, mas você pode me chamar de Dona Cida."

    Cida "Me diga, você está fazendo o que com o telefone do meu neto."

    Ren "Ele esqueceu o telefone aqui no centro comunitário."

    Ren "Ele saiu para pegar o pedal da guitarra pro ensaio e..."

    Cida "Esse menino vive esquecendo as coisas dele pra tudo que é lado."

    Cida "Eu falo que ele precisa parar e descansar se não vai ficar todo esquecido."

    Cida "Eu falava a mesma coisa pro pai dele."

    "Agora... Eu fiquei curioso sobre uma coisa..."

    Ren "Dona Cida, eu fiquei curioso sobre uma coisa..."

    Cida "Diga, querido!"

    Ren " Onde estão os pais do Johnny, ele fala bem pouco dele mesmo."

    "Toda vez que ele ou alguém toca no assunto dos pais dele, ele parece desconversar ou trocar pra qualquer outro assunto"

    Cida "Oh… ó céus…"

    "Não gostei desse 'Oh… ó céus…'"

    Cida "Bom, os pais do Johnny…"

    Cida "Eles..."

    Cida "Eles faleceram em um acidente de carro há uns 10 anos atrás."

    Cida "Eles estavam voltando de uma viagem que eles fizeram só eles dois, e no caminho..."

    Cida "Foram acertados por um caminhão durante um temporal..."

    Ren "...poxa Dona Cida, eu... eu não sabia... Meus pêsames..."

    Cida "Oh, não se preocupe meu jovem, hoje em dia o que sobrou foram apenas as boas memórias do meu filho e da minha nora."

    Cida "E eu agradeço muito ao meu neto por ter cuidado de mim durante o meu momento de cura."

    Ren "Fico feliz que o Johnny tenha ajudado a senhora, ele é um jovem muito bondoso..."

    Cida "Ah mas ele tem um coração de ouro, isso é desde quando ele era criança, sabe?"

    Cida " Ele vivia distribuindo flores para todo mundo na rua."

    Cida "A gente tinha que crescer o dobro de flores pra ter o que o vender."

    "Hehe, é um pouco difícil imaginar o Johnny distribuindo flores na rua."

    Cida "É... naquela época ele vivia sorrindo... Mas então veio o acidente."

    Cida "Meu neto começou a se isolar, se envolver em confusões, afrontar os mais velhos..."

    Cida "Ele já não sorria mais, especialmente depois que eu decidi fechar a floricultura para cuidar da minha saúde..."

    "Isso explica a reputação do Johnny..."

    "Mal consigo imaginar o que ele devia pensar na época..."

    "Se bem que todo mundo passa pelo luto da sua maneira"

    Ren "Mas... ele superou… não?"

    Cida "Em parte, sim… E eu agradeço imensamente ao seu tio por isso."

    Ren "O tio Astolfo? Como assim?"

    Cida "O centro significava muito para os pais do Johnny, e quando o Astolfo ouviu o que estava acontecendo, acolheu o Johnny de braços abertos."

    Cida "Chamou ele para dar aulas e ajudar a cuidar do lugar. E junto com isso ele escutou o que o menino tinha a falar."

    "Tio... Você é demais!"

    Cida "E quando as coisas foram melhorando, eu reabri a minha floricultura."

    Cida "Isso encheu o meu netinho de alegri-"

    Cida "Ah meu filho, você chegou eu estava tentando falar com você pelo telefone mas você não estava atendendo..."

    "O Johnny deve ter chegado na floricultura. Consigo ouvir a voz dele pelo telefone"

    Joh "Bença vó! Vim buscar as minhas coisas que eu esqueci. A senhora viu onde eu deixei?"

    Cida "Estão na entrada da garagem, onde você deixou."

    Cida "Inclusive, você poderia me ajudar a pegar a minha vitrola pra eu ouvir os meus discos do Elvis?"

    Joh "Brigado vó! A senhora é demais! Vou separar a sua vitrola lá."

    Cida "Enfim… é basicamente isso meu filho. Vê se cuida viu?"

    Ren "Pode deixar Dona Cida!"

    Cida "Também manda um beijo para o seu tio, aquele homem gos-"

    Ren "Pode deixar, Dona Cida… Eu vou mandar!"

    "A ligação acabou caindo agora no final."

    "Hmmm..."

    "Não imaginava que o Johnny tivesse passado por tanto..."

    "Eu não vou falar disso com ele, pode ser que ele fique bravo..."

    "Pelo menos não até o festival acabar..."

    jump Johnny_Dia5_PT3
    with fade

label Johnny_Dia5_PT3:

    scene bg sala de musica
    with fade

    "Algum tempo se passa e o Johnny volta para a sala de música."

    show johnny animado2 at center with dissolve:
        yalign 1.0
        zoom 0.5
        matrixcolor TintMatrix("#777")

    show johnny animado2 at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Joh "Cheguei! Aproveitei e peguei o amplificador maior…"

    Joh "*Respira* Perdi alguma coisa?"

    show johnny animado2 at center:
        matrixcolor TintMatrix("#fff")
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    Ren "Não... Acho que não..."

    show johnny animado2 at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Joh "Beleza então. *Respira*"

    Ren "Ah, Johnny..."

    show johnny pensativo1 at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Joh "Hmm?"

    show johnny pensativo1 at center:
        matrixcolor TintMatrix("#fff")
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    Ren "É..."

    Ren "..."

    show johnny neutro1 at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Joh "Desembucha."

    show johnny neutro1 at center:
        matrixcolor TintMatrix("#fff")
        yalign 1.0
        zoom 0.5
        linear 0.1 matrixcolor TintMatrix("#777")

    Ren "Nada demais, é só que..."

    Ren "Você é forte, cara!"

    show johnny preocupado2 at center:
        matrixcolor TintMatrix("#777")
        yalign 1.0
        zoom 0.5
        linear 0.15 yalign 1.0
        linear 0.15 yalign 0.85
        linear 0.1 matrixcolor TintMatrix("#fff")
        linear 0.15 yalign 1.0

    Joh "Hã? Mas esse amplificador até que é levinho, não pesa nem vinte quilos."

    "Acho que ele não entendeu o porquê de eu ter falado isso..."

    "Mas tudo bem, é melhor assim mesmo."

    "Agora eu entendo o Johnny melhor e é isso que importa."
