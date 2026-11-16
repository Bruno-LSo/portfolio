"""Painel da COVID-19 (repositório público Bruno-LSo/DashCovid19)."""
import modelo as M

SLUG = "covid"

_SVG = (
    '<svg viewBox="0 0 960 300" role="img" aria-label="Fluxo de dados e interação do painel">'
    '<defs><marker id="covid-s" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
    '<path d="M0 0 L10 5 L0 10z" fill="#4FD1D4"/></marker></defs>'
    # linha de cima: preparação
    '<rect x="10" y="20" width="200" height="70" rx="10" fill="#162A37" stroke="#4FB3E8"/>'
    '<text x="110" y="50" fill="#EAF1F6" font-family="Sora" font-size="14" text-anchor="middle">CSV do Ministério</text>'
    '<text x="110" y="72" fill="#A9B8C6" font-family="Sora" font-size="13" text-anchor="middle">HIST_PAINEL_COVIDBR</text>'
    '<path d="M210 55 H268" stroke="#4FD1D4" stroke-width="2" marker-end="url(#covid-s)"/>'
    '<rect x="270" y="20" width="200" height="70" rx="10" fill="#162A37" stroke="#4FD1D4"/>'
    '<text x="370" y="50" fill="#EAF1F6" font-family="Sora" font-size="14" text-anchor="middle">imports.py</text>'
    '<text x="370" y="72" fill="#A9B8C6" font-family="Sora" font-size="13" text-anchor="middle">junta, limpa, separa</text>'
    '<path d="M470 55 H528" stroke="#4FD1D4" stroke-width="2" marker-end="url(#covid-s)"/>'
    '<rect x="530" y="20" width="200" height="70" rx="10" fill="#162A37" stroke="#4FD1D4"/>'
    '<text x="630" y="50" fill="#EAF1F6" font-family="Sora" font-size="14" text-anchor="middle">df_states.csv</text>'
    '<text x="630" y="72" fill="#A9B8C6" font-family="JetBrains Mono" font-size="13" text-anchor="middle">50.949 linhas</text>'
    '<rect x="750" y="20" width="200" height="70" rx="10" fill="#162A37" stroke="#4FD1D4"/>'
    '<text x="850" y="50" fill="#EAF1F6" font-family="Sora" font-size="14" text-anchor="middle">df_brasil.csv</text>'
    '<text x="850" y="72" fill="#A9B8C6" font-family="JetBrains Mono" font-size="13" text-anchor="middle">1.887 dias</text>'
    '<path d="M740 90 V140 H480" stroke="#4FD1D4" stroke-width="2" fill="none" marker-end="url(#covid-s)"/>'
    # linha de baixo: interação
    '<rect x="270" y="120" width="200" height="70" rx="10" fill="#162A37" stroke="#5CC98A"/>'
    '<text x="370" y="150" fill="#EAF1F6" font-family="Sora" font-size="14" text-anchor="middle">dashboard.py</text>'
    '<text x="370" y="172" fill="#A9B8C6" font-family="Sora" font-size="13" text-anchor="middle">Dash, 6 callbacks</text>'
    '<path d="M370 190 V215" stroke="#4FD1D4" stroke-width="2" marker-end="url(#covid-s)"/>'
    '<rect x="10" y="220" width="170" height="64" rx="10" fill="#162A37" stroke="#FFD25E"/>'
    '<text x="95" y="248" fill="#EAF1F6" font-family="Sora" font-size="14" text-anchor="middle">Clique no mapa</text>'
    '<text x="95" y="268" fill="#A9B8C6" font-family="Sora" font-size="13" text-anchor="middle">escolhe a UF</text>'
    '<rect x="200" y="220" width="170" height="64" rx="10" fill="#162A37" stroke="#FFD25E"/>'
    '<text x="285" y="248" fill="#EAF1F6" font-family="Sora" font-size="14" text-anchor="middle">Ano e data</text>'
    '<text x="285" y="268" fill="#A9B8C6" font-family="Sora" font-size="13" text-anchor="middle">limitam o período</text>'
    '<rect x="390" y="220" width="170" height="64" rx="10" fill="#162A37" stroke="#FFD25E"/>'
    '<text x="475" y="248" fill="#EAF1F6" font-family="Sora" font-size="14" text-anchor="middle">Indicador</text>'
    '<text x="475" y="268" fill="#A9B8C6" font-family="Sora" font-size="13" text-anchor="middle">casos ou óbitos</text>'
    '<path d="M560 252 H598" stroke="#4FD1D4" stroke-width="2" marker-end="url(#covid-s)"/>'
    '<rect x="600" y="210" width="350" height="84" rx="10" fill="#162A37" stroke="#F08A7E"/>'
    '<text x="775" y="240" fill="#EAF1F6" font-family="Sora" font-size="14" text-anchor="middle">Atualiza cartões, série e mapa</text>'
    '<text x="775" y="262" fill="#A9B8C6" font-family="Sora" font-size="13" text-anchor="middle">e a comparação entre dois estados</text>'
    '<text x="775" y="282" fill="#A9B8C6" font-family="Sora" font-size="13" text-anchor="middle">com picos diário e mensal</text>'
    '</svg>')

CASO = dict(
    lead="Painel interativo com a evolução da COVID-19 no Brasil e nos 27 estados, de fevereiro de 2020 a abril de 2025, a partir do arquivo público do Ministério da Saúde.",
    blocos=[
        ("Telas", M.telas(SLUG, [
            ("01-visao-geral.webp", "Tela inicial: cartões do Brasil na última data, filtro de ano e de data e mapa por UF."),
            ("02-serie-e-comparacao.webp", "Série diária de casos novos e comparação entre dois estados, com picos diário e mensal."),
            ("03-estado-e-ano.webp", "São Paulo escolhido no mapa, ano de 2021 e indicador de óbitos por dia."),
        ]), "Capturas do painel rodando com os dados públicos do repositório.", "larga"),
        ("Fluxo de uso", M.fluxograma([
            ("Entrada", [("Página única", "controles à esquerda, mapa à direita")]),
            ("Filtros", [("Local", "Brasil ou UF clicada no mapa"), ("Ano", "um ou mais, de 2020 a 2025"), ("Data", "dia exato dos cartões e do mapa")], "atualizam"),
            ("Resultados", [("Cartões", "casos, óbitos, recuperados, em acompanhamento"), ("Série", "casos ou óbitos, acumulado ou por dia"),
                            ("Mapa", "casos acumulados por UF"), ("Comparação", "dois estados e seus picos")]),
        ]), "", "larga"),
        ("Dados e processamento", M.diagrama(_SVG, "O script de importação separa as linhas de estado e de Brasil; o painel lê os dois CSV e responde aos filtros."), "", "larga"),
        ("Casos novos por ano", M.painel("", '<div id="g-covid"></div>', "2025 até 25 de abril.")),
        ("Achados", M.achados([
            ("298.408", "casos novos em 3/2/2022, maior valor diário no Brasil"),
            ("4.249", "óbitos em 8/4/2021, maior valor diário no Brasil"),
            ("424.107", "óbitos em 2021, 59% dos 716.029 da série"),
            ("455.305", "casos em São Paulo em 06/2021, maior mês do estado"),
        ])),
        ("Óbitos por ano", M.barras([("2020", 194949), ("2021", 424107, True), ("2022", 74801), ("2023", 15067),
                                     ("2024", 5959), ("2025", 1558)], titulo="Óbitos novos por ano, Brasil", nota="2025 até 25 de abril.")),
        ("Funcionalidades", M.lista([
            ("Mapa", "Mapa coroplético por UF; o clique troca o local de todos os gráficos."),
            ("Período", "Filtro de um ou mais anos e seletor de data em formato DD/MM/AAAA."),
            ("Indicadores", "Casos acumulados, casos novos, óbitos totais e óbitos por dia."),
            ("Comparação", "Dois estados lado a lado, com o dia e o mês de maior número de casos."),
        ])),
    ],
)
