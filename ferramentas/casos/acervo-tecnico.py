"""Priorização do Acervo Técnico (repositório creasp-acervo-tecnico-bi). Indicadores da geração de 27/02/2026."""
import modelo as M

SLUG = "acervo-tecnico"


def _score():
    total, x0, larg = 270, 60, 840
    partes = [("Urgência", 150, "#F08A7E", ["Sessão vencida: 120 + 2 por dia, até 150",
                                              "Até 3 dias: 100 · 4 a 7 dias: 70",
                                              "8 a 15 dias: 40 · 16 a 30 dias: 20",
                                              "Mais de 30 dias: 10"]),
              ("Valor do edital", 80, "#FFD25E", ["A partir de R$ 50 mi: 80", "R$ 5 a 50 mi: 65", "R$ 1 a 5 mi: 50",
                                                   "R$ 300 mil a 1 mi: 35", "R$ 100 a 300 mil: 20", "Até R$ 100 mil: 10"]),
              ("Capital", 40, "#4FB3E8", ["Capital menor", "que 10% do", "edital: 40"])]
    p = ['<svg viewBox="0 0 960 300" role="img" aria-label="Composição do escore de priorização: urgência até 150, '
         'valor do edital até 80 e capital social até 40 pontos, total 270">']
    x = x0
    for nome, pts, cor, linhas in partes:
        w = larg * pts / total
        p.append(f'<rect x="{x:.1f}" y="30" width="{w - 4:.1f}" height="56" rx="8" fill="{cor}" opacity="0.9"/>')
        p.append(f'<text x="{x + 14:.1f}" y="64" fill="#162A37" font-family="Sora" font-size="15" font-weight="700">{nome}</text>')
        p.append(f'<text x="{x + w - 18:.1f}" y="64" fill="#162A37" font-family="JetBrains Mono" font-size="15" '
                 f'font-weight="700" text-anchor="end">{pts}</text>')
        for i, l in enumerate(linhas):
            p.append(f'<text x="{x + 4:.1f}" y="{118 + i * 24}" fill="#A9B8C6" font-family="Sora" font-size="13">{l}</text>')
        x += w
    p.append('<text x="60" y="290" fill="#EAF1F6" font-family="Sora" font-size="14">Escore máximo: 270 pontos. '
             'Críticos: 100 pontos ou mais, ou sessão vencida ou em até 3 dias.</text>')
    p.append("</svg>")
    return "".join(p)


CASO = dict(
    blocos=[
        ("Telas", M.telas(SLUG, [
            ("01-painel.webp", "Painel: 6 indicadores, 3 quadros de faixas e a lista de protocolos críticos ordenada pelo escore."),
            ("02-faixa-roxa.webp", "Clique na faixa Roxa (R$ 5 a 50 milhões): protocolos que seguem para aprovação manual."),
            ("03-sessoes-urgentes.webp", "Sessões urgentes: 236 vencidas e 23 em até 3 dias, com exportação para Excel."),
            ("04-graficos.webp", "Distribuição por faixa de valor e por urgência."),
            ("05-capital-social.webp", "Ranking das 381 empresas por capital social."),
        ]), "Tela reproduzida. Indicadores e faixas reais de 27/02/2026; protocolos, empresas, profissionais e órgãos com dados fictícios.", "larga"),

        ("Fluxo de páginas", M.fluxograma([
            ("Topo", [("Indicadores", "6 cartões com explicação do cálculo")], "abre o detalhe"),
            ("Quadros", [("Valor do edital", "6 faixas"), ("Prazo da sessão", "6 faixas"), ("Capital social", "7 faixas")], "clique na faixa"),
            ("Detalhe", [("Janela da faixa", "protocolos, totais, Excel"), ("Responsáveis técnicos", "histórico por empresa")]),
            ("Abas", [("Protocolos críticos", "841"), ("Perfil das empresas", "381"), ("Ranking por capital", "381"),
                      ("Gráficos", "faixas e urgência")]),
        ]), "", "larga"),

        ("Fluxo do processo", M.fluxograma([
            ("Origem", [("Banco DB2", "pedidos de certidão CAT e CAO, via JDBC")], "lê o documento do protocolo"),
            ("Edital", [("Valor e data da sessão", "extraídos do XML"), ("Duplicados", "170 editais contados uma vez")], "classifica"),
            ("Regras", [("Faixa de valor", "aprovação automática até R$ 5 mi"), ("Faixa de prazo", "vencida a mais de 30 dias"),
                        ("Capital social", "alerta abaixo de 10% do edital")], "soma"),
            ("Escore", [("0 a 270 pontos", "urgência, valor, capital")], "gera e envia"),
            ("Saída", [("Página HTML", "rotina programada, SFTP para o servidor interno")]),
        ]), "", "larga"),

        ("Escore de priorização", M.diagrama(_score(), "Pesos: urgência 55%, valor 30%, capital 15%."), "", "larga"),

        ("Pedidos por prazo", M.barras([
            ("Vencida", 236, True), ("Até 3 dias", 23), ("4 a 7 dias", 43), ("8 a 15 dias", 46),
            ("16 a 30 dias", 11), ("Mais de 30 dias", 11)],
            titulo="Protocolos com data de sessão, 27/02/2026", nota="Dias entre a geração do painel e a sessão pública da licitação.")),

        ("Achados", M.achados([
            ("1.365", "pedidos em análise: 1.234 CAT e 131 CAO"),
            ("22,2%", "têm valor de edital preenchido (303); nenhum CAO tem"),
            ("R$ 25,78 bi", "em editais, sem os 170 repetidos"),
            ("113", "pedidos acima de R$ 5 mi vão para aprovação manual"),
            ("246", "alertas de capital social menor que 10% do edital"),
            ("381", "empresas solicitantes (CNPJs distintos)"),
        ])),
    ],
    stack=["DB2", "JDBC", "Python", "pandas", "Plotly", "SFTP"],
)
