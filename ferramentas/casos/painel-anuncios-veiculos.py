"""Análise exploratória de anúncios de veículos e aplicativo web em Streamlit. Bootcamp TripleTen, Sprint 5.
Fonte: github.com/Bruno-LSo/vehicles_us_TripleTen (público): app.py, notebooks/EDA.ipynb, vehicles_us.csv.
Telas: app.py rodado localmente (só lê o CSV) e capturado com Playwright.
Números: calculados sobre o vehicles_us.csv do repositório."""
import modelo as M

SLUG = "painel-anuncios-veiculos"

_ARQ = '''<svg viewBox="0 0 960 220" role="img" aria-label="Caminho do dado até o gráfico no aplicativo">
<defs><marker id="veic-seta" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10z" fill="#4FD1D4"/></marker></defs>
<rect x="10" y="60" width="190" height="90" rx="12" fill="#162A37" stroke="#4FD1D4"/>
<text x="105" y="98" fill="#EAF1F6" font-family="Sora" font-size="14" text-anchor="middle">vehicles_us.csv</text>
<text x="105" y="124" fill="#A9B8C6" font-family="JetBrains Mono" font-size="13" text-anchor="middle">51.525 anúncios</text>
<path d="M200 105 H250" stroke="#4FD1D4" stroke-width="2" marker-end="url(#veic-seta)"/>
<rect x="250" y="60" width="190" height="90" rx="12" fill="#162A37" stroke="#4FB3E8"/>
<text x="345" y="98" fill="#EAF1F6" font-family="Sora" font-size="14" text-anchor="middle">pandas</text>
<text x="345" y="124" fill="#A9B8C6" font-family="Sora" font-size="13" text-anchor="middle">leitura na abertura</text>
<path d="M440 105 H490" stroke="#4FD1D4" stroke-width="2" marker-end="url(#veic-seta)"/>
<rect x="490" y="60" width="200" height="90" rx="12" fill="#162A37" stroke="#FFD25E"/>
<text x="590" y="98" fill="#EAF1F6" font-family="Sora" font-size="14" text-anchor="middle">Streamlit</text>
<text x="590" y="124" fill="#A9B8C6" font-family="Sora" font-size="13" text-anchor="middle">botão, caixas, seletores</text>
<path d="M690 105 H740" stroke="#4FD1D4" stroke-width="2" marker-end="url(#veic-seta)"/>
<rect x="740" y="60" width="200" height="90" rx="12" fill="#162A37" stroke="#F08A7E"/>
<text x="840" y="98" fill="#EAF1F6" font-family="Sora" font-size="14" text-anchor="middle">Plotly Express</text>
<text x="840" y="124" fill="#A9B8C6" font-family="Sora" font-size="13" text-anchor="middle">gráfico interativo</text>
<text x="10" y="195" fill="#A9B8C6" font-family="Sora" font-size="13">Publicado no Render como serviço web. O arquivo de configuração fixa a porta 10000 e o modo sem janela.</text>
</svg>'''

CASO = dict(
    nome="Painel de anúncios de veículos",
    resumo="Aplicativo web que gera histogramas e gráficos de dispersão de 51.525 anúncios de carros usados.",
    tec="Python · Streamlit · Plotly · pandas",
    area="modelos",
    lead="Aplicativo web para explorar uma base de 51.525 anúncios de carros usados nos Estados Unidos. "
         "A pessoa escolhe a coluna e o aplicativo desenha o histograma ou o gráfico de dispersão.",
    ficha=[("Contexto", "Bootcamp de Ciência de Dados, TripleTen"), ("Dados", "51.525 anúncios, 13 colunas, maio/2018 a abril/2019"),
           ("Aplicativo", "Streamlit publicado no Render"), ("Código", '<a href="https://github.com/Bruno-LSo/vehicles_us_TripleTen">github.com/Bruno-LSo/vehicles_us_TripleTen</a>')],
    numeros=[("51.525", "anúncios de carros usados"), ("13", "colunas: preço, ano, modelo, estado, quilometragem e outras"),
             ("US$ 9.000", "preço mediano dos anúncios"), ("3", "gráficos no aplicativo: 2 histogramas e 1 dispersão")],
    blocos=[
        ("Telas", M.telas(SLUG, [
            ("02-histograma.webp", "Botão \"Criar histograma\": distribuição da quilometragem (odometer)."),
            ("03-histograma-coluna.webp", "Caixa de seleção e escolha da coluna: histograma do ano do modelo."),
            ("04-dispersao.webp", "Gráfico de dispersão com eixos escolhidos: quilometragem contra preço.")]),
         "Aplicativo do repositório rodado localmente, com a base pública do projeto.", "larga"),
        ("Fluxo da tela", M.fluxograma([
            ("Entrada", ["Página única"]),
            ("Controles", [("Botão", "histograma da quilometragem"), ("Caixa 1", "histograma de qualquer coluna"), ("Caixa 2", "dispersão entre duas colunas")], "escolha"),
            ("Seleção", [("Coluna", "1 das 13"), ("Eixo X e eixo Y", "2 das 13")], "desenha"),
            ("Saída", [("Gráfico Plotly", "zoom, filtro e download em PNG")]),
        ]), "", "larga"),
        ("Arquitetura", M.diagrama(_ARQ, "Um arquivo Python de 57 linhas, sem banco de dados."), "", "larga"),
        ("Dados", M.lista([
            ("Colunas", "preço, ano do modelo, modelo, estado, cilindros, combustível, quilometragem, câmbio, tipo, cor, tração 4x4, data e dias no ar."),
            ("Período", "Anúncios publicados de 01/05/2018 a 19/04/2019."),
            ("Ausentes", "tração 4x4 em 25.953 linhas, cor em 9.267, quilometragem em 7.892, cilindros em 5.260 e ano em 3.619."),
            ("Tipos", "SUV (12.405), caminhonete truck (12.353) e sedã (12.154) somam 71,6% dos anúncios.")])),
        ("Preço mediano por estado do carro", M.barras(
            [("Novo", 21999, True), ("Como novo", 13995), ("Excelente", 10495), ("Bom", 7900), ("Razoável", 2500), ("Sucata", 2500)],
            titulo="Preço mediano em US$", nota="Calculado sobre o vehicles_us.csv do repositório. Novo: 143 anúncios; excelente: 24.773.")),
        ("Achados", M.achados([
            ("0,59", "correlação de Spearman entre preço e ano do modelo: carro mais novo, preço maior."),
            ("−0,48", "correlação de Spearman entre preço e quilometragem."),
            ("0,00", "correlação entre preço e dias no ar: o preço não muda o tempo do anúncio."),
            ("990.000", "milhas é a maior quilometragem. Valores extremos pedem limpeza antes de modelar.")])),
        ("Limites", M.lista([
            ("Exploração", "O aplicativo mostra a base sem limpeza. Valores ausentes e extremos entram nos gráficos."),
            ("Sem modelo", "O projeto não estima preço. É uma etapa de análise e publicação."),
            ("Hospedagem", "O endereço no Render não respondeu na conferência de 16/11/2026.")])),
    ],
    stack=["Python", "pandas", "Streamlit", "Plotly Express", "Render", "Git"],
    link=("Ver o código", "https://github.com/Bruno-LSo/vehicles_us_TripleTen"),
)
