import modelo as M

SLUG = "advinhae"

_seta = ('<defs><marker id="adv-s" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
         '<path d="M0 0 L10 5 L0 10z" fill="#4FD1D4"/></marker></defs>')


def _caixa(x, y, w, titulo, sub, cor="#4FD1D4"):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="64" rx="10" fill="#162A37" stroke="{cor}"/>'
            f'<text x="{x + w / 2}" y="{y + 28}" fill="#EAF1F6" font-family="Sora" font-size="14" text-anchor="middle">{titulo}</text>'
            f'<text x="{x + w / 2}" y="{y + 48}" fill="#A9B8C6" font-family="Sora" font-size="13" text-anchor="middle">{sub}</text>')


def _linha(x1, y1, x2, y2):
    return f'<path d="M{x1} {y1} L{x2} {y2}" stroke="#4FD1D4" stroke-width="2" fill="none" marker-end="url(#adv-s)"/>'


_svg = ('<svg viewBox="0 0 960 300" role="img" aria-label="Ciclo de atualização dos jogos e da pontuação">' + _seta
        + _caixa(10, 30, 170, "TheSportsDB", "ligas, times, jogos", "#4FB3E8")
        + _caixa(230, 30, 200, "sync-esportes", "cron a cada 5 min")
        + _caixa(480, 30, 200, "partidas", "horário em UTC")
        + _caixa(730, 30, 220, "fn_pontuar_partida", "20 / 10 / 0 e 2 / 1 / 0", "#5CC98A")
        + _caixa(730, 200, 220, "vw_ranking", "pontos e placares exatos", "#5CC98A")
        + _caixa(480, 200, 200, "E-mail de ranking", "Resend, com opt-out", "#FFD25E")
        + _caixa(230, 200, 200, "Site", "Realtime: aviso de intra", "#FFD25E")
        + _linha(180, 62, 228, 62) + _linha(430, 62, 478, 62) + _linha(680, 62, 728, 62)
        + _linha(840, 94, 840, 198) + _linha(730, 232, 682, 232) + _linha(480, 232, 432, 232)
        + '<text x="705" y="150" fill="#A9B8C6" font-family="Sora" font-size="13" text-anchor="middle">jogo encerrado</text>'
        + '</svg>')

CASO = dict(
    blocos=[
        ("Telas", M.telas(SLUG, [
            ("01-inicio.webp", "Página inicial: regra de pontuação e chamada para criar o bolão."),
            ("02-meus-boloes.webp", "Meus bolões: tipo, valor de entrada e prazo de adesão de cada bolão."),
            ("03-criar-esporte.webp", "Criar bolão, passo 1 de 5: só aparecem esportes com jogos marcados."),
            ("04-criar-premios.webp", "Passo 3 de 5: bolão clássico com percentuais do pote para 1º, 2º e 3º lugar."),
            ("05-jogos.webp", "Aba Jogos: placar ao vivo, jogo travado e palpite aberto com contagem até a trava."),
            ("06-palpites-galera.webp", "Palpites dos outros participantes, visíveis só depois que o jogo trava."),
            ("07-chaves.webp", "Aba Chaves: confrontos por rodada até a final."),
            ("08-ranking.webp", "Aba Ranking: pote, empates e prêmio de cada posição."),
            ("09-intra.webp", "Aba Intra: apostas durante o jogo, em duas janelas."),
        ]), "Telas reproduzidas a partir do código do site, com o banco trocado por dados fictícios. Dados fictícios.", "larga"),
        ("Fluxo de páginas", M.fluxograma([
            ("Entrada", [("Página inicial", "regra de pontuação"), ("Convite", "link com o código do bolão")]),
            ("Acesso", [("Entrar", "e-mail e senha ou Google"), ("Apelido", "confirmado no 1º acesso")], "login"),
            ("Painel", [("Meus bolões", "cartões por bolão"), ("Criar bolão", "5 passos"), ("Configurações", "apelido, chave Pix, e-mail de ranking")]),
            ("Bolão", [("Jogos", "palpite por partida"), ("Chaves", "mata-mata"), ("Ranking", "pontos e prêmios"),
                       ("Intra", "apostas ao vivo"), ("Convidar", "e-mail ou link"), ("Regras", "pontuação e prazos")], "abas"),
        ]), "O site é uma página única. A rota fica no endereço (#/painel, #/criar, #/bolao/código).", "larga"),
        ("Criar um bolão", M.fluxo([
            ("1", "Esporte", "7 esportes; só os que têm jogos agendados ficam ativos."),
            ("2", "Campeonato", "Lista de campeonatos com número de jogos e data do primeiro."),
            ("3", "Formato", "Clássico (1º, 2º e 3º) ou campeão leva tudo (100%)."),
            ("4", "Valor e intra", "Entrada por pessoa (0 para jogar sem dinheiro) e intra ligado ou não."),
            ("5", "Nome e prazo", "Prazo de adesão antes do primeiro jogo, no fuso de quem cria."),
        ])),
        ("Demonstração", M.painel("pontuação", '<div class="controles"><div class="campo"><label for="pa">Palpite, mandante <output id="pa-o">2</output></label><input id="pa" type="range" min="0" max="6" value="2"></div><div class="campo"><label for="pb">Palpite, visitante <output id="pb-o">1</output></label><input id="pb" type="range" min="0" max="6" value="1"></div><div class="campo"><label for="ra">Resultado, mandante <output id="ra-o">2</output></label><input id="ra" type="range" min="0" max="6" value="2"></div><div class="campo"><label for="rb">Resultado, visitante <output id="rb-o">0</output></label><input id="rb" type="range" min="0" max="6" value="0"></div></div><div class="kpi" style="margin-top:16px"><strong class="num" id="pts">10</strong><span id="pts-t" role="status">pontos</span></div>'), "Placar exato vale 20 pontos; acertar o vencedor ou o empate vale 10."),
        ("Regras no banco", M.lista([
            ("Trava do palpite", "Um gatilho recusa palpite feito a menos de 10 minutos do início do jogo."),
            ("Mata-mata", "Partida sem empate recusa palpite empatado."),
            ("Palpite dos outros", "Regra de acesso por linha: o palpite alheio só aparece depois da trava."),
            ("Prêmios", "Soma dos percentuais igual a 100 e 1º lugar sempre com a maior parte."),
            ("Empate no ranking", "Desempate por placares exatos; posições empatadas dividem o prêmio."),
            ("Auditoria", "Login, palpite, criação de bolão e pontuação ficam em logs_auditoria."),
        ])),
        ("Intra bolão", M.lista([
            ("Duas janelas", "Começo do jogo (0 a 20 min) e reta final (no futebol, 85 a 110 min de relógio)."),
            ("Pontos", "Placar exato 2, vencedor 1. Um décimo da pontuação normal."),
            ("Valor", "Aposta própria por janela, separada da entrada do bolão."),
            ("Aviso", "Realtime avisa quem está no site; uma função envia e-mail aos membros."),
            ("Ranking", "O criador decide se o intra soma no ranking geral ou corre em paralelo."),
        ])),
        ("Atualização dos jogos", M.diagrama(_svg, "A cada 5 minutos a função busca jogos e placares, pontua as partidas encerradas e envia o ranking por e-mail."), "", "larga"),
    ],
)
