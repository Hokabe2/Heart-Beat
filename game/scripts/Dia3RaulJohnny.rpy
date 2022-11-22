#DIA 3 - Johnny e Raul
#INT- SALA DE MÚSICA- DIA 3
label Dia3_RaulJohnny:
#[Vou ir checar a sala de música]
    scene bg sala de musica
    with fade

    Joh "Ok… Raul, me passa a chave de fenda?"

    Raul "Aqui! Agora passa aquele cabo ali por trás e conecta na entrada C"

    Joh "Passei e… Conectei. Agora testa o violão"

    Ren "O- Oi pessoal. Precisam de ajuda?"

    Raul "Fala Ren! A gente tá montando o equipamento para a apresentação, se quiser ajudar…"

    Joh "Só não atrapalhe, a gente passou duas horas só arrumando os cabos."

    Raul "Inclusive, aquele cabo ali ficou solto…"

    Joh "AAAAAAAAAAAAAHHHHHHHGHHHHH!"

    Raul "Droga, vamos ter que testar de novo."

    Joh "Ren! Liga e desliga a caixa de som."

    "No fim, demoramos uma hora para fazer a caixa de som funcionar. Quando não era o cabo que não funcionava, era a tomada; se a tomada funcionava, era mau contato com o plugin."

    Joh "Raul."

    Raul "Fala Johnny."

    Joh "Lembra do disco que eu emprestei pra você mês passado…?"

    Raul "Ah..? É aquele disco do Legião Urbana? Hehehe eu esqueci dele."

    Joh "E você vai me devolver quando Raul…?"

    Raul "Já devolvo nesta semana. Sem falta, confia."

    Joh "E é bom estar em bom estado, porque já é o terceiro que você pegou emprestado esse mês."

    Raul "Relaxa eu sempre devolvo uma hora ou outra."

    "Eu me pergunto que hora ou outra é essa."

    #Acho que dá para desenvolver mais esse diálogo até o Ren pedir para participar do festival

    Ren "Ah gente… Eu andei pensando e… Se eu posso participar das apresentações no festival."

    #Johnny surpreso

    #Raul surpreso

    Joh "E você sabe tocar algo?"

    Ren "Eu já tive aulas de violão e guitarra no colegial."

    Raul "Tá… Mas você acha que consegue acompanhar a gente?"

    Ren "E-eu queria pelo menos tentar, não quero ficar apenas olhando sem fazer nada."

    Joh "Hmm… E você tem alguma experiência com música?"

    Ren "Eu era da banda da minha escola, sabia? Me deem uma chance, se eu ver que não dou conta, aí continuamos do que jeito que tá. Tudo bem para vocês?"

    "É mentira, não fui aceito na banda da escola porque me acharam ‘Ok mas não bom’. "

    "Senti um calafrio na espinha por algum motivo, será que foi um pedido muito idiota?"

    Raul "Hmmm…Ren, nos dê um minuto para conversar. Johnny vem aqui um instante."

    Joh "…"

    Raul "…Johnny que você acha…"

    #efeito de fade in e fade out

    "Em uns dois minutos eles voltaram para a sala."

    Joh "Nós decidimos que se você não perder o nosso tempo, vamos ver se você sabe tocar pelo menos o básico. Então mostra pra gente o que você sabe fazer?"

    Raul "Você prefere a guitarra ou o violão?"

    Ren "Eu…"

    jump Cena_Dia3_RaulJohnny_Escolha_1

label Cena_Dia3_RaulJohnny_Escolha_1:
    menu:
        "Vou tentar o violão":
            jump Raul_positiva_Escolha_1_a
        "Vou tentar a guitarra":
            jump Johnny_positiva_Escolha_1_b

label Raul_positiva_Escolha_1_a:
    #Escolha A
    #[Escolha A Raul "Vou tentar o violão" ]
    Raul "Boa escolha, mano! Relaxa que eu não mordo."

    Raul "Diferente de outro ser humano."

    Joh "Não pegue leve com o novato."

    Raul "Esfria a cabeça aí Johnny boy"

    Raul "Vamos começar com uma sequência simples. Sol, sol, mi, mi, mi e ré. Agora a tua vez"

    Ren "Lá vai… Sol, sol, mi… mi, mi e… ré"

    Raul "Mais uma vez."

    "Ok é mais tranquilo do que eu me lembrava. Os meus dedos ainda escorregam um pouco nas casas mas se eu sentar pra ensaiar eu acho que consigo."

    Raul "Isso! Você é o próximo Mano Brown."

    Raul "Vamos testar outra música."

    Joh "Eu vou terminar de arrumar o equipamento do lado de fora, boa sorte com o ensaio aí."

    jump Dia3_RaulJohnny_Escolha_1_continuacao

label Johnny_positiva_Escolha_1_b:
    #Escolha B
    #[Escolha B Joh "eh- Eu… Eu… to- topo, opito, pela guitarra" ]

    Joh "Vou logo avisando que nem vem com corpo mole ou com desculpinha que não consegue acompanhar o ritmo. "

    Ren "E-"

    Joh "Vamo que vamo porque eu não tenho o dia todo. Tá vendo essa guitarra?"

    Ren "Sim, é a sua guitarra."

    Joh "Se derrubar, já sabe o que acontece. Então trate ela com muito cuidado."

    Raul "*risadinhas*"

    "É mais pesada do que parece"

    Joh " Imagino que você já conhece as notas básicas, certo novato?"

    Ren "Si- sim!"

    Joh "B5, E5, G, D, E, B e E5. 1, 2, 3 e 4. Alguma pergunta?"

    Ren "Ok… Lá vai."

    "B5… E5, G, D, E… B, E5!"

    Joh "Nada mau… mais uma vez."

    "Ok é mais tranquilo do que eu me lembrava. O ritmo é um pouco acelerado, mas nem tanto. Os meus dedos ainda escorregam um pouco nas casas mas se eu sentar pra ensaiar eu acho que consigo."

    Joh "Boa, garoto! Acho que eu posso trabalhar com isso. Agora vamos tentar com outra música e  dessa vez com um pedal."

    Raul "Eu vou terminar de arrumar o equipamento do lado de fora, boa sorte com o ensaio aí."

    jump Dia3_RaulJohnny_Escolha_1_continuacao

label Dia3_RaulJohnny_Escolha_1_continuacao:
    #Continuação
    #INT- SALA DE MÚSICA- DIA 3
    scene bg sala de musica

    Ren "*espreguiçando* Ahhh meus dedos tão vermelhos."

    Joh "Nada mal, Ren. Nada mal… Você realmente mandou bem. Vai ser bom ter você lá no palco."

    Raul "Será isso mesmo que eu ouvi? O Edgy Boy está elogiando o forasteiro?"

    Joh "Não me vem essa agora."

    Raul "Essa é uma atitude de uma… como se chama mesmo? Tusun, Tocom…"

    Ren "Tsundere? "

    Ren "Aquelas personagens que se importam com os outros, mas que são agressivas para disfarçar os verdadeiros sentimentos?"

    Raul "Isso aí. A Pris tinha me falado que ela acha que o John- Joh-"

    Raul "JOFFREY do desenho do dançarino arco-íris age assim. Ha ha ha (rindo de nervoso)."

    Joh "Joffrey, tô sabendo."

    Joh "Humph… Ainda não sei o que se passa na cabeça dela, ela é estranha. Não sei porque ela age desse jeito toda vez que me vê."

    Raul "Deve ser por causa daqueles boatos."

    Joh "Eu espero que não."

    "Os dois começaram a falar entre eles e se esqueceram de mim. Eles se empolgaram em rememorar algumas aventuras legais que viveram juntos, a maioria quando eram moleques. "

    Raul "Falando nisso, lembra quando você teve aquela ideia de irmos até um barraco abandonado no fim da cidade?"

    Joh "Deveríamos ir lá de novo um dia desses."

    Joh "Foi por pouco que a polícia não enquadrou a gente."

    Ren "A polícia?! O que foi que vocês fizeram??"

    "Já tinha escutado boatos do Johnny, mas nunca soube que ele se envolveu com a polícia. E pelo visto Raul também estava metido nessa história."

    Raul "Não é nada de mais Ren, só foi um incidente pequeno. Ha, ha, ha…"

    Joh "Acho que não tem problema contarmos para ele. "

    Joh "Seguinte, promete que não vai falar para ninguém sobre isso, tudo bem?"

    Ren "Pro- pro- prometo!"

    "(A história é quando Raul e Johnny foram ver uma casa abandonada ali nas redondezas de noite. Porém eles perceberam que tinha mais alguém ali com eles. Eles ficaram desesperados, mas depois descobriram que eram apenas outras crianças da cidade, o Johnny tinha enfiado a cabeça de um dos meninos na privada.)"

    "Esses dois não se parecem de jeito nenhum. É como se um fosse um Pincher bombado prestes a explodir a qualquer momento e o outro, um filhote de Pitbull brincalhão."

    "Para ser sincero, sinto um pouco de inveja da amizade desses dois."

    "Faz tempo que não tenho uma amizade desse tipo. Depois que terminei o ensino médio, perdi o contato com os meus amigos de classe. Na faculdade eu só tenho um amigo na minha sala, se é que ele me vê da mesma forma."


    Raul "No final descobrimos que aquele lugar era usado por umas crianças do bairro."

    Raul "Depois a polícia mandou fechar a cabana porque alguém foi pego por um ovini."

    Ren "Sério isso?"

    Joh "Não, provavelmente era porque eles achavam que uns drogados frequentavam aquele lugar."

    Raul "Tenho que admitir que foi uma aventura e tanto."

    Joh "É, foi… Eu só me senti mal por ter mentido para a minha vó."

    Joh "No restante da semana ela não parou de falar para eu tomar cuidado e estava feliz que ela podia confiar em mim."

    Joh "A sua tia não suspeitou nada?"

    Raul "Não, eu mostrei as fotos da gente lá em casa depois."

    Joh "Nos safamos por pouco, mas aquilo foi realmente perigoso. A gente podia ter encontrado sei lá quem naquele barraco no meio do nada."

    Raul "Eu sei, eu sei. Éramos uns moleques sem noção de perigo. Apesar de que você se envolveu em mais encrenca do que eu."

    Joh "Até perdi a conta."

    "Nossa… Vai saber o que esse maluco já fez."

    Joh "Oh, Ren."

    Joh "Você não costumava visitar o Astolfo? Eu nunca te vi pela cidade."

    Ren "Eu vinha bastante com os meus pais nos feriados."

    Ren "Eram bem divertidas as viagens de carro, como dizem, a diversão está na viagem não no destino."

    Ren "Lembro que a minha mãe brincava de vermos formar nas nuvens, falar nomes de animais de A a Z e sempre que chovia e aparecia um arco-íris, ela falava que terminava na casa do tio Astolfo."

    Ren "Meu pai sempre contava aquelas piadas de paizão"

    Ren "Quando passamos na frente de uma fazenda com um monte de bpis, ele falou ‘olha lá o seu tio’."

    Ren "Não o tio Astolfo, é um outro tio."

    Joh "Bom…"

    Raul "…"

    "Senti um clima estranho se formando. Será que toquei num assunto delicado para eles? Eu não deveria ter falado sobre essa piada do meu pai."

    Joh "Acho que já está ficando tarde."

    Ren "Vamos arrumando as coisas então…"

    "Quando terminamos de arrumar a sala, levei o lixo para fora. Ouvi os dois conversando lá dentro. Ouvi as palavras 'deveria falar com…', '...melhor para você…'."

    "Eu segurei a minha curiosidade e me afastei da porta."

    "Encontrei a Alexandra na recepção mexendo no celular."

    #INT- RECEPÇÃO- DIA 3

    scene bg recep
    with fade

    Ren "Oi!"

    Ale "Oh, oi Ren. Você terminou o ensaio com o Raul e o Johnny?"

    "Por que de repente senti meu coração acelerar? Eu fiquei meio bobo sem conseguir falar. Ela não deixou passar despercebido."

    Ale "Ren?"

    Ren "Ah, é, eu só estava levando esse lixo para a caçamba…"

    Ren "E ouvi uma conversa do Raul e do Johnny."

    Ren "Eles pareciam chateados."

    Ale "Aconteceu alguma coisa? Não é normal os dois estarem assim."

    Ren "Eu sei, eu sei…tudo começou quando eu falei sobre quando eu e a minha família costumávamos visitar o tio Astolfo."

    Ren "No meio da conversa o clima ficou meio tenso, aí usei o lixo como desculpa para sair da sala."

    Ale "…"

    Ale "Você não sabe?"

    Ren "Do quê?"

    Ale "Eles…"

    Ale "..."

    Ale "Esquece."

    Ale  "É melhor esperar até eles te falarem, não é certo pressionar alguém num assunto que a pessoa considera delicado."

    Ren "…"

    Ren "Obrigado."

    #[FIM DA CENA]
