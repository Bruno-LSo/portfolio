"""Caso detalhado: GXxT (repositório alien-crue)."""
import modelo as M

SLUG = "alien-crue"

ARQ = '''<svg viewBox="0 0 960 330" role="img" aria-label="Arquitetura do GXxT: cliente, servidor de jogo e banco">
<defs><marker id="gx-seta" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10z" fill="#4FD1D4"/></marker></defs>
<g font-family="Sora" text-anchor="middle">
<rect x="20" y="40" width="250" height="250" rx="12" fill="#162A37" stroke="#4FB3E8"/>
<text x="145" y="70" fill="#EAF1F6" font-size="16">Cliente (navegador ou app)</text>
<text x="145" y="100" fill="#A9B8C6" font-size="13">Vite, Three.js, PixiJS</text>
<text x="145" y="124" fill="#A9B8C6" font-size="13">Capacitor (Android e iOS)</text>
<text x="145" y="160" fill="#EAF1F6" font-size="13">envia: movimento, ataque,</text>
<text x="145" y="180" fill="#EAF1F6" font-size="13">habilidade, construção, chat</text>
<text x="145" y="216" fill="#EAF1F6" font-size="13">interpola a cena</text>
<text x="145" y="236" fill="#A9B8C6" font-size="13">atraso de 100 ms</text>
<text x="145" y="268" fill="#A9B8C6" font-size="13">mapa em blocos de ruas</text>
<rect x="355" y="40" width="250" height="250" rx="12" fill="#162A37" stroke="#4FD1D4"/>
<text x="480" y="70" fill="#EAF1F6" font-size="16">Servidor de jogo (Node.js)</text>
<text x="480" y="100" fill="#A9B8C6" font-size="13">autoritativo</text>
<text x="480" y="136" fill="#EAF1F6" font-size="13">simulação a 20 ciclos/s</text>
<text x="480" y="160" fill="#EAF1F6" font-size="13">dano, recarga, furtividade</text>
<text x="480" y="184" fill="#EAF1F6" font-size="13">criaturas por hora solar</text>
<text x="480" y="208" fill="#EAF1F6" font-size="13">blocos de 512 m (chunks)</text>
<text x="480" y="244" fill="#A9B8C6" font-size="13">só envia o que está a</text>
<text x="480" y="264" fill="#A9B8C6" font-size="13">2 chunks do jogador</text>
<rect x="690" y="40" width="250" height="250" rx="12" fill="#162A37" stroke="#5CC98A"/>
<text x="815" y="70" fill="#EAF1F6" font-size="16">Supabase (PostgreSQL)</text>
<text x="815" y="100" fill="#A9B8C6" font-size="13">login Google ou e-mail</text>
<text x="815" y="136" fill="#EAF1F6" font-size="13">perfis e personagens</text>
<text x="815" y="160" fill="#EAF1F6" font-size="13">construções do mundo</text>
<text x="815" y="184" fill="#EAF1F6" font-size="13">gangues e relações</text>
<text x="815" y="208" fill="#EAF1F6" font-size="13">livro de moedas</text>
<text x="815" y="232" fill="#EAF1F6" font-size="13">mercado e compras</text>
<text x="815" y="268" fill="#A9B8C6" font-size="13">10 tabelas</text>
<path d="M272 140 H352" stroke="#4FD1D4" stroke-width="2" marker-end="url(#gx-seta)"/>
<text x="312" y="130" fill="#FFD25E" font-size="13">ações</text>
<path d="M352 200 H272" stroke="#4FD1D4" stroke-width="2" marker-end="url(#gx-seta)"/>
<text x="312" y="222" fill="#FFD25E" font-size="13">10 por s</text>
<text x="312" y="320" fill="#A9B8C6" font-size="13">WebSocket</text>
<path d="M607 165 H687" stroke="#4FD1D4" stroke-width="2" marker-end="url(#gx-seta)" marker-start="url(#gx-seta)"/>
<text x="647" y="155" fill="#FFD25E" font-size="13">grava</text>
</g></svg>'''

CASO = dict(
    lead="Jogo online em tempo real sobre o mapa do mundo. O jogador escolhe um dos 8 tipos de fantasma, coleta recursos, constrói e disputa território. Dia e noite seguem a posição do sol no ponto do mapa onde o personagem está.",
    ficha=[("Tipo", "Produto próprio, em desenvolvimento"), ("Plataforma", "Navegador, com empacotamento para celular"),
           ("Servidor", "Autoritativo, WebSocket"), ("Monetização", "Somente itens visuais")],
    numeros=[("8", "tipos de fantasma"), ("24", "habilidades"), ("200", "níveis"), ("10", "tabelas no banco")],
    blocos=[
        ("Telas", M.telas(SLUG, [
            ("01-entrada.webp", "Entrada: login com Google ou e-mail e senha. Dados fictícios."),
            ("02-fantasma.webp", "Escolha do fantasma: 8 tipos com atributos, passiva, 3 habilidades e a árvore de 6 níveis. Dados fictícios."),
            ("03-jogo.webp", "Partida: vida, essência, moedas, barra de habilidades e de ações, chat e o cone de visão de uma criatura. Dados fictícios."),
            ("04-loja.webp", "Loja: só aparência e pacotes de moeda. Dados fictícios."),
            ("05-configuracoes.webp", "Configurações: som, auto-ataque, localização e 19 teclas. Dados fictícios."),
        ]), "Telas reproduzidas a partir do código do cliente (HTML e CSS do jogo, mesmos textos). O mapa de fundo é desenhado; no jogo ele vem de blocos de ruas reais em 3D.", "larga"),
        ("Fluxo do jogador", M.fluxograma([
            ("Entrada", [("Login", "Google ou e-mail")], "personagem novo"),
            ("Criação", [("Nome da sombra", "mínimo 3 letras"), ("Tipo de fantasma", "8 opções")], "conecta ao servidor"),
            ("Partida", [("Explorar", "mover, correr, esgueirar"), ("Combater", "ataque, overwatch, 3 habilidades"),
                         ("Coletar", "sucata, resina, cristal"), ("Construir", "6 tipos de bloco")]),
            ("Janelas", [("Equipe", "até 3 companheiros"), ("Loja", "aparência e moedas"), ("AdNexus", "recompensa por anúncio"), ("Configurações", "salvas no perfil")]),
        ], "As configurações e as teclas ficam no perfil do jogador e seguem para qualquer aparelho."), "", "larga"),
        ("Funcionalidades", M.lista([
            ("Mapa do mundo", "Blocos de ruas reais desenhados em 3D. 1 unidade do jogo vale cerca de 1 metro."),
            ("Ciclo solar", "Dia e noite pela elevação do sol na longitude e latitude do personagem. Criaturas têm período ativo: dia, noite ou sempre."),
            ("Sintonia Terrena", "Opcional. Até 5 km da localização real do jogador, todos os atributos sobem 7%."),
            ("Furtividade e overwatch", "Esgueirar reduz a velocidade a 45%. Criaturas veem num cone de cerca de 110 graus. Em overwatch, o primeiro tiro de reação causa 1,5 vez o dano."),
            ("Progressão longa", "Nível máximo 200 com curva cúbica. Habilidades sobem por uso até 130."),
            ("Construção", "6 blocos (muros, portão, seteira, chão de espinhos), gravados para todos os jogadores."),
            ("Economia", "Moeda Plasma Coin. Taxa de 2% no mercado e perda de 10% das moedas carregadas ao morrer. Toda transação vai para um livro de registro."),
        ])),
        ("Os 8 fantasmas", M.barras([
            ("Cinza (vitalidade)", 18, True), ("Eco (intelecto)", 18),
            ("Véu (furtividade)", 14), ("Vigília (vitalidade)", 15),
            ("Estático (intelecto)", 14), ("Lamento (furtividade)", 14),
            ("Fuligem (agilidade)", 14), ("Marcha (intelecto)", 14),
        ], titulo="Atributo mais alto de cada tipo (os 5 atributos somam 56 em todos)",
            nota="Valores de packages/shared/src/ghosts.ts, races.ts e classes.ts."), "Soldado, operadora de rádio, espião, enfermeira, eletricista, viúva, criança das minas e general. Cada tipo tem passiva, 3 habilidades (níveis 8, 45 e 160) e árvore de 6 níveis."),
        ("Arquitetura", M.diagrama(ARQ, "O servidor decide dano, recarga e posição e envia o estado 10 vezes por segundo. O cliente só desenha e interpola."), "", "larga"),
        ("Situação", M.achados([("7 de 16", "itens do roteiro concluídos: identidade, fantasmas, progressão, mapa, ciclo solar, habilidades e hordas"),
                                ("9", "itens pendentes, entre eles equipamento, missões, gangues 2.0 e monetização"),
                                ("4", "pacotes de moeda, de US$ 4,99 a US$ 49,99")])),
    ],
    stack=["TypeScript", "Three.js", "PixiJS", "WebSocket", "Node.js", "Supabase", "Vite", "Capacitor"],
)
