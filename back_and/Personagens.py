

class Personagem():
        def __init__(self,name,clan,vila):
            self.name:str=name
            self.clan:str =clan
            self.vila:str =vila 
            self.titulo:str
            self.descricao:dict
            self.img:str | None=None

naruto = Personagem(name="Naruto", clan="Uzumaki", vila="Konoha")
naruto.titulo="O menino da Raposa"
naruto.descricao={
    "Introducao": """Aqui está uma sugestão de texto para blog, seguindo o tema e o título que você solicitou.""",

    
    "O Menino da Raposa: A Importância de Naruto no Mangá Clássico": """Se você perguntar a qualquer fã de mangá sobre uma história de superação, é quase impossível não mencionar Naruto Uzumaki. Mas antes de se tornar o herói que conhecemos, antes de ser o centro de profecias e salvar o mundo, ele era apenas "O Menino da Raposa".

No início do mangá, conhecido como "Naruto Clássico" (antes do salto temporal), a história não é sobre um gênio talentoso ou um escolhido. É sobre um pária.

Naruto começa como um órfão barulhento, irritante e desesperado por atenção. Ele é o Jinchuuriki da Raposa de Nove Caudas (Kyuubi), a mesma besta que quase destruiu a Vila da Folha (Konoha). Por isso, ele não é visto como uma criança; ele é visto como o próprio monstro. Os adultos o desprezam e o temem, e as crianças, por reflexo, o isolam.

É nesse ponto de solidão absoluta que a verdadeira importância de Naruto Uzumaki é forjada.""",

    
    "O Pária que Queria ser Visto": """A importância de Naruto no mangá clássico não está em seu poder — na verdade, ele é academicamente um dos piores. Sua importância está em sua vontade inabalável de quebrar o ciclo de ódio.

O grande objetivo de Naruto não era, inicialmente, "salvar o mundo". Era algo muito mais humano: ser reconhecido. Ele gritava "Eu vou me tornar Hokage!" para que, finalmente, as pessoas da vila tivessem que parar de olhá-lo com desprezo e começar a olhá-lo com respeito.

Ele foi o motor da mudança. Enquanto o mundo ninja clássico era definido por regras, destino e ódio (Kakashi, Zabuza, Neji, Gaara), Naruto era a força caótica da empatia. Ele se recusava a aceitar o status quo.

Ele via um assassino cruel como Zabuza e, no fim, o fazia chorar por seu companheiro. Ele via um gênio arrogante como Neji, preso à ideia de um "destino imutável", e o derrotava para provar que o esforço pode, sim, mudar as cartas que recebemos.

A maior importância de Naruto no clássico foi sua capacidade de olhar para outros "monstros" — como Gaara do Deserto, outro Jinchuuriki consumido pela solidão e pelo ódio — e dizer: "Eu sei como você se sente".""",

    
    "Os Principais Feitos do 'Fracassado'": """Para provar seu valor, o Menino da Raposa teve que acumular feitos que ninguém esperava do "último da turma". No mangá clássico, seus maiores marcos foram:

A Batalha na Terra das Ondas (Contra Zabuza e Haku): Foi a primeira vez que Naruto provou seu lema de "não fugir e nunca voltar atrás com sua palavra". Ele também toca o coração de Haku e Zabuza, mostrando a eles um caminho além daquele de "apenas ferramentas ninjas".

A Vitória sobre Neji Hyuuga (Exame Chunin): Talvez seu feito mais importante filosoficamente. Naruto, o "fracassado", derrota Neji, o "gênio" do Clã Hyuuga. Ele não vence apenas na força, mas destrói a crença de Neji no destino, mudando a vida do Clã Hyuuga para sempre.

O Domínio do Rasengan: Enquanto Sasuke tinha o dom natural do Chidori, Naruto teve que usar de pura persistência (e seus Clones das Sombras) para dominar um Jutsu de Nível A, o Rasengan, provando ao lendário Jiraiya (e a si mesmo) que seu esforço superava sua falta de talento.

A Batalha contra Gaara (Invasão de Konoha): Este foi o momento em que Naruto se tornou, de fato, um herói para a Vila. Ele foi o único que pôde parar um Gaara transformado. Ele invocou o Chefe Sapo, Gamabunta, e o mais importante: ele salvou Gaara de si mesmo, transformando seu maior inimigo em seu primeiro e mais importante amigo.

O Confronto no Vale do Fim (Contra Sasuke): Embora tecnicamente uma "derrota" (ele não conseguiu trazer Sasuke de volta), esse feito define seu caráter. Naruto estava disposto a arriscar tudo, não para derrotar um inimigo, mas para salvar seu melhor amigo da escuridão.""",

    
    "O Legado do Clássico": """O "Naruto Clássico" não é a história de um menino que se torna o mais forte; é a história de um menino que, apesar de ter todos os motivos para odiar o mundo, escolheu amar e proteger.

O "Menino da Raposa" usou sua dor não como uma desculpa para destruir, mas como combustível para entender os outros. Ele transformou sua maior fraqueza — o monstro dentro dele — em sua maior força, e provou que a verdadeira força de um ninja está nos laços que ele cria."""

}
naruto.img ="/personagens/narutoClassico.jpeg"

sakura = Personagem(name="Sakura", clan="Haruno", vila="Konoha")
sakura.titulo="A menina do time 7"
sakura.descricao = {
    "Mais do que Apenas uma Sombra: A Evolução de Sakura Haruno no Clássico": """No meio de um Jinchuuriki com poder ilimitado e o último sobrevivente de um clã de gênios, é fácil esquecer o terceiro membro do Time 7. Sakura Haruno começa o mangá "Naruto Clássico" como a personagem com quem muitos poderiam se identificar, mas poucos admiravam: uma menina focada em sua paixão de infância por Sasuke e irritada com o protagonista barulhento, Naruto.

A importância de Sakura no clássico não vem de um poder herdado ou de um demônio selado. Pelo contrário: sua importância vem de sua *normalidade*. Ela é o ponto de vista humano, a ninja sem linhagem especial que é forçada a encarar a dura realidade de que está sendo deixada para trás.

Enquanto Naruto e Sasuke travavam batalhas que pareciam de outro nível, Sakura era o "cérebro" da equipe. Sua inteligência e seu controle de chakra impecável (reconhecido até por Kakashi) eram suas principais armas. No entanto, ela vivia à sombra de seus companheiros, uma sombra da qual ela mesma estava desesperadamente tentando sair.""",
    
   
    "Os Feitos que Definiram uma Kunoichi": """A jornada de Sakura no Clássico não é sobre vitórias esmagadoras, mas sobre *resiliência interna* e momentos de decisão que definiram seu caráter.

1.  O Corte de Cabelo (Exame Chunin - Floresta da Morte): Este é, sem dúvida, o momento definidor de Sakura no Clássico. Com Naruto e Sasuke incapacitados, ela é a única linha de defesa contra os Ninjas do Som. Percebendo que ela sempre dependeu dos outros, ela corta seu longo cabelo — um símbolo de sua vaidade e de sua antiga vida — e decide lutar. Ela não vence a luta, mas ela vence sua própria fraqueza e medo.

2.  A Luta contra Ino Yamanaka (Exame Chunin): Mais do que uma luta física, foi um confronto psicológico. Sakura enfrenta sua melhor amiga de infância e agora rival. A luta, que termina em empate, simboliza Sakura finalmente se colocando no mesmo patamar que Ino, não mais como a "testuda" insegura, mas como uma Kunoichi de Konoha.

3.  O Pedido a Tsunade (Pós-fuga de Sasuke): Após o fracasso em impedir Sasuke de deixar a vila, Sakura se encontra em seu ponto mais baixo. Ela se sente inútil por não ter feito nada além de chorar. Em vez de desistir, ela toma a decisão mais importante de sua vida: ela pede para se tornar discípula da Lendária Sannin, Tsunade.""",
    
   
    "O Legado do Clássico": """O legado de Sakura no "Naruto Clássico" não é uma lista de inimigos derrotados. É a promessa de sua própria evolução. Ela termina o arco clássico não como uma ninja completa, mas como uma pessoa que reconheceu suas falhas e deu o primeiro passo corajoso para mudar.

Ela é a prova de que força não precisa ser herdada; ela pode ser construída com pura determinação, suor e a recusa em ser deixada para trás."""
}
sakura.img ="/personagens/sakuraClassico.png"

sasuke = Personagem(name="Sasuke", clan="Uchiha", vila="Konoha")
sasuke.titulo="O ultimo Uchiha"
sasuke.descricao = {
    "O Gênio e o Vingador: O Caminho Sombrio de Sasuke Uchiha": """Se Naruto Uzumaki é o coração barulhento do mangá clássico, Sasuke Uchiha é sua contraparte sombria e silenciosa. O último sobrevivente (assim ele acreditava) do prestigiado Clã Uchiha, Sasuke não é um azarão; ele é o gênio, o prodígio e o "novato número 1" da academia.

Mas por trás de sua popularidade e talento, a importância de Sasuke no clássico é servir como um espelho trágico. Enquanto Naruto luta por reconhecimento, Sasuke luta por **vingança**.

Sua vida é definida por um único objetivo: matar seu irmão mais velho, Itachi Uchiha, que massacrou todo o seu clã. Essa motivação é o seu motor e sua prisão. No "Naruto Clássico", Sasuke é a personificação do trauma. Ele é a prova viva de que o talento e o "caminho fácil" não trazem felicidade.

Ele é forçado a confrontar uma verdade que o aterroriza: os laços que ele começa a formar com o Time 7 (Naruto, Sakura e Kakashi) o estão "enfraquecendo" e desviando-o de seu caminho de ódio. A história de Sasuke no clássico é uma tragédia; é a jornada de um menino que ativamente escolhe a escuridão em vez da luz, porque acredita que essa é a única forma de obter o poder necessário para corrigir seu passado.""",
    
    "Os Feitos que Marcaram o Vingador": """Os feitos de Sasuke no mangá clássico são uma demonstração de seu talento natural, mas também de sua queda em direção ao poder a qualquer custo.

1.  O Despertar do Sharingan (Terra das Ondas): Durante a batalha desesperada contra Haku, no espelho de gelo, o instinto de Sasuke para proteger Naruto desperta seu Kekkei Genkai. É o primeiro grande vislumbre do poder Uchiha e a primeira vez que ele coloca a vida de um companheiro acima da sua.

2.  A Marca da Maldição (Exame Chunin - Floresta da Morte): O encontro com Orochimaru muda tudo. Ao receber a Marca da Maldição, Sasuke ganha um poder imenso, mas corrupto. Essa marca se torna o símbolo de sua luta interna entre seu próprio poder e o poder "emprestado" da escuridão.

3.  O Domínio do Chidori: Como contraparte do Rasengan de Naruto, Kakashi ensina a Sasuke sua única técnica original. O Chidori representa o auge de seu poder como um ninja de Konoha — um poder focado, preciso e mortal, que ele usa efetivamente na luta contra Gaara.

4.  A Humilhação por Itachi: O breve e brutal retorno de Itachi à vila serve como o catalisador final. Sasuke usa seu Chidori, seu poder máximo, e é derrotado sem o mínimo esforço. Isso o quebra e o convence de que seus laços em Konoha o tornaram fraco.

5.  A Batalha no Vale do Fim (Contra Naruto): Este é o clímax de todo o "Naruto Clássico". Sasuke contra Naruto. Gênio contra fracassado. Ódio contra amizade. Sasuke luta para *cortar* seu último laço, ativando o estágio final de sua Marca da Maldição para derrotar Naruto. Ele vence a luta, mas escolhe não matar seu amigo — não por misericórdia, mas para obter poder de uma forma diferente da de seu irmão.""",
    
    "O Legado do Clássico": """O legado de Sasuke no clássico é a ausência. Ele é a ferida aberta que define o fim da era. Ao abandonar a vila, Sasuke não é apenas um desertor; ele é o objetivo de Naruto, a missão de resgate que irá definir toda a próxima fase da história. Ele é o amigo que foi perdido para a vingança, e o gênio que provou que o poder sozinho não preenche o vazio."""
}
sasuke.img ="/personagens/SasukeClassico.jpg"

kakashi = Personagem(name="Kakashi", clan="Hatake", vila="Konoha")
kakashi.titulo="O ninja de mil justsus"
kakashi.descricao = {
    "O Sensei Misterioso: O Fardo de Kakashi Hatake": """Kakashi Hatake é introduzido no "Naruto Clássico" como a figura mais enigmática e, indiscutivelmente, "cool" de Konoha. O Jounin de elite com o cabelo prateado, a máscara cobrindo o rosto e o Sharingan (o olho de outro) sempre escondido pela bandana.

Ele é o sensei do Time 7, conhecido por seu hábito crônico de se atrasar e seu gosto por romances duvidosos. Mas essa fachada relaxada esconde um passado trágico e um gênio tático.

A importância de Kakashi no Clássico é dupla: ele é o mentor que deve guiar os três protagonistas e o guardião que tenta desesperadamente impedir que a história trágica do mundo ninja se repita em seus alunos. Ele é um homem quebrado por seu passado (a morte de Obito, Rin e seu mestre Minato), e sua filosofia é um reflexo direto de suas falhas. Sua obsessão por "trabalho em equipe" é sua tentativa de redimir seus próprios erros.""",
    
    "Os Feitos do 'Ninja que Copia'": """Kakashi é o primeiro a mostrar ao leitor o que é um Jounin de verdade. Seus feitos no Clássico estabelecem o nível de poder e a complexidade das batalhas ninja.

1.  O Teste dos Sinos (Sua Verdadeira Missão): O feito mais importante de Kakashi não é uma luta, mas uma lição. Ao forçar Naruto, Sasuke e Sakura a trabalharem juntos para conseguir os sinos, ele ensina sua regra de vida, forjada em sua tragédia pessoal: "No mundo ninja, aqueles que quebram as regras são lixo. Mas aqueles que abandonam seus companheiros são piores que lixo." Ele foi o único professor que entendeu que o Time 7 precisava dessa lição acima de qualquer outra.

2.  A Batalha contra Zabuza Momochi: Na Terra das Ondas, vemos o "Ninja Copiador" em ação pela primeira vez. Ele revela seu Sharingan, copiando o Jutsu de Prisão de Água de Zabuza em tempo real e, mais tarde, soltando um arsenal de técnicas. A luta estabelece Kakashi como um combatente de nível mundial e um estrategista brilhante.

3.  O Selamento da Marca da Maldição: Durante o ataque de Orochimaru na Floresta da Morte, Kakashi confronta o Lendário Sannin. Ele não consegue vencê-lo, mas consegue realizar um feito crucial: usar o "Selo de Supressão do Mal" para conter a Marca da Maldição em Sasuke, adiando sua queda para a escuridão e mostrando seu profundo (e temeroso) conhecimento de Orochimaru.

4.  Ensinando o Chidori a Sasuke: Vendo a escuridão em Sasuke e sua rivalidade com Naruto, Kakashi toma uma decisão difícil: ele ensina a Sasuke sua única técnica original, o Chidori. Ele o faz na esperança de dar a Sasuke o poder necessário para proteger seus amigos e se afastar da vingança.

5.  A Derrota para Itachi Uchiha: O retorno de Itachi a Konoha nos dá uma medida do poder de Kakashi. Ele corajosamente enfrenta o gênio Uchiha para proteger Sasuke e Kurenai, mas é pego no Tsukuyomi. Sua derrota absoluta e a tortura mental que sofre mostram a diferença de nível entre o "Ninja Copiador" e um verdadeiro mestre do Mangekyou Sharingan.""",
    
    "O Legado do Clássico": """O legado de Kakashi no "Naruto Clássico" é, em muitos aspectos, um fracasso que alimenta sua determinação futura. Apesar de seus melhores esforços, ele não consegue salvar Sasuke da escuridão, assim como não conseguiu salvar Obito no passado. O Time 7 se despedaça. Ele termina o Clássico não como um herói vitorioso, mas como um mentor que falhou em sua lição mais importante, preparando o terreno para sua jornada de redenção no Shippuden."""
}
kakashi.img="/personagens/kakashiClassico.jpg"

listPersonas:list[Personagem]=[naruto,sakura,sasuke,kakashi]
