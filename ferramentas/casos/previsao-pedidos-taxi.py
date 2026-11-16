"""Previsão de pedidos de táxi por hora (série temporal). Bootcamp TripleTen, Sprint 13.
Fonte: Sprint_13/Series_Temporais.ipynb (repositório privado; sem link)."""
import modelo as M

SLUG = "previsao-pedidos-taxi"

_DIAGRAMA = '''<svg viewBox="0 0 960 300" role="img" aria-label="Montagem das variáveis a partir da série horária">
<defs><marker id="taxi-seta" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10z" fill="#4FD1D4"/></marker></defs>
<rect x="20" y="110" width="190" height="80" rx="12" fill="#162A37" stroke="#4FD1D4"/>
<text x="115" y="143" fill="#EAF1F6" font-family="Sora" font-size="15" text-anchor="middle">Pedidos por hora</text>
<text x="115" y="168" fill="#A9B8C6" font-family="JetBrains Mono" font-size="13" text-anchor="middle">4.416 horas</text>
<path d="M210 150 C260 150 260 50 330 50" stroke="#4FD1D4" stroke-width="2" fill="none" marker-end="url(#taxi-seta)"/>
<path d="M210 150 H330" stroke="#4FD1D4" stroke-width="2" marker-end="url(#taxi-seta)"/>
<path d="M210 150 C260 150 260 250 330 250" stroke="#4FD1D4" stroke-width="2" fill="none" marker-end="url(#taxi-seta)"/>
<rect x="330" y="15" width="290" height="70" rx="12" fill="#162A37" stroke="#4FB3E8"/>
<text x="475" y="44" fill="#EAF1F6" font-family="Sora" font-size="14" text-anchor="middle">Calendário</text>
<text x="475" y="68" fill="#A9B8C6" font-family="Sora" font-size="13" text-anchor="middle">ano, mês, dia, dia da semana (4)</text>
<rect x="330" y="115" width="290" height="70" rx="12" fill="#162A37" stroke="#FFD25E"/>
<text x="475" y="144" fill="#EAF1F6" font-family="Sora" font-size="14" text-anchor="middle">Defasagens</text>
<text x="475" y="168" fill="#A9B8C6" font-family="Sora" font-size="13" text-anchor="middle">pedidos de 1 a 24 horas antes (24)</text>
<rect x="330" y="215" width="290" height="70" rx="12" fill="#162A37" stroke="#5CC98A"/>
<text x="475" y="244" fill="#EAF1F6" font-family="Sora" font-size="14" text-anchor="middle">Média móvel</text>
<text x="475" y="268" fill="#A9B8C6" font-family="Sora" font-size="13" text-anchor="middle">12 horas anteriores (1)</text>
<path d="M620 50 C680 50 680 150 730 150" stroke="#4FD1D4" stroke-width="2" fill="none"/>
<path d="M620 150 H730" stroke="#4FD1D4" stroke-width="2"/>
<path d="M620 250 C680 250 680 150 730 150" stroke="#4FD1D4" stroke-width="2" fill="none" marker-end="url(#taxi-seta)"/>
<rect x="730" y="110" width="210" height="80" rx="12" fill="#162A37" stroke="#F08A7E"/>
<text x="835" y="143" fill="#EAF1F6" font-family="Sora" font-size="15" text-anchor="middle">Random Forest</text>
<text x="835" y="168" fill="#A9B8C6" font-family="Sora" font-size="13" text-anchor="middle">pedidos da próxima hora</text>
</svg>'''

CASO = dict(
    nome="Previsão de pedidos de táxi",
    resumo="Série temporal de pedidos de táxi em aeroportos, com previsão da hora seguinte.",
    tec="Python · pandas · scikit-learn",
    area="modelos",
    lead="Modelo que prevê o número de pedidos de táxi na próxima hora, a partir de seis meses de pedidos em aeroportos. "
         "A meta era erro (REQM) de até 48 pedidos no teste. O Random Forest com profundidade 12 chegou a 47,42.",
    ficha=[("Contexto", "Bootcamp de Ciência de Dados, TripleTen"), ("Problema", "Regressão em série temporal, horizonte de 1 hora"),
           ("Dados", "Pedidos de táxi de março a agosto de 2018"), ("Métrica", "REQM, meta de até 48 pedidos")],
    numeros=[("4.416", "horas na série, de 1º/03 a 31/08/2018"), ("84,4", "pedidos por hora, em média (máximo 462)"),
             ("47,42", "REQM no teste do melhor modelo"), ("44,3%", "da importância vem dos pedidos de 24 horas antes")],
    blocos=[
        ("Objetivo", M.texto([
            "Prever quantos pedidos de táxi chegam na próxima hora. Com a previsão, a empresa aloca motoristas antes dos picos.",
            "Critério de aceite: raiz do erro quadrático médio (REQM) de até 48 pedidos no conjunto de teste."])),
        ("Dados", M.lista([
            ("Origem", "Arquivo de pedidos de táxi em aeroportos, com registros a cada 10 minutos, fornecido pelo curso."),
            ("Tamanho", "4.416 linhas depois de somar os pedidos por hora. Sem valores ausentes e sem horas duplicadas."),
            ("Variável alvo", "num_orders: pedidos na hora. Mediana 78, desvio padrão 45, mínimo 0, máximo 462."),
            ("Divisão", "Ordem do tempo mantida: 3.974 horas para treino (90%) e as últimas 442 para teste (10%).")])),
        ("Organização", M.fluxograma([
            ("Dados", [("CSV de pedidos", "intervalos de 10 minutos"), ("Reamostragem", "soma por hora: 4.416 linhas")], "análise"),
            ("Análise", [("Ciclo diário", "vale entre 3h e 6h, picos à meia-noite e à tarde"), ("Volatilidade", "de menos de 50 a mais de 250 pedidos")], "divisão no tempo"),
            ("Divisão", [("Treino", "3.974 horas (90%)"), ("Teste", "442 horas finais (10%)")], "variáveis"),
            ("Variáveis", [("Calendário", "4"), ("Defasagens", "24"), ("Média móvel", "12 horas")], "treino"),
            ("Modelos", [("Regressão Linear", "referência"), ("Random Forest", "profundidade 8"), ("Random Forest", "profundidade 12")], "avaliação"),
            ("Resultado", [("REQM no teste", "meta de até 48 pedidos")]),
        ], "As médias usadas para preencher as primeiras horas vêm só do treino. Assim o teste não vaza para o treino."), "", "larga"),
        ("Variáveis do modelo", M.diagrama(_DIAGRAMA, "29 variáveis montadas a partir da própria série. Nenhuma fonte externa."), "", "larga"),
        ("Modelos e métricas", M.colunas(
            M.barras([("Random Forest, prof. 12", 47.42, True), ("Random Forest, prof. 8", 48.34), ("Regressão Linear", 48.41)],
                     titulo="REQM no teste (pedidos por hora)", casas=2, nota="Meta: até 48. Só o Random Forest com profundidade 12 ficou abaixo."),
            M.barras([("Random Forest, prof. 12", 12.00, True), ("Random Forest, prof. 8", 17.97), ("Regressão Linear", 25.82)],
                     titulo="REQM no treino (pedidos por hora)", casas=2, nota="Distância grande entre treino e teste: sinal de sobreajuste."))),
        ("Achados", M.achados([
            ("47,42", "REQM no teste do Random Forest com profundidade 12, abaixo da meta de 48."),
            ("44,3%", "da importância do modelo vem da defasagem de 24 horas: a mesma hora do dia anterior."),
            ("12,1%", "vem da hora imediatamente anterior. A média móvel de 12 horas soma 4,8%."),
            ("3h a 6h", "é o vale diário de demanda, com menos de 50 pedidos por hora.")])),
        ("Limites", M.lista([
            ("Margem pequena", "O melhor modelo ficou 0,58 pedido abaixo da meta. Os três modelos ficaram entre 47,42 e 48,41."),
            ("Sobreajuste", "REQM de 12,00 no treino e 47,42 no teste no modelo escolhido."),
            ("Hora do dia", "A hora não entrou como variável. O ciclo diário chega ao modelo só pelas defasagens."),
            ("Período curto", "Seis meses de dados. Não há um ano completo para medir sazonalidade anual.")])),
        ("Gráficos do notebook", M.telas(SLUG, [
            ("01-demanda-cinco-dias.webp", "Pedidos por hora de 24 a 29/08/2018. Pico perto de 400 pedidos em 27/08."),
            ("02-demanda-um-dia.webp", "Um dia de pedidos (24/08/2018): vale na madrugada e picos ao meio-dia e à noite."),
            ("03-previsao-e-importancia.webp", "Em cima, previsto e real no período de teste. Embaixo, as 10 variáveis de maior importância.")]),
         "Imagens geradas pelo notebook do projeto.", "larga"),
    ],
    stack=["Python", "Jupyter", "pandas", "NumPy", "scikit-learn", "Matplotlib"],
)
